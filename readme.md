# Capstone Flask Server

### Remember to make the environment variable to production while deploying

# Deployment Configuration
In this flask application `app/config.py` file defines three different deployment configuration.
* Production
* Development
* Testing

These configuration are directly effected by environment variables set. To change configuration we can use `os.environ['FLASK_ENV']` in run.py file. This variable can be set to `development`, `testing` and `production`. The configuration for individual deployment is set in `app/config.py` file which consist of extra details related to individual configuration. 

# Usage or Expand
This project follows a MVC like architecture where we have `Model`, `Controller` and `Service`. This is a headless program hence no need for views. 
* `Model` classes are replica of database table and are used for storing incoming requests on specific table.
* `Controller` classes are used for fetching the requests from the routes and formatting them before sending them to the service.
* `Service` classes are the only ones that interact with the database and does all the CRUD operations.
This way of coding helps to keep the code modular and easy to tweak. So any changes that needs to be made can simply be made by adding a few methods or classes to one of the files.
* `routes.py` is the routing file. This file consist of all the `API Endpoints`. Routes transfer the request that are sent to them to the controller. And controller then sends it to the service.
\
You can also make use of `makeResponse` which is a method described in `app/utils/responseHandler` package. This provides a handy way to create JSON responses that are need to be sent to the client.

# Available API's
In development mode the server is running at port 5000 in localhost. Hence, all API starts with `http://localhost::5000/`

## Restaurant
1. [GET] Fetch all restaurants `/restaurant`
2. [GET] Fetch restaurant by id `/restaurant/{id}`
3. [GET] Fetch restaurant by qr `/restaurant/qrcode/{qr}`
4. [POST] Create restaurant `/restaurant/register` \
    *JSON FORMAT for creating restaurant*
    ```
    {
        "resName": "<restaurant_name>",
        "about": "<restaurant_description>",
        "qr": "<generated_qr_code>",
        "address": "<city>",
        "locationLink": "<maps_link>"
    }
    ```

## User
1. [POST] Create an User `/user/register`
    *JSON format for creating user*
    ```
    {
        "usrId": "<user_id>",
        "usrpassword": "<user_password>",
        "rid": "<restaurant_id>"
    }
    ```
