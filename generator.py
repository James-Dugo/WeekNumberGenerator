import sys
import datetime

def printHeader(file):
    file.write("""BEGIN:VCALENDAR
VERSION:2.0
X-WR-CALNAME:Session2_Week_Numbers
X-WR-TIMEZONE:Australia/Sydney
CALSCALE:GREGORIAN
""")
     
def printWeek(f,dateStart,dateEnd, weekNum):
    f.write("""BEGIN:VEVENT
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
DESCRIPTION:This is a reference for Mqu Session 2 2022
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Week %d
TRANSP:TRANSPARENT
END:VEVENT
""" % (dateStart.strftime("%Y%m%d"),dateEnd.strftime("%Y%m%d"),weekNum))

def printBreak(f,dateStart,dateEnd):
    f.write("""BEGIN:VEVENT
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
DESCRIPTION:This is a reference for Mqu Session 2 2022
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Break
TRANSP:TRANSPARENT
END:VEVENT
""" % (dateStart.strftime("%Y%m%d"),dateEnd.strftime("%Y%m%d")))
    
f = open('out.ical','w')
printHeader(f)
numWeeks=13
hadBreak=False
startDate=datetime.date(2022,7,24)
endDate=startDate+datetime.timedelta(weeks=1)
for x in range(1,numWeeks):
    printWeek(f,startDate,endDate,x)
    startDate=endDate+datetime.timedelta(days=1)
    endDate=startDate+datetime.timedelta(weeks=1)
    
f.write("END:VCALENDAR")
f.close()