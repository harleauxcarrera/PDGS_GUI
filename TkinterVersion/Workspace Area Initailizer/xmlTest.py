import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="Type", value="1 Byte").text = "This identifies whether the packet is a Echo (8) (ping) or Echo Reply (0) (Ping reply)"
ET.SubElement(doc, "field2", name="Code", value="1 Byte").text = "Always equal to a value of zero (0)"
ET.SubElement(doc, "field3", name="Checksum", value="2 Bytes").text = "Header checksum"
ET.SubElement(doc, "field4", name="Identifier", value="2 Bytes").text = "If code field =0, then this field is used as an identifier to aid in matching echos and replies"
ET.SubElement(doc, "field5", name="Sequence Number", value="2 Bytes").text = "If code field = 0, then this field is used as and identifier to aid in matching echos and replies"
ET.SubElement(doc, "field6", name="Variable Data", value="Var size").text = "This section serves as data padding. Size varies so the packet meets the minimum size required. This size varies depending on the frame used on your LAN"



tree = ET.ElementTree(root)
tree.write("ICMP.xml", encoding="utf-8", xml_declaration=True)