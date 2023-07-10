Your mission, should you choose to accept it, involves developing an app, containerize it and set up a CI for it.
Please read carefully all the instructions.

If any of the following steps is not working, it is expected from you to fix them

## Installation

1. Create a virtual environment with `python3 -m venv challenge_venv`
2. Activate it with `source challenge_venv/bin/activate`
3. Install the requirements in this directory `pip install -r requirements.txt`

## Run the app

1. Move to `challenges/flask_container_ci` directory, if you are not already there
1. Run `export FLASK_APP=app/main.py`
1. To run the app execute `flask run`. If it doesn't works, fix it
3. Access `http://127.0.0.1:5000`. You should see the following

```
{
    "current_uri": "/",
    "example": "/matrix/'123n456n789'",
    "resources": {
        "column": "/columns/<matrix>/<column_number>",
        "matrix": "/matrix/<matrix>",
        "row": "/rows/<matrix>/<row_number>"
    }
}
```

4. You should be able to access any of the resources and get the following data:

* /matrix/\<matrix\>

    for example, for /matrix/123n456n789 the user will get:

    1 2 3
    4 5 6
    7 8 9

* /matrix/\<matrix\>/\<column_number\> 

    for example, for /matrix/123n456n789/2 the user will get:

    2
    5
    8

* /matrix/\<matrix\>/\<row_number\> 

    for example, for /matrix/123n456n789/1 the user will get:

    1 2 3 

## Containers

Using Docker or Podman, containerize the flask app so users can run the following two commands:

```
docker build -t app:latest /path/to/Dockerfile
docker run -d -p 5000:5000 app
```

1. You can use any image base you would like
2. Containerize only what you need for running the application, nothing else.

## CI

Great, now that we have a working app and also can run it in a container, let's set up a CI for it so it won't break again in the future
In current directory you have a file called tests.py which includes the tests for the app. What is required from you, is:

1. Write a CI pipeline that will run the app tests. You are free to choose whatever CI system or service you prefer. Use `python tests.py` for running the tests.
2. There should be some kind of test for the Dockerfile you wrote
3. Add additional unit test (or any other level of tests) for testing the app

### Guidelines 

* Except the app functionality, you can change whatever you want - structure, tooling, libraries, ... If possible, add `notes.md` file which explains reasons, logic, thoughts and anything else you would like to share
* The CI part should include the source code for the pipeline definition
