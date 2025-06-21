import xml.etree.ElementTree as ET

class Gun:
    def __init__(self, gun_element: ET.Element):
        self.info = {
            "Name" : gun_element.get("name"),
            "Damage" : gun_element.find("damage").text,
            "Damage Type" : gun_element.find("damage-type").text
        }

        print(self.info)
