# -*- coding: utf-8 -*-
# Author: Mark Spicer
# License: MIT

import json

import openroast_api


class Recipes(object):
    def on_get(self, req, resp):
        data = []
        keys = openroast_api.db.keys()
        for key in keys:
            data.append(key.decode('utf-8'))
        resp.body = json.dumps({'data': data})


class Details(object):
    def on_get(self, req, resp, recipe_id):
        data = []
        try:
            recipe = json.loads(openroast_api.db.get(recipe_id).decode('utf-8'))
            data.append(recipe)
        except:
            openroast_api.logger.error("Nope!")

        resp.body = json.dumps({'data': data})
