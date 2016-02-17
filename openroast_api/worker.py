# -*- coding: utf-8 -*-
# Author: Mark Spicer
# License: MIT

import os
import json
import requests

import openroast_api


def run():
    openroast_api.logger.debug("Started worker.")
    token = 'access_token=423796024493328|' + os.environ['FACEBOOK_API_KEY']
    url = 'https://graph.facebook.com/v2.5/666764253452044/files?' + token
    r = requests.get(url)
    data = r.json()
    file_list = data['data']

    for item in file_list:
        recipe_id = item['id']
        url = 'https://www.facebook.com/download/' + recipe_id
        r = requests.get(url)

        try:
            recipe = r.json()
            name = recipe['roastName']
            openroast_api.logger.debug("Found recipe: " + name)
        except:
            continue

        openroast_api.db.set(recipe_id, json.dumps(recipe))
