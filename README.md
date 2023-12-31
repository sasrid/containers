# Containers 101

## Terminologies

- Docker -  It's a company who pioneered implementation of container images, tools and associated ecosystem.

- Container Image - It's a portable packaged image that can be run anywhere where 'Container Runtime' installed. 

- Dockerfile - It's a file to define dependencies and the base image.

## Intro 

This repo has a simple python application that uses Flask framework. Generally, to run this python program, you need to have Python and Flask installed. It's impossible or more problematic when you need to run this on a different laptop or server.  You need to work with the owner of the laptop or owner to install these dependencies before running the program.  This is where container images are helpful.  This documentation explains the process of creating a container image and also methods to run them. 

## Creating a Container image  

### Dockerfile  
Create a file named Dockerfile in the directory where app is.     
Used python:3.8-slim as the base image.  Think of it like a fresh server or a laptop with python installed.  
Next two lines/instructions WORKDIR and COPY sets up working directory and copy files from the current directory to the working directory.  Your app code is copied into the working directory at this time. 
Nex command pip installs dependencies coded in the requirements.txt
Expose command is merely a documentation command. Refer https://docs.docker.com/engine/reference/builder/#expose for more info
ENV is optional.  
CMD is the one that sets the command to be executed when running a container from an image. 

### Docker build or Container build

```
docker build -t sarveshsridher/sampleapp:v1 .

```

This command builds the container image locally and tags it with sarveshsridher/sampleapp:v1   
sarveshsridher is the Docker hub account. 
sampleapp is the repository. 
v1 is a tag.  This can be used to reference multiple versions of the image (useful when updating/making changes to program).   

At the end of docker build command, you should be able to see the image locally. Use this following command to list. 
```
docker image ls
```

At this time, your docker image is ready to be run locally.  Command to run this is 'docker run'

```
docker run -p 5000:5000 sarveshsridher/sampleapp:v1
``` 

This -p option is to ask docker to setup port forwarding from local machine to docker network where container image is running. 


All this is good for local runs, but the purpose of containers are to run anywhere.  In order to run anywhere, this container image needs to be stored in a central repository.   There are several container registries that can hold user repositories.  Docker hub is one of them. Other ones are Azure Container Registry,  Google Container Registry and so on.  


### Docker push

For pushing, in other words, for storing container images require authentication credentials.  Use the following instructions to get one.   

Go to Dockerhub website, under Profile, Security, create 'Access Token' and provide write access. 
```
docker login -u sarveshsridher (use your own account name here)
```
use token password
```
docker push sarveshsridher/sampleapp:v1
```
This results in container image pushed to Docker hub (central repo that can be used from anywhere in the world to pull images)

### Docker run

You can run this following command anywhere in the world where docker runtime is installed. Most importantly, you don't need to ask your server owner or anyone to install python or flask, etc.   
```
docker run -p 5000:5000 sarveshsridher/sampleapp:v1
```

##  References 

https://www.freecodecamp.org/news/demystifying-containers-101-a-deep-dive-into-container-technology-for-beginners-d7b60d8511c1/ 
