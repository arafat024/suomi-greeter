## suomi-greeter

suomi-greeter is a small Python Flask web application packaged as a Docker image.
It demonstrates how to containerize and publish a simple backend service using Docker.

The application responds with Finnish-style greetings and provides a small example API.

## Features

- JSON API responses
- Personalized greeting endpoint
- Simple calculation endpoint
- Fully Dockerized using Python and Flask

## Endpoints

- `/`  
  Returns a welcome message and usage hints

- `/greet?name=YourName`  
  Returns a greeting, e.g.  
  `{ "greeting": "Terve, YourName!" }`

- `/square?number=5`  
  Returns the square of a number

## How to run

Pull the image:

```bash
docker pull arafat024/suomi-greeter:latest
