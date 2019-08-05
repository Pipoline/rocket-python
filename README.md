#### RocketChat API

Python API wrapper for the [Rocket chat API](https://rocket.chat/docs/developer-guides/rest-api)

[Documentation](http://docs.rocket-python.com)

![PyPI - Downloads](https://img.shields.io/pypi/dm/rocket-python)

#### Install

    pip install rocket-python

#### Usage

Initialize the client with a username and password.  This user *must* have Admin privs::

    from rocketchat.api import RocketChatAPI

    api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
                                  'domain': 'https://myrockethchatdomain.com'})

##### Available Calls
    api.send_message('message', 'room_id')
    
    api.get_private_rooms()
    
    api.get_private_room_history('room_id', oldest=date)
    
    api.get_public_rooms()
    
    api.get_room_info('room_id')
    
    api.get_private_room_info('room_id')
    
    api.get_room_history('room_id')
    
    api.create_public_room('room_name', 
                            members=[], 
                            read_only=False)
    
    api.delete_public_room('room_id')
    
    api.get_my_info()
    
    api.get_users()
    
    api.get_user_info('user_id')
    
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
    
    api.upload_file(room_id='room_id',
                    file='file',
                    description='File description',
                    message='Example message')

check /rocketchat/calls/api.py for more.

#### Running Tests

    py.test tests rocketchat

##### Sending a message

You'll first need to get the _id of the room you want to send a message to.  Currently, Rocket
can only send messages to *public* rooms.

    api.send_message('Your message', room_id)
