# portl
a simple python port scanner

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites 
What things you need to install the software and how to install them
```
python3
```

### Installing
```
git clone https://github.com/blackc8/portl.git
cd portl
```
### Testing
```
python portl.py scanme.nmap.org
```

## Usage
```
usage: portl.py [-h] [-dp] [-sF] [-b] [-v] <hostname>

a simple python port scanner

positional arguments:
  <hostname>            host to scan

optional arguments:
  -h, --help            show this help message and exit
  -dp, --ddport         do not display port
  -sF, --show_filtered  show filtered ports
  -b, --banner          grab the banners of ports
  -v, --version         dispaly version

author: blackc8
```
## Contributers
*  **Initial work** - [blackc8](https://github.com/blackc8)
 
##  License & copyright
© 2020 blackc8

Licensed under the [MIT LICENSE](LICENSE)
