#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import *
import configparser


def brain():
    config = configparser.ConfigParser()
    config.read('twitter_key.ini')
    api_key = config['apikey']['API_Key']
    api_secret = config['apikey']['API_Secret']
    access_token = config['apikey']['Access_Token']
    access_token_secret = config['apikey']['Access_Token_Secret']

    while True:
        api = OAuth(access_token, access_token_secret, api_key, api_secret)
        twitter_userstream = TwitterStream(auth=api, domain='userstream.twitter.com')

        for msg in twitter_userstream.user():
            if 'direct_message' in msg:
                message = msg['direct_message']['text']
                print(message)


if __name__ == '__main__':
    brain()
