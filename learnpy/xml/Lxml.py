import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

root = ET.Element("versionInfo")
ServerInfo = ET.SubElement(root, "ServerInfo")
ET.SubElement(ServerInfo, "ServerIp").text = "ipInfo"
ET.SubElement(ServerInfo, "ServerPort").text = "portInfo"
ET.SubElement(ServerInfo, "XmlLocalPath").text = "xmlInfo"
ET.SubElement(root, "testFolder").set("Version", "0")

rough_bytes = ET.tostring(root, "utf-8")
rough_string = str(rough_bytes, encoding="utf-8").replace("\n", "").replace("\t", "").replace("    ", "")
content = minidom.parseString(rough_string)
with open("tem.xml", 'w+') as fs:
    content.writexml(fs, indent="", addindent="\t", newl="\n", encoding="utf-8")


tree = ET.parse("tem.xml")
print(tree.getroot())
tree.getroot()