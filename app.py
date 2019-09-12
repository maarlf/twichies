from twilio.rest import Client

import os
import requests

import settings


# Twitch
CLIENT_ID = os.getenv('CLIENT_ID')


# Twillio
ACCOUNT_SID = os.getenv('TWILLIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILLIO_AUTH_TOKEN')
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# Gets the user objects for the specified Twitch login names
def get_user_id(login):
	url = 'https://api.twitch.tv/kraken/users'
	headers = {
		'Client-ID': CLIENT_ID,
		'Accept': 'application/vnd.twitchtv.v5+json'
	}
	params = {
		'login': login
	}

	r = requests.get(url, headers=headers, params=params)
	return r.json()


# Gets stream information (the stream object) for a specified user
def get_stream(user_id):
	url = 'https://api.twitch.tv/kraken/streams/' + str(user_id)
	headers = {
		'Client-ID': CLIENT_ID,
		'Accept': 'application/vnd.twitchtv.v5+json'
	}

	r = requests.get(url, headers=headers)
	return r.json()


def send_notification(streams):
	message_from = os.getenv('TWILLIO_FROM')
	message_to = os.getenv('TWILLIO_TO')
	message_body = login + ' is streaming, go watch it'

	message = client.messages \
		.create(
			body=message_body,
			from_=message_from,
			to=message_to
		)

	return message.sid

if __name__ == '__main__':
	login = 'streamer_name'
	user_id = get_user_id(login)['users'][0]['_id']
	streams = get_stream(user_id)
	if streams['stream'] is None:
		print(login + ' is not streaming right now')
	else:
		send_notification(streams)