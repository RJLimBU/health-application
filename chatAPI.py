import datetime
import json
import pymongo

checkMsgType = ["text", "voice", "image", "video"]

def readMessage(user_id, sender, recipient, messageType, content):
	curtime = datetime.datetime.now()
	date = curtime.strftime("%x")
	time = curtime.strftime("%X") 

	if user_id==None or type(user_id) is not int:
		return {'error': "incorrect user id format"}
	if sender==None or type(sender) is not str:
		return {'error': "incorrect sender format"}
	if recipient==None or type(recipient) is not str:
		return {'error': "incorrect recipient format"}
	if messageType==None or type(messageType) is not str:
		return {'error': "incorrect messageType format"}
	if content==None or type(content) is not str:
		return {'error': "incorrect content format"}
	if messageType not in checkMsgType:
		return {'error': "message type must be text/voice/image/video"}

	if messageType == "text":
		chatMessage = {
		'user_id': user_id,			#user id need to be greater than 0
		'sender': sender,			#username of the sender
		'recipient': recipient,		#id of receiver
		'date': date,			# date of message sent
		'time': time, 			# time of message sent
		'messageType': messageType, 	# type of messages
		'content': {
			'msg': content,		# content
			'link': None		# empty
			}
		}
	else:
		chatMessage = {
		'user_id': user_id,			#user id need to be greater than 0
		'sender': sender,			#username of the sender
		'recipient': recipient,		#id of receiver
		'date': date,			# date of message sent
		'time': time, 			# time of message sent
		'messageType': messageType, 	# type of messages
		'content': {
			'msg': None,		# content
			'link': content		# empty
			}
		}
	

	return chatMessage
	#jstr = json.dumps(chatMessage, indent=4)
	#return jstr

# out = readMessage(1, "joe", "doctor1", "text", "hello")
# print(out)
# print(type(out))
# print(out['content']['msg'])
# print(out['content']['link'])
# out = readMessage(1, "joe", "doctor1", "esst", "hello")
# print(out)
# chk = out.get('user_id',0)
# if chk:
# 	print(out[user_id])
# else:
# 	print(out['error'])