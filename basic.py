# -*- coding:utf-8 -*-
# filename: media.py
import urllib
import time
import json
class Basic:
	def __init__(self):
		self.__accessToken = ''
		self.__leftTime = 0
	def __read_get_access_token(self):
		appId = "wx41c4b459a045f0a6"
		appSecret = "de337b4fcfd03038f87d486ea13884f6"
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=""client_credential&appid=%s&secret=%s"%(appId,appSecret))
		urlResp = urllib.request.urlopen(postUrl)
		urlResp = json.loads(urlResp.read().decode())
		self.__accessToken = urlResp['access_token']
		self.__leftTime = urlResp['expires_in']
	def get_access_token(self):
		if self.__leftTime > 10:
			time.sleep(2)
			self.__lefTime -= 2
		else:
			self.__read_get_access_token()

