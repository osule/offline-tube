# Offline Youtube

Download Youtube videos for offline viewing.


## Installation

Clone project repository.

    git clone git@github.com:osule/offline-tube.git


Change into the project directory and run

    cp env.template .env

Set the value for `REDIS_URL` if you're running Redis on a different host.


Docker is a prerequisite for building this project.

First, [download and install](https://docs.docker.com/install/) appropriate Docker software for your machine.

Then run the following command in your terminal.

    docker-compose build



## Run

In your terminal, run

    docker-compose up

Navigate to http://localhost:3000/ in your browser.

## Deployment

[TODO]
