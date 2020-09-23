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

CREATE_IM_ROOM_TEST = {
    "room": {
        "_id": "Lymsiu4Mn6xjTAan4RtMDEYc28fQ5aHpf4",
        "_updatedAt": "2018-03-26T19:11:50.711Z",
        "t": "d",
        "msgs": 0,
        "ts": "2018-03-26T19:11:50.711Z",
        "meta": {
            "revision": 0,
            "created": 1522094603745,
            "version": 0
        },
        "$loki": 65,
        "usernames": [
            "chat.user",
            "something"
        ]
    },
    "success": True
}

GET_IM_ROOMS_TEST = {
    "ims": [
        {
            "_id": "ew28FnZqipDpvKw3Rrocket.cat",
            "_updatedAt": "2018-02-23T17:58:56.147Z",
            "t": "d",
            "msgs": 22,
            "ts": "2018-02-18T19:51:52.557Z",
            "lm": "2018-02-23T17:58:56.136Z",
            "topic": "a direct message with rocket.cat"
        },
        {
            "_id": "RtycPC29hqLJfT9xjew28FnZqipDpvKw3R",
            "_updatedAt": "2018-02-23T18:14:03.510Z",
            "t": "d",
            "msgs": 2,
            "ts": "2018-02-21T21:08:51.026Z",
            "lm": "2018-02-23T18:14:03.490Z",
            "usernames": ["something", "chat.user"],
        },
        {
            "_id": "ew28FnZqipDpvKw3Rf2CAhYGtjS9iNZ7nd",
            "_updatedAt": "2018-02-23T17:45:56.496Z",
            "t": "d",
            "msgs": 1,
            "ts": "2018-02-23T17:32:28.016Z",
            "lm": "2018-02-23T17:45:56.475Z",
            "usernames": ["chat.user2", "something"],
        }
    ],
    "offset": 0,
    "count": 3,
    "total": 3,
    "success": True
}

GET_IM_HISTORY_TEST = {
  "messages": [
    {
      "_id": "AkzpHAvZpdnuchw2a",
      "rid": "ByehQjC44FwMeiLbX",
      "msg": "hi",
      "ts": "2016-12-09T12:50:51.555Z",
      "u": {
        "_id": "y65tAmHs93aDChMWu",
        "username": "testing"
      },
      "_updatedAt": "2016-12-09T12:50:51.562Z"
    },
    {
      "_id": "vkLMxcctR4MuTxreF",
      "t": "uj",
      "rid": "ByehQjC44FwMeiLbX",
      "ts": "2016-12-08T15:41:37.730Z",
      "msg": "testing2",
      "u": {
        "_id": "bRtgdhzM6PD9F8pSx",
        "username": "testing2"
      },
      "groupable": False,
      "_updatedAt": "2016-12-08T16:03:25.235Z"
    },
    {
      "_id": "bfRW658nEyEBg75rc",
      "t": "uj",
      "rid": "ByehQjC44FwMeiLbX",
      "ts": "2016-12-07T15:47:49.099Z",
      "msg": "testing",
      "u": {
        "_id": "nSYqWzZ4GsKTX4dyK",
        "username": "testing1"
      },
      "groupable": False,
      "_updatedAt": "2016-12-07T15:47:49.099Z"
    },
    {
      "_id": "pbuFiGadhRZTKouhB",
      "t": "uj",
      "rid": "ByehQjC44FwMeiLbX",
      "ts": "2016-12-06T17:57:38.635Z",
      "msg": "testing",
      "u": {
        "_id": "y65tAmHs93aDChMWu",
        "username": "testing"
      },
      "groupable": False,
      "_updatedAt": "2016-12-06T17:57:38.635Z"
    }
  ],
  "success": True
}

LOGOUT_TEST = {
   "status": "success",
   "data": {
     "message": "You've been logged out!"
   }
}
