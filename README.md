## ButterCMS Django/Vue Challenge
### Setup Instructions

**=> With Docker**

Install Docker and Docker Compose on your system
- For Mac: [Download Docker Desktop](https://docs.docker.com/docker-for-mac/install/)
- For Linux: 
    - [Install Docker](https://docs.docker.com/engine/install/ubuntu/)
    - [Download Docker Compose](https://docs.docker.com/compose/install/)
    
Run the compose `up` command and wait for the container to build
```sh
$ docker-compose up --build -d
```

In your browser, navigate to https://127.0.0.1:8009/ and you would be able to access the homepage.

********************************************

**=> Without Docker**

Create a python 3 virtual environment
```sh
$ python3 -m venv env
```
Activate the virtual environment
```sh
$ source env/bin/activate
```
Install the dependencies from the requirements file
```sh
$ pip install -r requirements.txt
```
export your ButterCMS key
```sh
$ export BUTTER_KEY='your-key'
```
startup your server
```sh
$ python manage.py runserver
```


In your browser, navigate to https://127.0.0.1:8000/ and you would be able to access the homepage. 