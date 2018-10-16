"""
Given two dates (can be of different years), calculate the number of days between them (taking care of leap years).
"""

dt1 = [1,2,2000]
dt2 = [1,2,2004]

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countLeapYearsFromDate(dt):
    d = dt[0]
    m = dt[1]
    y = dt[2]
    if (m>2):
        return (int(y/4) - int(y/100) + int(y/400))
    else:
        return (int((y-1)/4) - int((y-1)/100) + int((y-1)/400))


def countDays(dt):
    d = dt[0]
    m = dt[1]
    y = dt[2]
    n = y*365 + d

    for i in range(0, m):
        n += daysOfMonth[i]

    n += countLeapYearsFromDate(dt)

    return n

print(countDays(dt2)-countDays(dt1))
