# CookWise - A Professional REST API with Python, Django REST Framework, and Docker using Test-Driven Development (TDD)

## Overview
CookWise is an API web application that allows users to create and manage their own recipes and ingredients. Each user can register, log in, and build a personalized collection of recipes and ingredients. The project is built with Django REST Framework (DRF) to provide a robust and scalable API, following best practices with Test-Driven Development (TDD) to ensure reliability and maintainability.

The application is designed with security, scalability, and ease of use in mind, and is deployed on Amazon Web Services (AWS) for production.

#### Link - http://ec2-3-83-146-24.compute-1.amazonaws.com/api/docs/

## Installation

### Creating a New App in Django
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
# Verify the Following:
Make sure the template project branch has the following features:

1. Flake8 is used.
2. Basic User creation is implemented.
3. Token authentication is set up.
4. Docker is properly configured.
5. Unit tests are written for most features.
   
# Deployment

Local Deployment (Ensure Port is Set to 8000)

```bash
docker-compose -f docker-compose-deploy.yml down
docker-compose -f docker-compose-deploy.yml up
```

# Connecting to an EC2 Instance

1. Set up SSH keys.
2. Add the SSH key-pair into the EC2 instance.
3. Connect to the EC2 instance using the following command:

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
