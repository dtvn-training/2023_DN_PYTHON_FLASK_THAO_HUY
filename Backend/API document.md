# API Documentation

## Introduction

> This is an API document for Frontend understand more about Endpoint - Request - Response - Error Handling…

## Login

- ### **[POST]/api/login**

  > - Summary: Login
  > - Header (Content-Type): application/json
  > - **RefreshToken PAYLOAD:**

  ```
  Payload = {
    "user_id": user_id,
    "role_id": role_id
  }
  ```

  - ### **Request Body:**

  ```
  {
    "email": "string",
    "password": "string"
  }
  ```

  - ### **Responses:**

  ```
  Cookies:
  {
    'RefreshToken': refresh_token
  }
  ```

  ```
  Message:
  '200' = {
  	'msg': 'Đăng nhập thành công!'
  }

  '401' = {
  	  'msg' = {
  		'Null': 'Vui lòng điền email/mật khẩu!',
  		'Email': 'Email không tồn tại!',
  		'Password': 'Sai mật khẩu!'
  	  }
  }
  ```

  - ### **Error Handling:**

  ```
  The API handles errors by returning appropriate status codes and error messages.
  Possible error responses include:
  {
  	'500': 'Unexpected Error'
  	'404': 'Page Not Found'
  	'401': 'Unauthorized'
  }
  ```

  ## Get Access Token

- ### **[POST]/api/refresh_token**

  > - Summary: Transmit payload from RefreshToken to AccessToken
  > - Header (Authorization): RefreshToken

  - ### **Authorization HEADER:**

  ```
  {
  'Authorization': 'Refresh token'
  }
  ```

  - ### **Request BODY:**

  ```
  {
    "email": "string",
    "password": "string"
  }
  ```

  - ### **Responses:**

  ```
  {
  	'AccessToken': 'Access_token'
  }
  ```

  - ### **Error Handling:**

  ```
  {
  	'401' = {
  	   'msg':{
  			'InvalidTokenError': 'Invalid token!',
  			'DecodeError': 'Token failed validation!',
  			'InvalidSignatureError': 'Invalid refresh token!',
  			'ExpiredSignatureError': 'The RF token is expired!',
  	    }
  	 }

  	'404' = {
  			'msg': 'Page not found!'
       }
  	'500' = {
  			'msg': 'Unexpected error!'
       }
  }
  ```

  ## Logout

- ### **[GET]/api/logout**

  > - Summary: Delete refresh token in Cookies at Endpoint = ‘/api/refresh_token’
  > - Header (Authorization): None

  - ### **Request BODY:**

  ```
  {
    null
  }
  ```

  - ### **Responses:**

  ```
  {
    'RefreshToken': null
    '200' = {
  		'msg': 'Đăng xuất thành công!'
    }
  }
  ```

  - ### **Error Handling:**

  ```
  {
  '500' = {
  		'msg': 'Unexpected error!'
    }
  }
  ```

  ## User management

  ## Get user

- ### **[GET]/api/user_info**
  > - Summary: Get user informations
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token'
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    "user_id",
    "email",
    "first_name",
    "last_name",
    "image",
    "address",
    "phone",
    "avatar",
    "role_id",
    "create_at",
    "update_at"
  }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected error!'
    }
  }
  ```
- ## Get all users
- ### **[GET]/api/all_user_info**

  > - Summary: Get all user informations
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: Admin

  - ### **Request HEADER:**

  ```
  {
    'Authorization': 'Access Token'
  }
  ```

  - ### **Responses:**

  ```
  '200' = {
    msg: [
        user1 = {
            "user_id",
            "email",
            "first_name",
            "last_name",
            "image",
            "address",
            "phone",
            "avatar",
            "role_id",
            "create_at",
            "update_at"
        },
        user2 = {
            "user_id",
            "email",
            "first_name",
            "last_name",
            "image",
            "address",
            "phone",
            "avatar",
            "role_id",
            "create_at",
            "update_at"
        },
        ...]

  }
  ```

  - ### **Error Handling:**

  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Admin resources access denied!'
    }
  }
  ```

- ## Delete user
- ### **[GET]/api/delete_user**
  > - Summary: Delete user by ID
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: Admin
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token'
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Delete User successfully!"
  }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
- ## Delete all user
- ### **[GET]/api/delete_all_user**
  > - Summary: Delete all users
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: Admin
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token'
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Delete all users successfully!"
  }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
