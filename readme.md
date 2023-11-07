# Capstone Flask Server

### Remember to make the environment variable to production while deploying

# Deployment Configuration
In this flask application `app/config.py` file defines three different deployment configuration.
* Production
* Development
* Testing

These configuration are directly effected by environment variables set. To change configuration we can use `os.environ['FLASK_ENV']` in run.py file. This variable can be set to `development`, `testing` and `production`. The configuration for individual deployment is set in `app/config.py` file which consist of extra details related to individual configuration. 

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
