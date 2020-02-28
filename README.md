# Docker Environment Creator (denv-creator)

***This project is under construction and does not currently function properly. Feel free to use it and test it.***

Automates the process of creating a docker environment (using `docker-compose`) with all the containers you want, also with all of their respective configuration files. This can be done by answering a few questions on the command line.

# Supported Containers

* Nginx
* PHP-FPM

# Requirements

* Python

# Install and Run

**Clone the repo**

`cd /path/to/my/development/environments`
`git clone https://github.com/ebebbington/denv-creator.git`
 
 **Create your project!**
 
 `python denv-creator/index.py`
 
# File Structure

* `__pycache__/`
  * Cached files of our python scripts. This gets generated automatically and they are being ignored
  
* `.github/`
  * Holds github related configurations. Nothing to worry about
  
* `containers/`
  * The list of container classes. This holds a class for each container - which encapsulates the logic for each one
  
* `data/`
  * General files to aid in the container configuration such as the default `php.ini` file
  
* `.gitignore`
  * Contains a list of files or directories for Git to ignore as we don't want those files committed
  
* `CONTRIBUTING.md`
  * Contribution guide
  
* `index.py`
  * Our main entrypoint script, makes the basic calls to the `Project` class to setup the environment
  
* `LICENSE.txt`
  * License file
  
* `project.py`
  * Our project class. This is where the magic happens. It holds 90% of the logic for the project (represents the project)
  
* `README.md`
  * `self`
  
* `response.md`
  * A class to handle speaking to the user. This abstracts the logic to log out data, ask for input or show errors

* `test.py`
  * Testing file to act as a playground
  
* `validate.py`
  * Validation file to handle all things validat-ey

# Flow of Execution

1. Use calls the main script

2. The main scripts makes all the calls to the `Project` methods

3. The project class is what does the magic. It collects data from the user

4. Eventually when all data is collected, the project class uses the container classes to aid in creating/writing files and directories

# Built With

* [Python](https://docs.python.org) - Language used

# Authors

* Edward Bebbinton - **Owner/Developer** - [ebebbington](https://github.com/ebebbington)
* Will Bebbington - **Developer** - [willjb95](https://github.com/willjb95)

# Contributing

See [here](#CONTRIBUTING.md)

# License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
