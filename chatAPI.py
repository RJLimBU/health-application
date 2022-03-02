import datetime
import json

def readMessage(user_id, sender, recipient, messageType, content):
	curtime = datetime.datetime.now()
	date = curtime.strftime("%x")
	time = curtime.strftime("%X") 

	if user_id==None or user_id is not int:
		return "error: incorrect user id"

	if messageType == "text":
		chatMessage = {
		'user_id': user_id,	
		'sender': sender,			#username of the sender
		'recipient': recipient,		#id of receiver
		'date': date,			# date of message sent
		'time': time, 			# time of message sent
		'messageType': messageType, 	# type of messages
		'cotent': {
			'msg': content,		# content
			'link': None		# empty
			}
		}
	else:
		chatMessage = {
		'user_id': user_id,	
		'sender': sender,			#username of the sender
		'recipient': recipient,		#id of receiver
		'date': date,			# date of message sent
		'time': time, 			# time of message sent
		'messageType': messageType, 	# type of messages
		'cotent': {
			'msg': None,		# content
			'link': content		# empty
			}
		}
	

	jstr = json.dumps(chatMessage, indent=4)

	return jstr


# out = readMessage(1, "joe", "doctor1", "text", "hello")
# print(out)
# print(type(out))
