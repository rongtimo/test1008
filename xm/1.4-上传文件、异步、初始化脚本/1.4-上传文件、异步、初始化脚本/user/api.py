from django.core.cache import cache

from lib.http import render_json
from lib.sms import send_vcode
from common import keys
from common import errors
from user.models import User
from user.forms import ProfileForm
from user import logics


def submit_phone(request):
    '''提交手机号，发送验证码'''
    # phone = request.POST.get('phone')
    phone = request.GET.get('phone')
    send_vcode(phone)
    return render_json(None)


def submit_vcode(request):
    '''提交短信验证码，登录'''
    # phone = request.POST.get('phone')
    # vcode = request.POST.get('vcode')
    phone = request.GET.get('phone')
    vcode = request.GET.get('vcode')

    cache_vcode = cache.get(keys.VCODE_KEY % phone)

    if vcode == cache_vcode:
        # 执行登录过程
        user, _ = User.objects.get_or_create(phonenum=phone, nickname=phone)

        # 在 session 中记录登录状态
        request.session['uid'] = user.id

        return render_json(user.to_dict())
    else:
        return render_json('验证码错误', errors.VCODE_ERR)


def get_profile(request):
    '''获取个人资料'''
    user = request.user
    return render_json(user.profile.to_dict())


def set_profile(request):
    '''修改个人配置'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.id = request.session['uid']
        profile.save()
        return render_json(None)
    else:
        return render_json(form.errors, errors.PROFILE_ERR)


def upload_avatar(request):
    '''头像上传'''
    user = request.user
    avatar = request.FILES.get('avatar')  # 取出文件对象

    logics.upload_avatar.delay(user, avatar)
    return render_json(None)
