from web.controllers.api import route_api
from flask import request,jsonify
from application import app,db
from common.models.member.Member import Member
from common.libs.user.Helper import getCurrentDate
from common.models.member.OauthMemberBind import OauthMemberBind
import requests
import json
@route_api.route("/member/login",methods=["GET","POST"])
def login():
    resp = {"code":200,"msg":"操作成功","data":{}}
    req = request.values
    code = req["code"] if "code" in req else ""
    if not code or len(code) < 1:
        resp["code"] = -1
        resp["msg"] = "需要code"
        return jsonify(resp)

    secret="6b56c913e3cdc88627f179d72ac30c01"
    url="https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(app.config["MINA_APP"]["appid"],app.config[MINA_APP]["appkey"],code)
    r = requests.get(url)
    res = json.loads(r.text)
    openid = res["openid"]
    nickname = req['nickName'] if 'nickName' in req else ''
    sex = req['gender'] if 'gender' in req else 0
    avatar = req['avatarUrl'] if 'avatarUrl' in req else ''

    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        model_member = Member()
        model_member.nickname = nickname
        model_member.sex = sex
        model_member.avatar = avatar
        model_member.salt = MemberService.geneSalt()
        model_member.updated_time = model_member.created_time = getCurrentDate()
        db.session.add(model_member)
        db.session.commit()

        model_bind = OauthMemberBind()
        model_bind.member_id = model_member.id
        model_bind.type = 1
        model_bind.openid = openid
        model_bind.extra = ''
        model_bind.updated_time = model_bind.created_time = getCurrentDate()
        db.session.add(model_bind)
        db.session.commit()

        bind_info = model_bind

    return jsonify(resp)


