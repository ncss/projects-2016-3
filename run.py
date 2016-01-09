#!/usr/bin/env python3
from tornado.ncss import Server


def home_handler(response):
    #see if authorised or unauthorised
    #display either home page
    response.write('Home!')

def search_handler(response):
    #display search page
    #do search later
    response.write('Search!')

def profile_handler(response, id):
    #displays profile of user with given id 
    response.write(id)

def own_profile_handler(response):
    #redirect to user's own profile page
    response.redirect('/profile/1') #always go to profile 1

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
server.register(r'/', home_handler)
server.register(r'/search', search_handler)
server.register(r'/profile/(\d+)', profile_handler)
server.register(r'/profile', own_profile_handler)
server.register(r'/profile/(\d+)/edit', edit_profile_handler)
server.register(r'/profile/create', create_profile_handler)
server.register(r'/post/all', all_post_handler)
server.register(r'/post/create', new_post_handler)
server.register(r'/about', about_handler)


server.run()
