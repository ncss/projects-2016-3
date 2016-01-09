#!/usr/bin/env python3
import os

from tornado.ncss import Server


def index(response):
    response.write('Hello World!')


port = os.getenv('PORT')
if port:
  server = Server(port=int(port))
else:
  server = Server()

server.register('/', index)
server.run()
