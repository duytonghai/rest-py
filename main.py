# sample.py
import falcon
import json


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'Soon ripe soon rotten',
            'author': 'Dito'
        }

        resp.body = json.dumps(quote)

    def on_post (self, req, resp):
        """Handles POST requests"""
        req_body = req.stream.read()
        body = json.loads(req_body.decode('utf-8'))
        resp_body = {
            'data': 'Post succeeded with id: ' + str(body['value'])
        }

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(resp_body)

api = falcon.API()
api.add_route('/quote', QuoteResource())
