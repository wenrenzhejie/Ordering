from application import app
from flask import request,redirect,g
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
from common.libs.LogService import LogService
import re
@app.before_request
def before_request():
    g.current_user = None
    ignore_urls = app.config["IGNORE_URLS"]
    ignore_check_login_urls = app.config["IGNORE_CHECK_LOGIN_URLS"]
    path = request.path
    pattern = re.compile("%s"%"|".join(ignore_check_login_urls))
    if pattern.match(path):
        return
    pattern = re.compile("%s" % "|".join(ignore_urls))
    if pattern.match(path):
        return
    user_info = check_login()
    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))
    g.current_user = user_info
    LogService.addAccessLog()
    return

def check_login():
    cookies = request.cookies
    auth_cookie = cookies["user"] if "user" in cookies else ""
    # app.logger.error(auth_cookie)
    if auth_cookie is None:
        return False
    auth_info = auth_cookie.split("#")
    if len(auth_info) < 2:
        return False
    user_info = User.query.filter_by(uid=auth_info[1]).first()
    if user_info is None:
        return False
    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False
    if user_info.status != 1:
        return False
    return user_info