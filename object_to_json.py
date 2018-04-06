import json
from hotel import Hotel

def obj_dict(obj):
    return obj.__dict__

def write_to_json(list_hotels):
    json_file = open("hotels.json","w", encoding="utf-8")
    json.dump([ob.__dict__ for ob in list_hotels],json_file)
    json_file.close()
    print("Data written as Json")
