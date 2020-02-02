# Aeroform

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The Aeroform is a web application which make airport self-registration more easiest for traveller.
Administrators can on their side, check, correct, validate or devalidate travelers's registrations.

This webapp has been design for the moment for two countries:
* Mali
* Congo DR

# New Features!
  - Generate QRcode for a registration
  - Found a registration by id or QRcode
  - View an detailled statitic of all registration

You can also:
  - Export all registration in Excel file
  - Add easily new domain support
  - Send a feedback or request to administrator

This app has been made in intent to run in containers . You'll find all informations in the docker and docker-compose files.

NB: The app need to be tested more ! Your contribution will be very helpful :)
You can make your own modification to make it compatible on the cloud (like GKE, AKS, EKS ...)
Please refer to the Setup section !

### Tech

Aeroform uses a number of open source projects to work properly:

* Python - used in many application domains
* Django - Python web framework for developers with short deadline
* Semantic UI - Awesome CSS framework
* jQuery - Javascript DOM Manipulator Framework

### Requirements
* Docker - Required
* Docker-compose - Required
* Python - Required
* Django - Required

### Installation
First you need to edit two files in the env foler
* .aero_env - Environment variables to run django container.
* .db_env - Environment variables to setup database container

NB: For Django secret's variable, you should probably use a robust encrypted passhprase
```sh
echo 'mypassphrase' | base64
```

Then install the dependencies and devDependencies and start docker-compose.

```sh
$ docker-compose build
$ docker-compose up -d 
$ docker container ls (to see if everything is going well)
```
Verify the deployment by navigating to your server address in your preferred browser.

### Development

Want to contribute? Great!

It's a very interesting project.
You can ask for a pull-requests and make your involment.

Feel free to contact me.

MIT
