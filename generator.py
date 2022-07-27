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
    
    #TODO add support for leap years
    def nextWeek(self):
        if(self.month==2 and self.day>=22):
            #Feb            
            newMonth=self.month+1
            newDay=(self.day+7) % 28
        elif(self.month==(1,3,5,7,8,10,12) and self.day>=25):
            #months w/ 30 days
            newMonth=self.month+1
            newDay=(self.day+7) % 31
        elif(self.day>=21):
            #months w/ 30 days
            newMonth=self.month+1
        else:
            #month doesn't increase
            newMonth=self.month
            newDay=self.day+7
        return myDate(self.year,newMonth,newDay)

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
DESCRIPTION:This is a reference for Mqu Session 2 2022
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Week %d
TRANSP:TRANSPARENT
END:VEVENT
""" % (dateStart.toString(),dateEnd.toString(),UID,weekNum), file=f)

def printBreak(f, UID, dateStart,dateEnd):
    print("""BEGIN:VEVENT
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
UID:%s
DESCRIPTION:This is a reference for Mqu Session 2 2022
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Break
TRANSP:TRANSPARENT
END:VEVENT
""" % (dateStart.toString(),dateEnd.toString(),UID), file=f)
    
with open('test.ical','w') as f:
    printHeader(f)
    numWeeks=13
    hadBreak=False
    startDate=myDate(2022,7,24)
    for x in range(1,numWeeks):
        printWeek(f,UID,startDate,)
        

f.close()