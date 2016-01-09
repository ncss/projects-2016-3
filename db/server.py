from tornado.ncss import Server

'''
Handler for each path is below
'''
def index_handler(response):
	response.write('Hello World')

server = Server()
server.register('/', index_handler)

