import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('Rahul Shetty API Course\\API Automation\\utilities\\properties.ini')
    return config
