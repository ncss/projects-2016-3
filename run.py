#!/usr/bin/env python3
from tornado.ncss import Server
import pprint
import hashlib
import os
from engine import render_file, ParseError
from models.User import User

#user has id, email, fname, lname, location, password
#post has id, userid, message, status, timestamp
#status is 0-2
#skill has skill id, skill name, category id, rank,
#skill categories - 1=medicine, 2=engineering, currently ranked 1-10

users = {1:{'user_id': 1, 'email' : 'evan@email.com', 'fname': 'Evan', 'lname': 'Kohilas', 'location': 'Sydney', 'password': 'A1B2', 'age':'18', 'gender':'Male'},
        2:{'user_id': 2, 'email' : 'aleks@email.com', 'fname': 'Aleks', 'lname': 'Bricknell', 'location': 'Mount Gambier', 'password': 'qwerty', 'age':'18', 'gender':'Male'},
        3:{'user_id': 3, 'email' : 'katherine@email.com', 'fname': 'Katherine', 'lname': 'Allen', 'location': 'Sydney', 'password': 'hello1'}
}

user = {1:User(1, 'evan@email.com', 'Evan', 'Kohilas', '12/10/97', 'Sydney', 'M', '', '123456789'),
        2:User(2, 'amy@email.com', 'Amy', "O'Rourke", '7/10/99', 'Newcastle', 'F', '', '98765432'),
        3:User(3, 'aleks@email.com', 'Aleks', 'Bricknell', '27/06/98', 'Syndey', 'M', '', '67893456')
        }


posts = {1:{'id': 1, 'userid': 1, 'message' : "I'm ok", 'status': 0},
        2:{'id': 2, 'userid': 1, 'message' : "I'm still ok", 'status': 0},
        3:{'id': 3, 'userid': 2, 'message' : "I'm not ok", 'status': 1},
}
skills = {1:{'id':1, 'skill name': 'first aider', 'category id':1, 'rank':1},
        2:{'id':2, 'skill name': 'emergency doctor', 'category id':1, 'rank':8},
        3:{'id':3, 'skill name': 'structural engineer', 'category id':2, 'rank':6}
        }

def get_cookie(response):
    return response.get_secure_cookie("userLoggedIn")

def login_required(function):
    #login decorator
    #check if user is logged in, if not redirect to home
    def inner(response, *args, **kwargs):
        if get_cookie(response):
            return function(response, *args, **kwargs)
        else:
            return return_403(response)
    return inner

def return_403(response, *args, **kwargs):
    response.set_status(403)
    response.write("403")
    #render(response, '403.html', {})

def login_handler(response):
    #database password check
    #assume database stuff worked fine
    email = response.get_field("email")
    password = hashlib.sha256(response.get_field("password").encode('ascii')).hexdigest()

    if User.verify_password(email, password):
        response.set_secure_cookie("userLoggedIn", User.getPerson(email).user_id)
        response.redirect('/')
    else:
        response.write("wrong login")

def logout_handler(response):
    response.clear_cookie("userLoggedIn")
    response.redirect('/')

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

@login_required
def search_handler(response):
    #display search page
    #do search later
    response.write(render_file(os.path.join('templates', 'search.html'), {"name": "WildCats!"}))

@login_required
def profile_handler(response, profile_id):
    #displays profile of user with given id
    userID = int(profile_id)
    response.write(render_file(os.path.join('templates', 'profile.html'), {'User':user[userID]}))

def own_profile_handler(response):
    #redirect to user's own profile page
    userID = get_cookie()
    if userID:
        profile_handler(response, userID)
    else:
        response.redirect('/')

@login_required
def edit_profile_handler(response, id):
    #edit profile with given id
    response.write(render_file(os.path.join('templates', 'profile_edit.html'), {}))
    #response.write('edit profile {}'.format(id))

@login_required
def create_profile_handler(response):
    #signup page
    response.write(render_file(os.path.join('templates', 'create.html'), {}))

@login_required
def all_post_handler(response):
    # display all posts
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
    #display all posts

@login_required
def new_post_handler(response):
    #new post page
    response.write(render_file(os.path.join('templates', 'addpost.html'), {}))

def about_handler(response):
    #about page
    response.write('about')

def default_handler(response, method, *args, **kwargs):
    #default 404
    return return_404(response)

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
server.set_default_handler(default_handler)

server.run()
