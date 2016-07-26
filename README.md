# SIGTERM demo

This is an example of how to handle SIGTERM in python. It defines a function that will be called when `docker stop` is executed on the running container.

    docker build -t mindi/sigterm_demo:latest
    docker run -i --name=sigterm_demo -t mindi/sigterm_demo:latest

In another terminal:

    docker stop sigterm_demo
