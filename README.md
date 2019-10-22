# Docker Environment Creator

Creates all the neccessary files and configurations to build a working docker enironment from scratch. This will create the configuration for each container you specify in a list **but limited to what is supported**, and includes:

* All docker files

* Container configurations

* ... And many more! 

## Supported Containers

* Nginx ***(WIP)***

## Requirements

* Python

## Install and Run

*Note: The docker environment directory will be created where this project was cloned. Say you clone this project in `/tmp`, the new directory will be placed in `/tmp/some-dir`* 

**Navigate to Where The Docker Project Will Lie**

`cd /path/to/some/dir`

**Clone the repo**

 `git clone https://github.com/ebebbington/docker-environment-creator.git`
 
 `cd docker-environment-creator`
 
 **Create your environental files!**
 
 `python creator.py`

## Built With

* [Python](https://docs.python.org) - Language used

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
