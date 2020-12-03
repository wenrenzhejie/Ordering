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