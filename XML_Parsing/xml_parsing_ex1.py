import xml.etree.ElementTree as ET
import binascii
tree = ET.parse('WPA2_PSK_AES.xml')
root = tree.getroot()
import robot.libraries.OperatingSystem

#print(root[4].tag)
print(root[5])
name_index = -1
ssid_config_index = -1
msm_index = -1
for x, i in enumerate(root):
    if "name" in i.tag :
        name_index = x
    elif "SSIDConfig" in i.tag:
        ssid_config_index = x
    elif "MSM" in i.tag:
        msm_index = x

print(name_index, ssid_config_index, msm_index)

name = root[name_index].text
print(name)
for x in root[ssid_config_index]:
    for subtag in x:
        if "hex" in subtag.tag:
            subtag.text = "113527832837263"
        elif "name" in subtag.tag:
            subtag.text = "Testing"

for x in root[msm_index]:
    for subtag in x:
        if "sharedKey" in subtag.tag:
            for el in subtag:
                if "keyMaterial" in el.tag:
                    el.text = str(binascii.hexlify(b'PPSK_HS_DEMO')).strip('b').strip("'")


tree.write('Open_Auth2.xml', default_namespace='xmlns')
print("Hanamant Testing")
print("Hanamnat Testing2")

def modify_xml(ssid):
    for x in root:
        if 'name' in x.tag:
            x.text = str(ssid)
            break

# for x in root:
#     for subelement in x:
#         for child in subelement:
#             print(child.tag)

#
# tree.write('Open_Auth1.xml', default_namespace='xmlns')
