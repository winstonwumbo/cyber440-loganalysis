import xml.etree.ElementTree as ET
from collections import defaultdict

event_id_input = input("Enter the EventID to search for (4624): ")

inputfile = 'SecurityLog-rev2.xml'
outputfileXML = open('partDoutput.xml', 'w')
outputfileMD = open('partDTimeCount.md', 'w')

tree = ET.parse(inputfile)
root = tree.getroot()

namespaces = {'': 'http://schemas.microsoft.com/win/2004/08/events/event'}

numevents_per_hour = defaultdict(int)

numevents_total = 0

for event in root.findall('Event', namespaces):
    event_id_object = event.find('System/EventID', namespaces)
    if event_id_object is not None:
        event_id = event_id_object.text
        if event_id == event_id_input:
            outputfileXML.write(ET.tostring(event, encoding='unicode'))
            
            time_created_object = event.find('System/TimeCreated', namespaces)
            if time_created_object is not None:
                full_timestamp = time_created_object.get('SystemTime')
                # Shortens the timestamp to the hour (first 13 characters, including the T)
                cleaned_timestamp = full_timestamp[:13]
                numevents_per_hour[cleaned_timestamp] += 1
                numevents_total += 1

outputfileXML.close()

for timestamp in sorted(numevents_per_hour):
    print(str(timestamp) + "   " + str(numevents_per_hour[timestamp]))
    outputfileMD.write(str(timestamp) + "   " + str(numevents_per_hour[timestamp]))

print("Number of events with EventID " + str(event_id_input) + ": " + str(numevents_total))
outputfileMD.write("Number of events with EventID " + str(event_id_input) + ": " + str(numevents_total))
outputfileMD.close()

print("Output saved to ./partDoutput.xml and ./partDTimeCount.md")
