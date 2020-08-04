from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import xml.etree.ElementTree as ET

stream = file('robot_calibration.yaml', 'r')
data = load(stream, Loader=Loader)
print(data['kinematics']['shoulder'])

def modifyBody(body, translation, rotation):
    body[0].text = str(translation).strip('[]')
    body[1].text = str(rotation).strip('[]')

tree = ET.parse('ur5e.default.xml')
root = tree.getroot()
modifyBody(root[0], [1, 2, 3], [1, 2, 3, 4])
link_0 = root[0]
print(link_0[0].text)
print(link_0[1].text)


    