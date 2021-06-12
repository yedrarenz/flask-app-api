# flask-app-api
Sample project with Python (Flask, SQLAlchemy, REST)

Sample URLs

# Get Users
Request URL: http://localhost:5000/api/v1.0/users

Request Type: <b>Get</b>

# Get User by ID
Request URL: http://localhost:5000/api/v1.0/user/id/1

Request Type: <b>Get</b>

# Adding User
Request URL: http://localhost:5000/api/v1.0/user

Request Type: <b>Post</b>

Content:
```
{
    "name" : "Ian Alinso",
    "team" : "Teamba"
}
```

# Updating User Information
Request URL: http://localhost:5000/api/v1.0/user

Request Type: <b>Put<b>

Content:
```
{
    "name" : "Ian Alinso",
    "team" : "Teamba"
}
```