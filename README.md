# DDoS Attack Script Using Proxies

This Python script allows you to send HTTP requests through a list of proxy servers for the purpose of conducting DDoS attacks. It is designed to overload target websites by using multiple proxies to distribute the load.

## Features

- Loads a list of proxies from a specified file.
- Sends HTTP GET requests to a target URL using each proxy.
- Handles proxy errors and request exceptions.
- Displays the response from the target site.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:


pip install requests
text

## Usage

1. Clone the repository or download the script file.
2. Create a text file named `proxy.txt` in the same directory as the script.
3. Open the script and replace `URL_TARGET_SITE` with the URL of the site you want to attack.
4. Execute the script using Python:


python your_script_name.py
text

Replace `your_script_name.py` with the actual name of your Python file.


