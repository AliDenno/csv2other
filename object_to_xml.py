import xml.etree.cElementTree as ET
import xml.dom.minidom

class Hotel:
     def __init__(self, full_name, rating):
        self.name = full_name
        self.rating=rating 

def obj_dict(obj):
    return obj.__dict__

Hotel1=Hotel("MER","5")
Hotel2=Hotel("RAK","4")
Hotel3=Hotel("DAM","34")
list_name=[]
list_name.append(Hotel1)
list_name.append(Hotel2)
list_name.append(Hotel3)

root = ET.Element("root")

for hotel in list_name:
    doc = ET.SubElement(root, "hotel")

    #ET.SubElement(doc, "hotelname", name=hotel.name).text = "some value1"
    ET.SubElement(doc, "hotelname").text = hotel.name
    ET.SubElement(doc, "Hotelratings").text = hotel.rating

    tree = ET.ElementTree(root)
tree.write("filename.xml")


xml = xml.dom.minidom.parse("filename.xml") # or xml.dom.minidom.parseString(xml_string)
print(xml.toprettyxml())



