#!/usr/bin/env python3
import os

from tornado.ncss import Server
import pprint
import hashlib
import os
from engine import render_file, ParseError
from models.User import User
from models.Post import Post

#user has id, email, fname, lname, location, password
#post has id, userid, message, status, timestamp
#status is 0-2
#skill has skill id, skill name, category id, rank,
#skill categories - 1=medicine, 2=engineering, currently ranked 1-10
#user passwords = 12345, qwerty, 98765
user = {1:User(1, 'evan@email.com', 'Evan', 'Kohilas', '12/10/97', 'Sydney', 'M', '', '123456789', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'),
        2:User(2, 'amy@email.com', 'Amy', "O'Rourke", '7/10/99', 'Newcastle', 'F', '', '98765432', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5'),
        3:User(3, 'aleks@email.com', 'Aleks', 'Bricknell', '27/06/98', 'Sydney', 'M', '', '67893456', '79737ac46dad121166483e084a0727e5d6769fb47fa9b0b627eba4107e696078')
        }
emails = {'evan@email.com':1, 'amy@email.com':2, 'aleks@email.com':3}

posts = {1:{'id': 1, 'userid': 1, 'message' : "I'm ok", 'status': 0},
        2:{'id': 2, 'userid': 1, 'message' : "I'm still ok", 'status': 0},
        3:{'id': 3, 'userid': 2, 'message' : "I'm not ok", 'status': 1},
}

post = {1:Post(1, "I'm in trouble", 1, 2, 12), 
        2:Post(2, "I'm ok", 2, 0, 13),
        3:Post(3, "I'm not in trouble, but not ok", 3, 1, 14)}


skills = {1:{'id':1, 'skill name': 'first aider', 'category id':1, 'rank':1},
        2:{'id':2, 'skill name': 'emergency doctor', 'category id':1, 'rank':8},
        3:{'id':3, 'skill name': 'structural engineer', 'category id':2, 'rank':6}
        }

def get_cookie(response):
    return 1
    #return response.get_secure_cookie("userLoggedIn")

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

def return_404(response, *args, **kwargs):
  response.set_status(404)
  response.write(render_file(os.path.join('templates', '404.html'), {}))

def login_handler(response):
    #database password check
    #assume database stuff worked fine
    email = response.get_field("email")
    password = hashlib.sha256(response.get_field("password").encode('ascii')).hexdigest()

    if User.verify_password(email, password):
        userID = emails[email] #fix this once db is integrated
        response.set_secure_cookie("userLoggedIn", str(user[userID].get_user_id()))
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
        userLoggedIn = int(userLoggedIn)
        #response.write(User.get_person(int(userLoggedIn)).fname + ' is logged in')
        response.write(user[userLoggedIn].get_first_name() + ' is logged in')
    else:
        response.write('Not logged in!')
    response.write('Home!')

@login_required
def search_handler(response):
    #display search page
    #do search later
    response.write(render_file(os.path.join('templates', 'search.html'), {}))

@login_required
def send_to_handler(response):
    pass
    ''' relying on get_people
    query = response.get_field('search-query')
    results = User.get_people(name)
    response.write(results)
    '''

@login_required
def profile_handler(response, profile_id):
    #displays profile of user with given id
    #personInfo = users[1]
    userID = int(profile_id)
    response.write(render_file(os.path.join('templates', 'profile.html'), {'user':user[userID]}))

@login_required  
def own_profile_handler(response):
    #redirect to user's own profile page
    userID = get_cookie(response)
    profile_handler(response, userID)


@login_required
def edit_profile_handler(response, id):
    #edit profile with given id
    response.write('edit profile {}'.format(id))

@login_required
def create_profile_handler(response):
    #signup page
    response.write(render_file(os.path.join('templates', 'create.html'), {}))

@login_required
def all_post_handler(response):
    #display all posts
    #posts = Post.get10() function does not exist yet
    posts = Post.get_all_posts()
    for post in posts:
        #response.write(post.get_message())
        #response.write(str(post.get_author_id()) + '<br>')
        pass

    #response.write(render_file(os.path.join('templates', 'viewpost.html'), Post.get_all_posts()))
    response.write(render_file(os.path.join('templates', 'viewpost.html'), {}))

    '''
        userID = get_cookie(response)
    if userID:
        for individualPost in post:
            #pass in post list to template
            #response.write(post[individualPost].get_message() + '<br>')
            #userName = User.get_user(post.author_id).fname
            #response.write('by' + userName + '<br>')
            response.write('all posts')
            ######response.write(render_file(os.path.join('templates', 'viewposts.html'), {'user':user[userID}))#######
            
    else:
        response.redirect('/')
        '''

@login_required
def new_post_handler(response):
    #new post page
    response.write(render_file(os.path.join('templates', 'addpost.html'), {}))

def about_handler(response):
    #about page
    response.write(render_file(os.path.join('templates', 'about.html'), {'user':user[userID]}))

def styleguide_handler(response):
    #about page
    #Needs "about.html" file to be made
    response.write(render_file(os.path.join('templates', 'styleguide.html'), {}))

def default_handler(response, method, *args, **kwargs):
    #default 404
    return return_404(response)

port = os.getenv('PORT')
if port:
  server = Server(port=int(port))
else:
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
server.register(r'/styleguide', styleguide_handler, url_name = 'styleguide')
server.register(r'/send-to', send_to_handler, url_name = 'send-to')
server.set_default_handler(default_handler)

server.run()
