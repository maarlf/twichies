import os
import requests

import settings

CLIENT_ID = os.getenv('CLIENT_ID')

def get_stream():
	url = 'https://api.twitch.tv/kraken/streams'
	headers = {'Client-ID': CLIENT_ID}
	params = {
		'Accept': 'application/vnd.twitchtv.v5+json',
		'channel': '<Channel Name>'
	}

	r = requests.get(url, headers=headers, params=params)
	return r.json()

if __name__ == '__main__':
	print(get_stream())