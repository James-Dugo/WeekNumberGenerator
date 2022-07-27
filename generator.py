import sys

UID = "6rgn5vj7deelo7blsmh0touo2b@google.com"

class myDate:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    
    def toString(self):
        retstr=("%d%02d%02d"%(self.year,self.month,self.day))
        return retstr

def printHeader(file):
    with file:
        file.write("""BEGIN:VCALENDAR
VERSION:2.0
X-WR-CALNAME:Session2_Week_Numbers
X-WR-TIMEZONE:Australia/Sydney
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Australia/Sydney
X-LIC-LOCATION:Australia/Sydney
BEGIN:STANDARD
TZOFFSETFROM:+1100
TZOFFSETTO:+1000
TZNAME:AEST
DTSTART:19700405T030000
RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU
END:STANDARD
BEGIN:DAYLIGHT
TZOFFSETFROM:+1000
TZOFFSETTO:+1100
TZNAME:AEDT
DTSTART:19701004T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=1SU
END:DAYLIGHT
END:VTIMEZONE""")
     
def printWeek(f, UID, dateStart,dateEnd, weekNum):
    print("""BEGIN:VEVENT
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
UID:%s
DESCRIPTION:This is a reference for the week
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Week %d
TRANSP:TRANSPARENT
END:VEVENT
""" % (dateStart.toString(),dateEnd.toString(),UID,weekNum), file=f)

with open('test.ical','w') as f:
    printHeader(f)

f.close()