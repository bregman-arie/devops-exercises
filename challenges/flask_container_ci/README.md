Your mission, should you choose to accept it, involves fixing the app in this directory, containerize it and set up a CI for it.
Please read carefully all the instructions.

## Installation

1. Create a virtual environment with `python3 -m venv challenge_venv`
2. Activate it with `source challenge_venv/bin/activate`
3. Install requirements.txt `pip install -r requirements.txt`

## Run the app

1. Run `export FLASK_APP=app/app.py`
1. To run the app execute `flask run`. If it doesn't works, fix it


## Containers

Using Docker or Podman, containerize the flask app so users can run the following two commands:

```
docker build -t app:latest /path/to/Dockerfile
docker run -d -p 5000:5000 app
```

1. You can use any image base you would like
2. Containrize only what you need for running the application, nothing else.

## CI

Great, now that we have a working app and also can run it in a container, let's set up a CI for it so it won't break again in the future

1. The CI should run the tests in the app directory
2. There should be some kind of test for the Dockerfile you wrote
2. Add additional unit test (or another level of tests)
