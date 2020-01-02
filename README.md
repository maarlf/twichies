# Twitchies
A Twitch SMS notification app, get notified when your favourite streamer is live.

## Requirements
- Python 3.7
- Twitch Developer API
- Twillio Account

## Libraries
- requests, to pull API data
- time, to set timeouts
- twilio client, to send SMS

## Preparations
- Get Twtich.tv Developer Client ID
- Setup Twillio account
- Clone this repo, move to `twitchies` directory and then run `pip install -r requirements.txt`

## How To Use

Copy environment variables
```
$ cp .env.example .env
```

Run it
```
$ python app.py
```
