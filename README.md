# project_psip

## Description
Project for PSIP 23/24 for Stanisław Skrzyński.
Application for food delivery service. Basic local database controls with crud for clients, couriers orders and restaurants and locations.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

pip install -r ./requirements.txt


## Usage

Run application from main.py 
First login window will pop-up and you need to enter the login and password as well as the parameters to your postgres database. For this to work you need the postgis extention installed. You can load params from .env file from main directory. While checking simulate option some random entries should be created for each of the table. You should be able to login using admin:admin.
When logged in the main window will pop-up and you can manipulate all the data from there.

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## TODO
- better address system
- simulating adding locations with normal addresses.
- add separate windows for couriers, restaurants and clients