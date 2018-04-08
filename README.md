# Bucketlist
This is an API for a buckelist using flask.
A bucketlist is a list of all the goals you want to achieve,dreams you want to fulfill and
life experiences you desire to experience before you die (or hit the bucket). 
The API shall therefore have the ability to:

    1. Create a bucketlist (by giving it a name/title)
    2. Retrieve an existing bucketlist
    3. Update it (by changing it's name/title)
    4. Delete an existing bucketlist

## TECHNOLOGIES USED
    1. Python 3
    2. Flask
    3. Postgresql
    4. Dependencies provided in requirements.txt
 
## INSTRUCTONS
* ## Clone this repo
    ```
    git clone https://jmutuku95@bitbucket.org/jmutuku95/bucketlist.git
    ```
    cd to the cloned folder
    
1. Create virtual environmnet and install all requirements in requirements.txt
    ```
    $ virtualenv -p python3 venv
    (venv)$ pip install -r requirements.txt
    ```

2. Set up database and ensure it's running on port 5432
   in psql
   ```
   postgres=# CREATE DATABASE flask_api;
   postgres=# CREATE DATABASE testdb;
   ```

3. Set up environment variables
    NB:edit DATABASE_URL in env.bat, .env and instance/config.py to reflect
       your database url
       ## Manually
        ```
            ../venv/Scripts/activate
            export FLASK_APP=run.py
            export SECRET=some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING
            export APP_SETTINGS=development
            export DATABASE_URL=postgresql://localhost/flask_api
        ```

On windows:
    Navigate to project folder using CLI and run 'env.bat' to set environment variables
    ```
    \bucketlist>env.bat
    ```

On UNIX based os, from project folder run 
    ```
    $ source .env
    ```


4. Ensure all tests are working
    ```
    python manage.py test
    ```

5. Run 
    ```
    flask run
    ``` 
    to test the app in 'development' setting. 
    To change the environment to either 'staging' or 'production' set environment variable 'APP_SETTINGS'
    to either 'staging' or 'production' respectively.
    ```
    export APP_SETTINGS=staging
    ```
    or 
    ```
    export APP_SETTINGS=production
    ```
    

## API Resources
  '\auth\register\'   POST    - to register new user, requires email and password arguments
  '\auth\login\'      POST    - to login existing user, requires email and password
  '\bucketlists\'     GET     - gets all bucketlists for user
  '\bucketlists\{id}' GET/PUT/DELETE - gets a specific bucketlist using it's 'id' either for viewing,
                                editing or deleting depending on HTTP verb used

