import xml.etree.ElementTree as ET

class BaseWeapon:
    def __init__(self, weapon_element: ET.Element):
        self.info = {
            "Name" : weapon_element.get("name"),
            "Damage" : weapon_element.find("damage").text,
            "Damage Type" : weapon_element.find("damage-type").text,
            "Cost" : weapon_element.find("cost").text,
            "Weight": weapon_element.find("weight").text,
            "Rarity": weapon_element.find("rarity").text,
            "Description": weapon_element.find("description").text.strip()
        }

        self.info["Damage Effects"] = t.text if (t := weapon_element.find("damage-effects")) is not None and t else None

        qualities = []
        qualities_element = weapon_element.find("qualities")
        for quality in qualities_element.findall("quality"):
            qualities.append(quality.text)

        self.info["Qualities"] = qualities

        available_mods = {
            "Receivers": [],
            "Barrels": [],
            "Grips": [],
            "Sights": []
        }

        mods = weapon_element.find("available-mods")

        receivers = mods.find("receivers")
        for receiver in receivers.findall("receiver"):
            available_mods["Receivers"].append(receiver.text)

        barrels = mods.find("barrels")
        for barrel in barrels.findall("barrel"):
            available_mods["Barrels"].append(barrel.text)

        grips = mods.find("grips")
        for grip in grips.findall("grip"):
            available_mods["Grips"].append(grip.text)

        sights = mods.find("sights")
        for sight in sights.findall("sight"):
            available_mods["Sights"].append(sight.text)

        self.info["Available Mods"] = available_mods
