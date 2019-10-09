import datetime

from user.models import User
from social.models import Swiped


def rcmd_users(user):
    '''用户推荐'''
    # 筛选出所有被当前用户划过的用户的 uid
    swiped = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_uid_list = [sw.sid for sw in swiped]
    swiped_uid_list.append(user.id)  # 排除自己

    # 计算出生年份的范围, 2019
    curr_year = datetime.date.today().year  # 当前年份

    # min_dating_age = 20, max_dating_age = 35
    # max_birth_year = 2019 - 20 = 1999
    max_birth_year = curr_year - user.profile.min_dating_age
    # min_birth_year = 2019 - 35 = 1984
    min_birth_year = curr_year - user.profile.max_dating_age

    # 根据条件筛选 user 对象
    users = User.objects.filter(
        location=user.profile.location,
        sex=user.profile.dating_sex,
        birth_year__range=[min_birth_year, max_birth_year]
    ).exclude(id__in=swiped_uid_list)[:20]

    return users
