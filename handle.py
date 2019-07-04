# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import web
import reply
import receive
class  Handle(object):
		def GET(self):
			try:
				data = web.input()
				
				if len(data) == 0:
					return "hello, this is handle view"
				signature = data.signature
				print(signature)
				timestamp = data.timestamp
				print(timestamp)
				nonce = data.nonce
				print(nonce)
				echostr = data.echostr
				print(echostr)
				token = "mytoken"

				list = [token,timestamp,nonce]
				print(list)
				list.sort()
				print(list)
				list2 = ''.join(list)
				sha1 = hashlib.sha1()
				print(sha1)
				sha1.update(list2.encode('utf-8'))
				print(sha1)
				hashcode = sha1.hexdigest()
				print(hashcode)
				print(signature)
				print ("handle/GET func: hashcode, signature: ", hashcode, signature)
				if hashcode == signature:
					return echostr
				else:
					return ""
			except Exception as Argument:
				return Argument

		def POST(self):
			try:
				webData = web.data()
				print("Handle Post webdata is",webData)
			#后台打印日志
				recMsg = receive.parse_xml(webData)
				print(recMsg)
				if isinstance(recMsg,receive.Msg):
					print(recMsg)
					print(receive.Msg)
					toUser = recMsg.FromUserName
					fromUser = recMsg.ToUserName
					print(recMsg.MsgType)
					if recMsg.MsgType == 'text':
						print("text")
						content = recMsg.Content.decode('utf-8')
						replyMsg = reply.TextMsg(toUser,fromUser,content)
						return replyMsg.send()
					if recMsg.MsgType == 'image':
						mediaId = recMsg.MediaId
						print(mediaId)
						print(11111111111111111)
						replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
						print(replyMsg)
						print(11111111111)
						return replyMsg.send()
					else:
						return reply.Msg().send()
				else:
					print("暂且不处理未识别的消息")
					return success
			except Exception as Argment:
				return Argment

