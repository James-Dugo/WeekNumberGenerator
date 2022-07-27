import sys



def printHeader(file):
    with file:
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        file.write("X-WR-CALNAME:WEEKNUMBERS\n")
        file.write("X-WR-TIMEZONE:Australia\n")
        file.write("CALSCALE:GREGORIAN\n")
     
     
with open('test.ical','w') as f:
    printHeader(f)

f.close()