import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import src.services as services
from src.students import student_info_att
import src.netra_id as netra_id


app = Flask(__name__)

@app.route('/student', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').strip()

	resp = MessagingResponse()
	msg = resp.message()

	incoming_msg = incoming_msg.lower()
	output="Something went Wrong !!!"
	bk="```"
	if 'help' in incoming_msg:
		output='''
		
Yoo!!! 🤟

COMMANDS :

1) Enter your jntuh rollno -> get ur details/attandence 
	example :
		20bd1a6647
	result :

		SANJUTH REDDY PULLAGURLA 
		3rd year
		CSM-A

		Overall Attendence %: 71.84%

		Subject wise Attendence :
		DLVS : 70.21%
		DAA : 71.43%
		SE : 65.85%
		WT : 78.57%
		PPG : 85.29%
		MENTOR : 100%
		WT_LAB : 40%

	# ik my attendence sucks ;_;

2) date -> gives the date obslyy

3) joke -> makes aa lame joke, lol

4) motivate -> gives a quote which half of us dont even understand :)

5) help -> u can figure out what this does👍

Thank You 😎!!!

'''
		bk="```"
		output=f"{bk}{output}{bk}"

	elif 'date' in incoming_msg:
		output = services.get_date()

	elif 'joke' in incoming_msg:
		output = services.get_joke()

	elif 'motivate' in incoming_msg:
		output = services.get_quote()

	elif incoming_msg[0:2]=='20':
		if netra_id.isValidId(incoming_msg):
			output = student_info_att(incoming_msg)
		else:
			output = "Not a Valid roll"
	else:
		output='''
		
Yoo!!! 🤟

COMMANDS :

1) Enter your jntuh rollno -> get ur details/attandence 
	example :
		20bd1a6647
	result :

		SANJUTH REDDY PULLAGURLA 
		3rd year
		CSM-A

		Overall Attendence %: 71.84%

		Subject wise Attendence :
		DLVS : 70.21%
		DAA : 71.43%
		SE : 65.85%
		WT : 78.57%
		PPG : 85.29%
		MENTOR : 100%
		WT_LAB : 40%

	# ik my attendence sucks ;_;

2) date -> gives the date obslyy

3) joke -> makes aa lame joke, lol

4) motivate -> gives a quote which half of us dont even understand :)

5) help -> u can figure out what this does👍

Thank You 😎!!!

'''
		bk="```"
		output=f"{bk}{output}{bk}"
	msg.body(output)
	return str(resp)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8080)