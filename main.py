import csv
from bin.hotel import Hotel
from bin.validate_record import validate_name, validate_rating, validate_url
from bin.object_to_json import write_as_json
from bin.object_to_xml import write_as_xml

def validate_record(a):
    """ Validates a record according to its name, rating and url """
    if(a != []):
        if(bool(validate_name(a[0])) and bool(validate_rating(a[2])) and bool(validate_url(a[5]))):
            return Hotel(a[0],a[1],a[2],a[3],a[4],a[5]) 
        else:
            pass

def write_data(data):
    write_as_json(data)
    write_as_xml(data)

path = r"data/hotels.csv"
file = open(path,encoding='utf-8', errors='surrogateescape', newline='')
reader = csv.reader(file)
reader = filter(lambda x : x != [], reader)

header = next(reader) # The first line is the header
result = list(map(validate_record, reader))
write_data(result)

