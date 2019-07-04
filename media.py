# -*- coding: utf-8 -*-
# filename: media.py
import os
from basic import Basic
import urllib.request
import poster.encode
from poster.streaminghttp import register_openers
print(os.getcwd())
class Media(object):
	def __init__(self):
		register_openers()
	#上传图片
	def uplaod(self,accessToken,filePath,mediaType):
		openFile = open(filePath,"rb")
		param = {'media':openFile}
		postData,postHeaders = poster.encode.multipart_encode(param)
		
		postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken,mediaType)
		request = urllib.request.Request(postUrl,postData,postHeaders)
		urlResp = urllib.request.urlopen(request)
		print(urlResp.read())


if __name__ == '__main__':
	myMedia = Media()
	accessToken = Basic().get_access_token()
	filePath = os.getcwd()+"/test.jpg"
	mediaType = "image"
	myMedia.uplaod(accessToken,filePath,mediaType)
