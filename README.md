# CookWise - A Professional REST API with Python, Django REST Framework and Docker using Test Driven Development (TDD)


## Overview
This project is a web application that allows users to create and manage recipes and ingredients. Each user can register, log in, and build their own personalized collection of recipes and ingredients. The project is built with the Django REST Framework (DRF) to provide a robust and scalable API, following best practices with Test-Driven Development (TDD).

The application is designed with security, scalability, and ease of use in mind, and is deployed on Amazon Web Services (AWS) for production environments.

 
## Installation
 
# Creating a new app in Django

```bash
docker-compose run --rm app sh -c "python manage.py startapp core"
```

# Running flake8

```bash
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

# Running unit tests

```bash
docker-compose run --rm app sh -c "python manage.py test"
```
# Verify that:
Template project branch is the branch in which the following things are already done:

1. Flake8 is installed.
2. Basic User creation is done.
3. Token authentication is done.
4. Docker is properly setup.
5. Unit tests are written for most features.
   
# Deployment

Local deployment (Remember to change port to 8000)

```bash
docker-compose -f docker-compose-deploy.yml down
docker-compose -f docker-compose-deploy.yml up
```

# Connecting to EC2 instance

1. Setup ssh keys
2. Add ssh key-pair into EC2 instance
3. Connect to EC2 instance using the following command:

```bash
ssh ec2-user@IPADRESSHERE
```

4. Create ssh key-pair in EC2 instance

```bash
ssh-keygen -t ed25519 -b 4096
```

To view the ssh key-pair:

```bash
cat ~/.ssh/id_ed25519.pub
```

5. Copy the public key to github
