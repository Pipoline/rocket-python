#### RocketChat API

Python API wrapper for the [Rocket chat API](https://rocket.chat/docs/developer-guides/rest-api)

[Documentation](http://docs.rocket-python.com)

![Travis (.org)](https://img.shields.io/travis/Pipoline/rocket-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/rocket-python)
![PyPI](https://img.shields.io/pypi/v/rocket-python)
![Codecov](https://img.shields.io/codecov/c/github/Pipoline/rocket-python)

#### Install

    pip install rocket-python

#### Usage

Initialize the client with a username and password or token and user_id.
This user *must* have Admin privs:

    from rocketchat.api import RocketChatAPI

    api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
                                  'domain': 'https://myrocketchatdomain.com'})
    # or
    api = RocketChatAPI(settings={'token': 'sometoken', 'user_id': 'someuserid',
                                  'domain': 'https://myrocketchatdomain.com'})

##### Available Calls

###### Messages / Rooms general functions
    api.send_message('message', 'room_id')
    
    api.upload_file(room_id='room_id',
                    file='file',
                    description='File description',
                    message='Example message')
    
    api.upload_remote_file(room_id='room_id',
                    url='url',
                    description='File description',
                    message='Example message')
    
###### Users
    api.create_user('email', 
                    'name', 
                    'password', 
                    'username', 
                     active=True, 
                     roles=['user'], 
                     join_default_channels=True, 
                     require_password_change=False, 
                     send_welcome_email=False, 
                     verified=False, 
                     customFields=None)
                    
    api.delete_user('user_id')
    
    api.get_user_id('user_name')
    
    api.get_users()
    
    api.get_user_info('user_id')
    
    api.get_my_info()

###### Direct Messages
    api.create_im_room('username')
    
    api.close_room('room_id')
    
    api.open_room('room_id')
    
    api.get_im_room_history('room_id', oldest=date)
    
    api.get_im_rooms()

###### Groups / Private Rooms
    api.create_private_room('room_name', 
                            members=[], 
                            read_only=False)
    
    api.invite_private_room('room_id', 'user_id')
    
    api.get_private_rooms()
    
    api.get_private_room_history('room_id', oldest=date)
    
    api.get_room_id('room_name')
    
    api.get_private_room_info('room_id')
    
    api.set_room_topic('topic', 'room_id')

###### Channels / Public Rooms
    api.get_public_rooms()
    
    api.create_public_room('room_name', 
                            members=[], 
                            read_only=False)
    
    api.invite_public_room('room_id', 'user_id')
    
    api.get_room_info('room_id')
    
    api.get_public_room_id('room_name')
    
    api.get_room_history('room_id')
    
    api.delete_public_room('room_id')
    

check /rocketchat/calls/api.py for more.

#### Running Tests

    py.test tests rocketchat

##### Sending a message

You'll first need to get the _id of the room you want to send a message to.  Currently, Rocket
can only send messages to *public* rooms.

    api.send_message('Your message', room_id)