- ## Update user
- ### **[GET]/api/update_user**
  > - Summary: Update user by ID
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
    {
        "email",
        "first_name",
        "last_name",
        "role_id",
        "address",
        "phone"
    }
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Update user successfully!"
  }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```



  ## Campaign 

  ## Get campaign

- ### **[GET]/api/campaign/<_camp_id>**
  > - Summary: Get campaign informations
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token'
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    "user_id",
    "name",
    "user_status",
    "budget",
    "bid_amount",
    "start_date",
    "end_date",
    "usage_rate",
    "campaign_id",
    "create_at",
    "update_at"
  }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '404' = {
  		'msg': 'Campaign not found!'
    }
  '500' = {
  		'msg': 'Unexpected error!'
    }
  }
  ```

 - ### **Example:**
 ```
 URL : {{domain}}/api/campaign/6f0caf18-5dcc-4f95-ace3-381536a2bdad
 Reponse :
 {
    "bid_amount": 0,
    "budget": 1000,
    "campaign_id": "6f0caf18-5dcc-4f95-ace3-381536a2bdad",
    "create_at": "Fri, 01 Dec 2023 10:04:19 GMT",
    "end_date": "Fri, 05 May 2023 23:59:59 GMT",
    "name": "abcd123",
    "start_date": "Sun, 01 Jan 2023 23:59:59 GMT",
    "update_at": "Fri, 01 Dec 2023 10:04:19 GMT",
    "usage_rate": 0.0,
    "used_amount": 0,
    "user_id": "6cd11s58-f613-47",
    "user_status": true
}
 ```


- ## Get all campaigns
- ### **[GET]/api/all_campaign**

  > - Summary: Get all campaign informations
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: Admin, User

  - ### **Request HEADER:**

  ```
  {
    'Authorization': 'Access Token'
  }
  ```

  - ### **Responses:**

  ```
  '200' = {
    msg: [
        campaign1 = {
            "user_id",
            "name",
            "user_status",
            "budget",
            "bid_amount",
            "start_date",
            "end_date",
            "usage_rate",
            "campaign_id",
            "create_at",
            "update_at"
        },
        campaign2 = {
            "user_id",
            "name",
            "user_status",
            "budget",
            "bid_amount",
            "start_date",
            "end_date",
            "usage_rate",
            "campaign_id",
            "create_at",
            "update_at"
        },
        ...]

  }
  ```

  - ### **Error Handling:**

  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
    }
  '404' = {
  		'msg': 'Campaign not found!'
    }
  '500' = {
  		'msg': 'Admin resources access denied!'
    }
  }
  ```


 - ### **Example:**
 ```
 URL : {{domain}}/api/all_campaign
 Reponse :
  {
    "campaigns": [
        {
            "bid_amount": 0,
            "budget": 100,
            "campaign_id": "123",
            "create_at": null,
            "end_date": "Tue, 26 Dec 2023 23:59:59 GMT",
            "name": "abc",
            "start_date": "Thu, 23 Nov 2023 23:59:59 GMT",
            "update_at": null,
            "usage_rate": 10.0,
            "user_id": "6cd11s58-f613-47",
            "user_status": true
        },
        {
            "bid_amount": 0,
            "budget": 100,
            "campaign_id": "324e144e-9686-42",
            "create_at": null,
            "end_date": "Mon, 25 Dec 2023 23:59:59 GMT",
            "name": "abc",
            "start_date": "Sat, 25 Nov 2023 23:59:59 GMT",
            "update_at": null,
            "usage_rate": 10.0,
            "user_id": "6cd11s58-f613-47",
            "user_status": true
        }
    ]
}

 ```


- ## Delete campaign
- ### **[DELETE]/api/delete_campaign<camp_id>**
  > - Summary: Delete Campaign by ID
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: Admin, User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token'
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Delete Campaign successfully!"
  }
  '400' = {
  		'msg': 'Delete Campaign failed!'
  }
  '404' = {
  		'msg': 'Invalid campaign ID'
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Delete Campaign failed!'
    }
  '404' = {
  		'msg': 'Invalid campaign ID'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```

  - ### **Example:**
 ```
 URL :  {{domain}}/api/delete_campaign/324e144e-9686-42
 Reponse :
  {
    "msg": "Delete Campaign successfully!",
    "payload": null,
    "status_code": 200
  }

```


