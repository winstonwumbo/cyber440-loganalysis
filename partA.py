inputfile = open('SecurityLog-rev2.xml', 'r')

outputfile = open('partAoutput.xml', 'w')

numLines = 0

for line in inputfile:
    outputfile.write(line)
    
    numLines += 1

inputfile.close()
outputfile.close()

print("Number of lines processed: ", numLines)
print("Output saved to ./partAoutput.xml")