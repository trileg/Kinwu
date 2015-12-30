#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from twitter import *


def brain():
    api_key = os.environ.get("KINWU_API_KEY")
    api_secret = os.environ.get("KINWU_API_SECRET")
    access_token = os.environ.get("KINWU_ACCESS_TOKEN")
    access_token_secret = os.environ.get("KINWU_ACCESS_TOKEN_SECRET")
    dm_to = os.environ.get("KINWU_DM_TO")

    while True:
        api = OAuth(access_token, access_token_secret, api_key, api_secret)
        t = Twitter(auth=api)
        twitter_userstream = TwitterStream(auth=api, domain='userstream.twitter.com')

        for msg in twitter_userstream.user():
            if 'direct_message' in msg:
                message = msg['direct_message']['text']
                if 'ping' in message:
                    t.direct_messages.new(user=dm_to, text="pong")
                elif 'hoge' in message:
                    t.direct_messages.new(user=dm_to, text="fuga")


if __name__ == '__main__':
    brain()