- ## Update campaign
- ### **[PUT]/api/update_campaign/<camp_id>**
  > - Summary: Update campaign 
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Update campaign successfully!"
  }
  '400' = {
  		'msg': 'Invalid date',
      'msg': 'Invalid name. Please re-enter',
      'msg': 'Invalid title. Please re-enter',
      'msg': 'Invalid. Please re-enter',
      'msg': 'Update campaign failed!',
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
      'msg': 'Invalid date',
      'msg': 'Invalid name. Please re-enter',
      'msg': 'Invalid title. Please re-enter',
      'msg': 'Invalid. Please re-enter',
      'msg': 'Update campaign failed!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```

  - ### **Example:**
 ```
 URL :  {{domain}}/api/update_campaign
 Body : 
 {
    "campaign_id": "324e144e-9686-42",
    "name" : "abcd1234567",
    "user_id": "6cd11s58-f613-47",
    "bid_amount": "0",
    "budget": "1000",
    "start_date" : "2023-11-23 23:59:59",
    "end_date" : "2023-11-27 23:59:59",
    "user_status": "2",
    "title": "haizzz",
    "description": "help me",
    "img_preview": "hrhshseh",
    "final_url": "tjthhh"
  }
 Reponse :
  {
    "msg": "Update Campaign successfully!",
    "payload": null,
    "status_code": 200
  }

```



- ## Create campaign
- ### **[POST]/api/add_campaign**
  > - Summary: Update campaign 
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User, Admin
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Add campaign successfully!"
  }
  '400' = {
  		'msg': 'Invalid date',
      'msg': 'Invalid name. Please re-enter',
      'msg': 'Invalid title. Please re-enter',
      'msg': 'Invalid. Please re-enter',
      'msg': 'Add campaign failed!'
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
      'msg': 'Invalid date',
      'msg': 'Invalid name. Please re-enter',
      'msg': 'Invalid title. Please re-enter',
      'msg': 'Invalid. Please re-enter',
      'msg': 'Add campaign failed!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
  - ### **Example:**
 ```
 URL :  {{domain}}/api/add_campaign
 Body :
 {
    "name" : "abcd123",
    "user_id": "6cd11s58-f613-47",
    "bid_amount": "0",
    "budget": "1000",
    "start_date" : "2023-01-01 23:59:59",
    "end_date" : "2023-05-05 23:59:59",
    "user_status": true,
    "title": "help",
    "description": "help me",
    "img_preview": "afhbfd",
    "final_url": "tjthhh"
}

 Reponse :
  {
    "msg": "Add Campaign successfully!",
    "payload": null,
    "status_code": 200
}

```

- ## Search campaign 
- ### **[POST]/api/campaign/search**
  > - Summary:  Search campaign by name
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Search campaign successfully!"
  }
  '400' = {
  		'msg': 'Search campaign failed!',
      'msg': 'Invalid date'
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '400' = {
  		'msg': 'Invalid Authentication!'
      'msg': 'Search campaign failed!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
  - ### **Example:**
 ```
 URL :  {{domain}}/api/campaign/search
 Body :
{
    "name" : "abcd123",
    "user_id": "6cd11s58-f613-47",
    "start_date" : "2023-01-01 23:59:59",
    "end_date" : "2023-05-05 23:59:59"
}


 Reponse :
  {
    "msg": "Search campaign successfully!",
    "payload": null,
    "status_code": 200
}

```

- ## Banner campaign 
- ### **[POST]/api/banner_campaign/<camp_id>**
  > - Summary:  Search campaign by name
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User, Admin
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    msg: "Update campaign successfully!"
  }
  '404' = {
      'msg': 'Invalid campaign ID'
    }
  '400' = {
  		'msg': 'Update campaign failed!',
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '404' = {
      'msg': 'Invalid campaign ID'
    }
  '400' = {
  		'msg': 'Update campaign failed!',
      'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
  - ### **Example:**
 ```
 URL :  {{domain}}/api/banner_campaign/7
 Body :
{
    "budget" : "2000",
    "end_date" : "2023-05-05 23:59:59",
    "bid_amount": "900",
    "user_status": true
}

 Reponse :
 {
    "msg": "Update banner successfully!",
    "payload": null,
    "status_code": 200
}

```

- ## Get Banner campaign 
- ### **[POST]/api/get_banner_campaign**
  > - Summary:  Get banner by status, bid_amount
  > - Header (Authorization): AccessToken[Payload]
  > - Accessible: User, Admin
  - ### **Request HEADER:**
  ```
  {
    'Authorization': 'Access Token',
  }
  ```
  - ### **Responses:**
  ```
  '200' = {
    "name",
    "user_status",
    "bid_amount",
    "campaign_id"
  }
  '404' = {
      'msg': 'Campaign not found'
    }
  ```
  - ### **Error Handling:**
  ```
  {
  '404' = {
      'msg': 'Invalid campaign ID'
      'msg': 'Campaign not found'
    }
  '400' = {
      'msg': 'Invalid Authentication!'
    }
  '500' = {
  		'msg': 'Unexpected Error!'
    }
  }
  ```
  - ### **Example:**
 ```
 URL :  {{domain}}/api/get_banner_campaign
 Reponse :
 {
    "campaigns": [
        {
            "bid_amount": 1000,
            "campaign_id": 3,
            "name": "abc",
            "user_status": true
        },
        {
            "bid_amount": 500,
            "campaign_id": 5,
            "name": "abc",
            "user_status": true
        },
        {
            "bid_amount": 100,
            "campaign_id": 4,
            "name": "abc",
            "user_status": true
        }
    ]
}

```