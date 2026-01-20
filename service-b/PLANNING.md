example data:
{'timestamp': datetime.datetime(2026, 1, 19, 0, 0),
  'location_name': 'Tel Aviv',
  'country': 'Israel',
  'latitude': 32.08088,
  'longitude': 34.78057,
  'temperature': 12.8,
  'temperature_unit': '°C',
  'wind_speed': 3.1,
  'wind_speed_unit': 'km/h',
  'humidity': 92,
  'humidity_unit': '%'}

fastapi
POST /clean

expected commits:

feat (fastapi): server initialized
feat (fastapi): include router
feat (fastapi): api router and healthcheck route
feat (fastapi): POST /clean route (return status message for now)
feat (pandas): dataframe loader and checker
feat (pandas): temperature_catagory column implemented
feat (pandas): wind_status column implemented
feat (json): packaging to be sent to service c 
