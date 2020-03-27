import requests

#runtime cache for stations
station_cache = {}

def get_weather_for_date_at_location(date, latitude, longitude, api_key):
    station_id = None
    key = (latitude, longitude)
  
    if key in station_cache:
        station_id = station_cache[key]
    else :
        station_api_call = 'https://api.meteostat.net/v1/stations/nearby?lat={latitude}&lon={longitude}&limit=1&key={api_key}'
        response = requests.get(station_api_call.format(latitude=latitude, longitude=longitude, api_key=api_key))
        if response.status_code == 200:
            content=response.json()['data'][0]
            station_id = content['id']
            station_cache[(latitude,longitude)] = station_id
    
    if station_id is None:
        return None
    
    weather_api_call = 'https://api.meteostat.net/v1/history/daily?station={station}&start={start_date}&end={end_date}&key={api_key}'
    response = requests.get(weather_api_call.format(station=station_id, start_date=date, end_date=date, api_key=api_key))
    if response.status_code == 200:
        return response.json()['data'][0]
    
    return None
    
