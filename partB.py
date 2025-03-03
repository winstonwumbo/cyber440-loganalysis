import xml.etree.ElementTree as ET

event_id_input = input("Enter the EventID to search for (4624): ")

inputfile = 'SecurityLog-rev2.xml'

outputfile = open('partBoutput.xml', 'w')

tree = ET.parse(inputfile)
root = tree.getroot()

namespaces = {'': 'http://schemas.microsoft.com/win/2004/08/events/event'}

for event in root.findall('Event', namespaces):
    event_id_object = event.find('System/EventID', namespaces)
    if event_id_object is not None:
        event_id = event_id_object.text
        if event_id == event_id_input:
            outputfile.write(ET.tostring(event, encoding='unicode'))

outputfile.close()

print("Output saved to ./partBoutput.xml")