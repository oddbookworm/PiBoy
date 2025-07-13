import xml.etree.ElementTree as ET
from .base_weapon import BaseWeapon
from pprint import pprint

class SmallGun(BaseWeapon):
    def __init__(self, gun_element: ET.Element):
        super().__init__(gun_element)

        self.info["Rate"] = gun_element.find("rate").text
        self.info["Range"] = gun_element.find("range").text
        self.info["Ammo"] = gun_element.find("ammo").text

        pprint(self.info)
