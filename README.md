
## Overview

**CookWise** is a web application that allows users to create and manage their own recipes. Users can register, log in, upload images, and build a personalized collection of recipes. It provides a secure and organized platform for users to store and manage their own culinary quest.


## Tech & Tools:  
- **Django REST Framework (DRF):** Used to build secure and reliable APIs with built-in features for authentication and serialization.  
- **Test-Driven Development & Unit Tests:** Ensures the application works as expected by writing tests before code implementation and validating individual components.  
- **Docker:** Creates a consistent and isolated environment for development, testing, and deployment.  
- **AWS:** Provides a reliable platform for deploying the application with high availability and performance.  


#### Give it a try [here](http://ec2-3-83-146-24.compute-1.amazonaws.com/api/docs/) !


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
