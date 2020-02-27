# Docker Environment Creator (denv-creator)

***This project is under construction and does not currently function properly. Feel free to use it and test it.***

Automates the process of creating a docker environment (using `docker-compose`) with all the containers you want, also with all of their respective configuration files. This can be done by answering a few questions on the command line.

# Supported Containers

* Nginx ***(WIP)***
* PHP-FPM ***(WIP)***

# Requirements

* Python

# Install and Run

*Note: All files related to the docker environment will reside **under** this cloned project - make sure to make this cloned project the name of your project. Say you clone this project in `/tmp/my-docker-project`, the files will be placed underneath such as `/tmp/my-docker-project/docker-compose.yml`*

**Navigate to Where The Docker Project Will Lie**

`cd /path/to/my/development/environments`

**Clone the repo**

 `git clone https://github.com/ebebbington/docker-environment-creator.git your-project-name`
 
 `cd your-project-name`
 
 **Create your environental files!**
 
 `python docker-environment-creator/index.py`
 
 ***Note: The `docker-environment-creator` directory will remove itself once everything is complete leaving only the files created by this python project***

# Built With

* [Python](https://docs.python.org) - Language used

# Authors

* Edward Bebbinton - **Owner/Developer** - [ebebbington](https://github.com/ebebbington)
* Will Bebbington - **Developer** - [willjb95](https://github.com/willjb95)

# Contributing

See [here](#CONTRIBUTING.md)

# License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
