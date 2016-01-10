#!/usr/bin/env python3
from tornado.ncss import Server
import pprint
import hashlib
import os
from engine import render_file, ParseError
from models import User

#user has id, email, fname, lname, location, password
#post has id, userid, message, status, timestamp
#status is 0-2
#skill has skill id, skill name, category id, rank,
#skill categories - 1=medicine, 2=engineering, currently ranked 1-10
users = {1:{'user_id': 1, 'email' : 'evan@email.com', 'fname': 'Evan', 'lname': 'Kohilas', 'location': 'Sydney', 'password': 'A1B2', 'age':'18', 'gender':'Male'},
        2:{'user_id': 2, 'email' : 'aleks@email.com', 'fname': 'Aleks', 'lname': 'Bricknell', 'location': 'Mount Gambier', 'password': 'qwerty'},
        3:{'user_id': 3, 'email' : 'katherine@email.com', 'fname': 'Katherine', 'lname': 'Allen', 'location': 'Sydney', 'password': 'hello1'}
}
'''
posts = {1:{'id': 1, 'userid': 1, 'message' : "I'm ok", 'status': 0},
        2:{'id': 2, 'userid': 1, 'message' : "I'm still ok", 'status': 0},
        3:{'id': 3, 'userid': 2, 'message' : "I'm not ok", 'status': 1},
}
'''
skills = {1:{'id':1, 'skill name': 'first aider', 'category id':1, 'rank':1},
        2:{'id':2, 'skill name': 'emergency doctor', 'category id':1, 'rank':8},
        3:{'id':3, 'skill name': 'structural engineer', 'category id':2, 'rank':6}
        }

def get_cookie(response):
    return response.get_secure_cookie("userLoggedIn")

def login_handler(response):
    #database password check
    #assume database stuff worked fine
    email = response.get_field("email")
    password = hashlib.sha256(response.get_field("password").encode('ascii')).hexdigest()

    if User.verify_password(email, password):
        response.set_secure_cookie("userLoggedIn", User.getPerson(email).get_user_id())
        response.redirect('/')
    else:
        response.write("wrong login")

def logout_handler(response):
    response.clear_cookie("userLoggedIn")
    response.redirect('/')

def unknown_handler(response, error):
	response.write('404<br>{}'.format(error))

def home_handler(response):
	#see if authorised or unauthorised
    #display either home page
    #login(response, '2')
    #response.write(str(response.get_secure_cookie("userLoggedIn")))
    userLoggedIn = get_cookie(response)
    if userLoggedIn:
        response.write(User.getPerson(int(userLoggedIn)).fname + ' is logged in')
    else:
        response.write('Not logged in!')
    response.write('Home!')

def search_handler(response):
    #display search page
    #do search later
    response.write(render_file(os.path.join('templates', 'search.html'), {}))




def profile_handler(response, profile_id):
    #displays profile of user with given id
    personInfo = users[1]
    response.write(render_file(os.path.join('templates', 'profile.html'), personInfo))
  





def own_profile_handler(response):
    #redirect to user's own profile page
    '''
    userID = get_cookie()
    if userID:
        profile_handler(response, userID)
    else:
        response.redirect('/')
    '''

    response.write('profile')

def edit_profile_handler(response, id):
    #edit profile with given id
    response.write('edit profile {}'.format(id))

def create_profile_handler(response):
    #signup page
    response.write(render_file(os.path.join('templates', 'create.html'), {}))

def all_post_handler(response):
    '''
    userID = get_cookie()
    if userID:
        posts = Post.get10()
        for post in posts:
            response.write(post.message + '<br>')
            userName = User.get_user(post.author_id).fname
            response.write('by' + userName + '<br>')
            response.write('all posts')
    else:
        response.redirect('/')
    '''
    response.write('posts')
    #display all posts

def new_post_handler(response):
    #new post page
    response.write(render_file(os.path.join('templates', 'addpost.html'), {}))

def about_handler(response):
    #about page
    response.write('about')

server = Server()
server.register(r'/', home_handler, url_name = 'name')
server.register(r'/login', login_handler, url_name = 'login')
server.register(r'/logout', logout_handler, url_name = 'logout')
server.register(r'/search', search_handler, url_name = 'search')
server.register(r'/profile/(\d+)', profile_handler, url_name = 'profile')
server.register(r'/profile', own_profile_handler, url_name = 'own_profile')
server.register(r'/profile/(\d+)/edit', edit_profile_handler, url_name = 'edit_profile')
server.register(r'/profile/create', create_profile_handler, url_name = 'create_profile')
server.register(r'/post/all', all_post_handler, url_name = 'all_post')
server.register(r'/post/create', new_post_handler, url_name = 'create_post')
server.register(r'/about', about_handler, url_name = 'about')

server.run()
