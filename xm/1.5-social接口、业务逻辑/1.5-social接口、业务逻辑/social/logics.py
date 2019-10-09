import datetime

from django.core.cache import cache

from swiper import config
from common import errors
from user.models import User
from social.models import Swiped
from social.models import Friend


def rcmd_users(user):
    '''用户推荐'''
    # 筛选出所有被当前用户划过的用户的 uid
    swiped = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_uid_list = [sw.sid for sw in swiped]

    # 再把自己加进去
    swiped_uid_list.append(user.id)

    # 计算 出生年份 的范围
    curr_year = datetime.date.today().year  # 当前年份
    max_birth_year = curr_year - user.profile.min_dating_age
    min_birth_year = curr_year - user.profile.max_dating_age

    # 根据条件筛选 user 对象
    users = User.objects.filter(
        location=user.profile.location,
        sex=user.profile.dating_sex,
        birth_year__range=[min_birth_year, max_birth_year]
    ).exclude(id__in=swiped_uid_list)[:20]

    return users


def like(user, sid):
    '''喜欢了某人'''
    # 添加滑动记录
    # 调用了类方法
    Swiped.swipe('like', user.id, sid)

    # 检查对方是否喜欢过你
    # 调用了类方法
    if Swiped.is_liked_someone(sid, user.id):
        # 建立好友关系
        # 类方法
        Friend.make_friends(user.id, sid)
        # TODO: 向好友推送完成匹配的消息 (集成消息推送服务)
        # 1. 应用内消息通知，只有当接收消息的人打开app的时候才能看到
        # 2. 消息推送的方式，把消息push到用户手机的通知栏
        #   a. iOS 只有一种做法：调用苹果的Push Notification服务
        #   b. Android 有两种做法：
        #     i. 自己写一个Android的后台服务，跟自己的服务器建立长链接，有消息推过来就提示用户
        #     ii. 集成第三方的消息推送服务，它自己肯定也有一个Android后台服务活着，跟他的服务器通信

        return True  # 返回完成匹配的结果
    else:
        return False


def superlike(user, sid):
    '''超级喜欢了某人'''
    # 添加滑动记录
    Swiped.swipe('superlike', user.id, sid)

    # 检查对方是否喜欢过你
    if Swiped.is_liked_someone(sid, user.id):
        # 建立好友关系
        Friend.make_friends(user.id, sid)
        # TODO: 向好友推送完成匹配的消息 (集成消息推送服务)
        # 向被滑动的用户，发送短信

        return True  # 返回完成匹配的结果
    else:
        return False


def rewind(user):
    '''
    每天允许撤销 3 次
    '''
    # 获取当前日期已反悔的次数
    now = datetime.datetime.now()
    # key = 'Rewind-%s-%s' % (user.id, now.date())
    key = 'Rewind-%s' % user.id

    # 隐患
    # 每24小时允许反悔三次
    # 每个自然日允许反悔三次
    # rewind_times = cache.get(key, 0, 86400)
    rewind_times = cache.get(key, 0)
    # 分钟：1440
    # 秒：86400

    # 次数检查
    if rewind_times < config.REWIND_TIMES:
        rewind_times += 1
        # 计算到晚上凌晨剩余的秒数
        remain_second = 86400 - (now.hour * 3600 + now.minute * 60 + now.second)
        # 添加缓存记录，精确的到本日结束，这个 key 过期
        cache.set(key, rewind_times, remain_second)
        # 按 stime 排序，把最后一次的滑动记录找出来
        record = Swiped.objects.filter(uid=user.id).latest('stime')
        # 撤销好友记录
        Friend.break_off(user.id, record.sid)
        # 删除滑动记录
        record.delete()
    else:
        raise errors.RewindLimited('反悔次数达到每日上限')


def get_users_liked_me(user):
    '''获取喜欢过我的用户列表'''
    uid_list = Swiped.liked_me(user.id)
    return User.objects.filter(id__in=uid_list)
