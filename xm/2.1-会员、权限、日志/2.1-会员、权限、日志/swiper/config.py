'''业务配置以及第三方平台的配置'''

REWIND_TIMES = 3  # 每日反悔次数

# 滑动积分配置
SCORE_LIKE = 5       # 右滑积分
SCORE_DISLIKE = -5   # 左滑积分
SCORE_SUPERLIKE = 7  # 上滑积分


# 云资讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_PARAMS = {
    "sid": 'e749e99071ee277991c27cf9eb62fc8d',
    "token": 'bdcacd327c23b7c6a55adf2955e93c43',
    "appid": '081502fffccd4313bdf6369d36802fd0',
    "templateid": "421727",
    "param": None,
    "mobile": None,
}


# 七牛云配置
QN_URL_PREFIX = 'pvhv7tfry.bkt.clouddn.com'
QN_ACCESS_KEY = 'H-nVN0se7wqWSO1ek2CbVkwfTjQ8JIqFY8tFsU2x'
QN_SECRET_KEY = '6HlyNprKRMfN3wrW6zmg91Tltf0XMVNuUCWd7GOC'
QN_BUCKET = '20190731'
