from meteostat import get_weather_for_date_at_location
import configparser

CONFIG_FILE = 'config.ini'

config_parser = configparser.ConfigParser()
config_parser.read(CONFIG_FILE)
if len(config_parser) == 0:
    print("ERROR: no config file loaded")
    exit(1)

api_key = config_parser.get('Login Parameters', 'api_key', fallback='')

if len(api_key) == 0:
    print("Missing configuration file with API Key")
    exit(1)


#47.575482, -122.129757, KRNT0
result = get_weather_for_date_at_location(date='2019-03-03', latitude=47.575482, longitude=-122.129757, api_key=api_key)

print(result)