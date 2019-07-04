# -*- coding: utf-8 -*-
# filename: reply.py
import time

class Msg(object):
	def __init__(self):
		pass
	def send(self):
		return success 
class TextMsg(Msg):
	def __init__(self,toUserName,fromUserName,content):
		print("textmsginit")
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content
	def send(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[text]]></MsgType>
		<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		return XmlForm.format(**self.__dict)
class ImageMsg(Msg):
	print("msg")
	def __init__(self,toUserName,fromUserName,mediaId):
		print("imagemsginit")
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MediaId'] = mediaId
		print(2)
	def send(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[image]]></MsgType>
		<Image>
		<MediaId><![CDATA[{MediaId}]]></mediaId>
		</Image>
		</xml>
		"""
		print(1)
		return XmlForm.format(**self.__dict)
