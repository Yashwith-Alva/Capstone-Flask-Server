* Install all the required packages for the project
```
pip install -r requirements.txt
```

* Create a virtual environment. This is necessary to run the app in different configuration
```
python -m venv capstone
```

* Activate the environment
```
capstone\Scripts\activate
```

* In `app/config.py` file there is a list of configuration setup to connect to the database. Change these based on your local mysql database

* The flask app by default will be launched in PORT 5000 on the localhost.
* The flask app is set to run at `development` configuration.
* To change the build configuration, go to run.py and change it to following
    * For `development`: {Runs in debug mode}
    ```
    os.environ['FLASK_ENV'] = 'development'
    ```
    
    * For `testing`:  {It is not setup, will run similar to development mode}
    ```
    os.environ['FLASK_ENV'] = 'testing'
    ```

    * For `production`: {No debugging option}
    ```
    os.environ['FLASK_ENV'] = 'production'
    ```

* To run the app:
    ```
    python run.py
    ```