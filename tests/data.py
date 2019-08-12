PUBLIC_ROOM_TEST = {'channels': [
    {'name': 'Test Room',
     '_id': '123456'}
]}

GET_ROOM_INFO_TEST = {
  "channel": {
    "_id": "ByehQjC44FwMeiLbX",
    "ts": "2016-11-30T21:23:04.737Z",
    "t": "c",
    "name": "testing",
    "usernames": [
      "testing",
      "testing1",
      "testing2"
    ],
    "msgs": 1,
    "default": 'true',
    "_updatedAt": "2016-12-09T12:50:51.575Z",
    "lm": "2016-12-09T12:50:51.555Z"
  },
  "success": 'true'
}

GET_ME_TEST = {
  "_id": "aobEdbYhXfu5hkeqG",
  "name": "Example User",
  "emails": [
    {
      "address": "example@example.com",
      "verified": 'true'
    }
  ],
  "status": "offline",
  "statusConnection": "offline",
  "username": "example",
  "utcOffset": 0,
  "active": 'true',
  "success": 'true'
}

GET_USERS_TEST = {
  "users": [
    {
      "_id": "nSYqWzZ4GsKTX4dyK",
      "createdAt": "2016-12-07T15:47:46.861Z",
      "services": {
        "password": {
          "bcrypt": "..."
        },
        "email": {
          "verificationTokens": [
            {
              "token": "...",
              "address": "example@example.com",
              "when": "2016-12-07T15:47:46.930Z"
            }
          ]
        },
        "resume": {
          "loginTokens": [
            {
              "when": "2016-12-07T15:47:47.334Z",
              "hashedToken": "..."
            }
          ]
        }
      },
      "emails": [
        {
          "address": "example@example.com",
          "verified": 'true'
        }
      ],
      "type": "user",
      "status": "offline",
      "active": 'true',
      "roles": [
        "user"
      ],
      "name": "Example User",
      "lastLogin": "2016-12-08T00:22:15.167Z",
      "statusConnection": "offline",
      "utcOffset": 0,
      "username": "example"
    }
  ],
  "count": 3,
  "offset": 2,
  "total": 10,
  "success": 'true'
}

GET_USER_INFO_TEST = {
  "user": {
    "_id": "nSYqWzZ4GsKTX4dyK",
    "createdAt": "2016-12-07T15:47:46.861Z",
    "services": {
      "password": {
        "bcrypt": "..."
      },
      "email": {
        "verificationTokens": [
          {
            "token": "...",
            "address": "example@example.com",
            "when": "2016-12-07T15:47:46.930Z"
          }
        ]
      },
      "resume": {
        "loginTokens": [
          {
            "when": "2016-12-07T15:47:47.334Z",
            "hashedToken": "..."
          }
        ]
      }
    },
    "emails": [
      {
        "address": "example@example.com",
        "verified": 'true'
      }
    ],
    "type": "user",
    "status": "offline",
    "active": 'true',
    "roles": [
      "user"
    ],
    "name": "Example User",
    "lastLogin": "2016-12-08T00:22:15.167Z",
    "statusConnection": "offline",
    "utcOffset": 0,
    "username": "example"
  },
  "success": 'true'
}

UPLOAD_FILE_TEST = {
   "success": "true"
}

SET_ROOM_TOPIC_TEST = {
  "topic": "test topic",
  "success": 'true'
}
