# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.libs.user.Helper import ops_render
route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    return ops_render( "index/index.html")