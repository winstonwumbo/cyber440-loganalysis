import xml.etree.ElementTree as ET

event_id_input = input("Enter the EventID to search for (4625): ")

inputfile = 'SecurityLog-rev2.xml'

outputfile = open('partCoutput.xml', 'w')

numevents = 0

tree = ET.parse(inputfile)
root = tree.getroot()

namespaces = {'': 'http://schemas.microsoft.com/win/2004/08/events/event'}

for event in root.findall('Event', namespaces):
    event_id_object = event.find('System/EventID', namespaces)
    if event_id_object is not None:
        event_id = event_id_object.text
        if event_id == event_id_input:
            outputfile.write(ET.tostring(event, encoding='unicode'))
            numevents += 1

outputfile.close()

print("Number of events with EventID " + str(event_id_input) + ": " + str(numevents))
print("Output saved to ./partCoutput.xml")