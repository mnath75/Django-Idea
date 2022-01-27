# Django Idea
The aim for this application is to enable creating and selling courses online.  
For now just user authentication works.

This is server side part created with Django Rest Framework.

## How to run
Install Docker Desktop.  
Then run:
```console
docker compose up
```

### ENV settings
Create .env file with necessary infomation. Check the .env.example for guidance. 

## User authentication
Request authentication is made with json web token passed to the user in http-only cookie.  
Endpoints comes from https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
