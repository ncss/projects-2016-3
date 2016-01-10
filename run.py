#!/usr/bin/env python3
from tornado.ncss import Server
import pprint
from engine import render_file, ParseError

#user has id, email, fname, lname, location, password
#post has id, userid, message, status, timestamp
#status is 0-2
#skill has skill id, skill name, category id, rank, 
#skill categories - 1=medicine, 2=engineering, currently ranked 1-10
users = {1:{'id': 1, 'email' : 'evan@email.com', 'fname': 'Evan', 'lname': 'Kohilas', 'location': 'Sydney', 'password': 'A1B2'},

        2:{'id': 2, 'email' : 'aleks@email.com', 'fname': 'Aleks', 'lname': 'Bricknell', 'location': 'Mount Gambier', 'password': 'qwerty'},
        3:{'id': 3, 'email' : 'katherine@email.com', 'fname': 'Katherine', 'lname': 'Allen', 'location': 'Sydney', 'password': 'hello1'}
}

posts = {1:{'id': 1, 'userid': 1, 'message' : "I'm ok", 'status': 0},
        2:{'id': 2, 'userid': 1, 'message' : "I'm still ok", 'status': 0},
        3:{'id': 3, 'userid': 2, 'message' : "I'm not ok", 'status': 1},
}

skills = {1:{'id':1, 'skill name': 'first aider', 'category id':1, 'rank':1},
        2:{'id':2, 'skill name': 'emergency doctor', 'category id':1, 'rank':8},
        3:{'id':3, 'skill name': 'structural engineer', 'category id':2, 'rank':6}
        }

def login_handler(response):
    #database password check 
    #assume database stuff worked fine
    email = response.get_field("email")
    password = response.get_field("password")
    loggedIn = False
    for i in users:
        if users[i]['email'] == email:
            if users[i]['password'] == password:
                response.set_secure_cookie("userLoggedIn", str(i))
                loggedIn = True
                break
    if loggedIn:
        response.redirect('/')
    else:
        response.write("wrong login")
    

def unknown_handler(response, error):
	response.write('404<br>{}'.format(error))

def home_handler(response):
	#see if authorised or unauthorised
    #display either home page
    #login(response, '2')
    response.write(str(response.get_secure_cookie("userLoggedIn")))
    userLoggedIn = response.get_secure_cookie("userLoggedIn")
    if userLoggedIn:
        response.write(str(userLoggedIn) + 'is logged in')
    else:
        response.write('Not logged in!')


    response.write('Home!')



    '''if not loggedin display log in page
            collect login details
            make cookie with login details

    ''' 
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
    for i in posts:
        response.write(posts[i]['message'] + '<br>')
        userName = user[posts[i]['userid']]['fname']
        response.write('by' + userName + '<br>')
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
server.register(r'/login', login_handler, url_name = 'login')
server.register(r'/search', search_handler, url_name = 'search')
server.register(r'/profile/(\d+)', profile_handler, url_name = 'profile')
server.register(r'/profile', own_profile_handler, url_name = 'own_profile')
server.register(r'/profile/(\d+)/edit', edit_profile_handler, url_name = 'edit_profile')
server.register(r'/profile/create', create_profile_handler, url_name = 'create_profile')
server.register(r'/post/all', all_post_handler, url_name = 'all_post')
server.register(r'/post/create', new_post_handler, url_name = 'create_post')
server.register(r'/about', about_handler, url_name = 'about')


server.run()
