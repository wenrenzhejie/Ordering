DEBUG=True
SQLALCHEMY_ECHO=True
SQLALCHEMY_ENCODING="utf-8"
SERVER_PORT=9000
SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
JSON_AS_ASCII=False

##过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}
PAGE_SIZE=50
PAGE_DISPLAY=10



MINA_APP={
    "appid":"wx4ef416cbfab4b7c3",
    "appkey":"6b56c913e3cdc88627f179d72ac30c01"
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://127.0.0.1:9000'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}