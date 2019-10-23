# Docker Environment Creator

Creates all the neccessary files and configurations to build a working docker enironment from scratch, from the command line. This will create the configuration for each container you specify in a list **but limited to what is supported**, and includes:

* All docker files

* Container configurations

* ... And many more! 

## Supported Containers

* Nginx ***(WIP)***

## Requirements

* Python

## Install and Run

*Note: All files related to the docker environment will reside **under** this cloned project - make sure to make this cloned project the name of your project. Say you clone this project in `/tmp/my-docker-project`, the files will be placed underneath such as `/tmp/my-docker-project/docker-compose.yml`*

**Navigate to Where The Docker Project Will Lie**

`cd /path/to/my/development/environments`

**Clone the repo**

 `git clone https://github.com/ebebbington/docker-environment-creator.git your-project-name`
 
 `cd your-project-name`
 
 **Create your environental files!**
 
 `python docker-environment-creator/index.py`
 
 ***Note: The `docker-environment-creator` directory will remove itself once everything is complete leaving only the files created by this python project***

## Built With

* [Python](https://docs.python.org) - Language used

## Authors

* Edward Bebbinton - **Owner/Developer** - [ebebbington](https://github.com/ebebbington)
* Will Bebbington - **Developer** - [willjb95](https://github.com/willjb95)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details