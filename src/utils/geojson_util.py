from asyncio import constants
from datetime import datetime
from uuid import uuid4

speed_colors = [
    '#fa6e6e',
    '#fa9b45',
    '#fbf01c',
    '#88ed02',
    '#13c600',
    '#00ba73',
    '#00a9d1',
    '#0093ff',
    '#0071ff',
    '#1800ff',
]

def get_speed_color(speed):
    speed_index = int(speed / 10)
    if (speed_index >= len(speed_colors)):
        speed_index = len(speed_colors)
    return speed_colors[speed_index]

def get_speed(properties):
    for key, value in properties.items():
        lowerKey = key.lower()
        if ('speed' in lowerKey):
            return value
    return 0


def raw_geojson_to_clean_geojson(raw_geojson, file_id = uuid4()):
    gps_element_list = raw_geojson['features']
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    geojson = {
        "type": "FeatureCollection",
        "dataName": f'Selected-Trip-{file_id}',
        "dateTime": now,
        "dataType": "Point",
        "features": []
    }
    for idx, gps_element in enumerate(gps_element_list):
        properties = gps_element["properties"]
        properties['Id'] = gps_element['Id'] if 'Id' in properties else (idx+1)
        properties['Item'] = gps_element['Item'] if 'Item' in properties else 'Driving Point'
        properties['Count'] = gps_element['Count'] if 'Count' in properties else 1
        properties['Color'] = gps_element['Color'] if 'Color' in properties else get_speed_color(
            get_speed(properties))
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": gps_element['geometry']['coordinates']
            },
            "properties": properties}
        geojson['features'].append(feature)
    return geojson
