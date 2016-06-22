#### RocketChat API

Python API wrapper for the [Rocket chat API](https://rocket.chat/docs/developer-guides/rest-api/)

#### Install

    pip install rocket-python

#### Usage

Initialize the client with a username and password.  This user *must* have Admin privs::

    from rocketchat.api import RocketChatAPI
    
    api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
                                  'domain': 'https://myrockethchatdomain.com'})

#### Supported Calls

Only a few calls exist within the API, and I am only adding them as they are needed by 
users.  If you need a call, open an issue or send a pull request.

##### Sending a message

You'll first need to get the _id of the room you want to send a message to.  Currently, Rocket
can only send messages to *public* rooms.

    api.send_message('Your message', room_id)

