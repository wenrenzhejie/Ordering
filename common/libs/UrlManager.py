# -*- coding: utf-8 -*-
from application import app,db
import time
class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%( int(time.time()) )
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildImageUrl(path):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        return url