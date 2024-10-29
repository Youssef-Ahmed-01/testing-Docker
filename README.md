# testing docker with sqlite and flask
 modified alpine: python added using "apk add python3"

## Overview

This project is a simple Flask web application that is containerized using Docker.

## Usage

1. **Clone the repo and get Docker installed on your machine**

2. **pull the alpine image**
    ```terminal/bash
    docker pull youssefahmed01/alpask:v1.0
3. **navigate to the repo directory using "cd" command**
4. **build new image v1.1 using Dockerfile**
    ```terminal/bash
    docker build -t youssefahmed01/alpask:v1.1 .
5. **then run using VScode or temrinal**  
    ```terminal/bash
    docker run -it --name <Container-name> youssefahmed01/alpask:v1.1
6. **go to browser to add data or search for data to/from dbfile**  
    http://127.17.0.1:5000
    or
    http://localhost:5000


