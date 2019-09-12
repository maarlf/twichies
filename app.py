import os
import requests

import settings


CLIENT_ID = os.getenv('CLIENT_ID')


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


if __name__ == '__main__':
	login = '<Twitch Name>'
	user_id = get_user_id(login)['users'][0]['_id']
	print(get_stream(user_id))