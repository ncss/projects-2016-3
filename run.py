#!/usr/bin/env python3
from tornado.ncss import Server
import pprint
from engine import render_file, ParseError

#user has id, email, fname, lname, location, password
#post has userid, message, status, timestamp

user = {1:{'id': 1, 'email' : 'evan@email.com', 'fname': 'Evan', 'lname': 'Kohilas', 'location': 'Sydney', 'password': 'A1B2'},
        2:{'id': 2, 'email' : 'aleks@email.com', 'fname': 'Aleks', 'lname': 'Bricknell', 'location': 'Mount Gambier', 'password': 'qwerty'},
        3:{'id': 3, 'email' : 'katherine@email.com', 'fname': 'Katherine', 'lname': 'Allen', 'location': 'Sydney', 'password': 'hello1'}}

def unknown_handler(response, error):
	response.write('404<br>{}'.format(error))

def home_handler(response):
	#see if authorised or unauthorised
    #display either home page
    response.write('Home!')

def search_handler(response):
    #display search page
    #do search later
    response.write('Search!')

def profile_handler(response, profile_id):
    #displays profile of user with given id
    response.write(render_file('templates\\profile.html', {}))    
    
   
def own_profile_handler(response):
    #redirect to user's own profile page
    profile_handler(response, '1') #always go to profile 1

def edit_profile_handler(response, id):
    #edit profile with given id
    response.write('edit profile {}'.format(id))

def create_profile_handler(response):
    #signup page
    response.write('sign up')

def all_post_handler(response):
    #display all posts
    response.write('all posts')

def new_post_handler(response):
    #new post page
    response.write('new post')

def about_handler(response):
    #about page
    response.write('about')



    

    

server = Server()
server.register(r'/', home_handler, url_name = 'name')
server.register(r'/search', search_handler, url_name = 'search')
server.register(r'/profile/(\d+)', profile_handler, url_name = 'profile')
server.register(r'/profile', own_profile_handler, url_name = 'own_profile')
server.register(r'/profile/(\d+)/edit', edit_profile_handler, url_name = 'edit_profile')
server.register(r'/profile/create', create_profile_handler, url_name = 'create_profile')
server.register(r'/post/all', all_post_handler, url_name = 'all_post')
server.register(r'/post/create', new_post_handler, url_name = 'create_post')
server.register(r'/about', about_handler, url_name = 'about')


server.run()
