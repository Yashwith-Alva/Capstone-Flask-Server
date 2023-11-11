# Capstone Flask Server

> [!WARNING]
> Remember to make the environment variable to production while deploying

> [!IMPORTANT]
> No Auth, Yet to implement

# Deployment Configuration
In this flask application `app/config.py` file defines three different deployment configuration.
* Production
* Development
* Testing

These configuration are directly effected by environment variables set. To change configuration we can use `os.environ['FLASK_ENV']` in run.py file. This variable can be set to `development`, `testing` and `production`. The configuration for individual deployment is set in `app/config.py` file which consist of extra details related to individual configuration. 

# Architectural Pattern
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

> [!IMPORTANT]
> In the below endpoints wherever '<>' is present, substitute it with the necessary values.

## Restaurant

1. [GET] Fetch all restaurants `/restaurant`
2. [POST] Create restaurant `/restaurant` \
    <sub>*JSON FORMAT for creating restaurant*</sub>
    ```
    {
        "resName": "<restaurant_name>",
        "about": "<restaurant_description>",
        "qr": "<generated_qr_code>",
        "address": "<city>",
        "locationLink": "<maps_link>"
    }
    ```
3. [GET] Fetch restaurant by id `/restaurant/<int:id>`
4. [GET] Fetch restaurant by qr `/restaurant/qrcode/<string:qr>`\
5. *TODO* [POST] Update restaurant by id
    ```
    Will be adding soon
    ```

## User
1. [POST] Create an User `/user/register`\
    <sub>*JSON format for creating user*</sub>
    ```
    {
        "usrId": "<user_id>",
        "usrpassword": "<user_password>",
        "rid": "<int:restaurant_id>"
    }
    ```

2. [POST] Update the userId `/update/user/userid`\
    <sub>*JSON format for updating userId*</sub>
    ```
    {
        "usrpassword" : <user_password>,
        "rid" : <int:restaurant_id>
    }
    ```

3. [POST] Update the user password `/update/user/password`\
    <sub>*JSON format for updating userId*</sub>
    ```
    {
        "usrId" : <user_id>,
        "rid" : <int:restaurant_id>
    }
    ```

## Menu Items
1. [GET] Get all the items in the table `/restaurant/menu`
2. [POST] Create a new item in the table `/restaurant/menu`\
    <sub>*JSON format for creating a new menu item. itemId, rid and itemName are must*</sub>
    ```
    {
    "itemName" : <item_name>,
    "rid" : <int:restaurant_id>,
    "category" : <category>,
    "ingredient_info" : <ingredient_info>
    }
    ```
3. [GET] Get menu by restaurant id `/restaurant/menu/<int:restaurant_id>`
4. [POST] Update menu item\
    <sub>*JSON format for updating menu item. ItemId and rid are must. If any other feild not given, it will update mysql to None*</sub>
    ```
    {
    "itemId" : <int:item_id>,
    "itemName" : <item_name>,
    "category" : <category>,
    "ingredient_info" : <ingredient_info>,
    "rid" : <int:restaurant_id>
    }
    ```

## Nutrition
1. [GET] Fetch all the nutrition items `/restaurant/menu/nutrition`
2. [POST] Create a new nutrition item `/restaurant/menu/nutrition`\
    <sub>*JSON format for creating a nutrition item. foodType is case sensitive*</sub>
    ```
    {
    "itemId" : <int:item_id>,
    "energy" : <int>,
    "protein" : <int>,
    "carbohydrate" : <int>,
    "fat" : <int>,
    "foodType" : <"VEG"/"NON-VEG">
    }
    ```
3. [GET] Fetch nutrition by itemId `/restaurant/menu/nutrition/<int:item_id>`
4. [POST] Update nutrition by itemId `/update/restaurant/menu/nutrition `\
    <sub>*JSON format for creating a updating nutrition values*</sub>
    ```
    {
    "itemId" : <int:itemId>,
    "energy" : <int>,
    "protein" : <int>,
    "carbohydrate" : <int>,
    "fat" : <int>
    }
    ```

# RESOURCES
- It includes MySQL database used in the project. It can be directly exported into the mysql workbench.
* It also includes various testcases that was run in thunderclient.
* You can import the JSON file directly to the thunderclient application.