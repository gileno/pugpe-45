import falcon
import json

class HelloWorld:
    def on_get(self, req, resp):
        resp.body = 'Hello World'

api = falcon.API()
api.add_route('/', HelloWorld())
