import os
import requests

import settings

CLIENT_ID = os.getenv('CLIENT_ID')

def get_stream(user_id):
	url = 'https://api.twitch.tv/kraken/streams/' + str(user_id)
	headers = {
		'Client-ID': CLIENT_ID,
		'Accept': 'application/vnd.twitchtv.v5+json'
	}

	r = requests.get(url, headers=headers)
	return r.json()

if __name__ == '__main__':
	print(get_stream(999))