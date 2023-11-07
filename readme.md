# Capstone Flask Server

### Remember to make the environment variable to production while deploying

# Available API's
All API start with `http://localhost::5000/`

## Restaurant
1. [GET] Fetch all restaurants `/restaurant`
2. [GET] Fetch restaurant by id `/restaurant/{id}`
3. [GET] Fetch restaurant by qr `/restaurant/qrcode/{qr}`
4. [POST] Create restaurant `/restaurant/register` \
    JSON FORMAT for creating restaurant
    ```
    {
        "resName": "restaurant name",
        "about": "restaurant description",
        "qr": null,
        "address": "city",
        "locationLink": "Maps link"
    }
    ```


## Flask Integration with the Server