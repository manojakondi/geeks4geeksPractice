"""
Given a time in hours and minutes, find the angle between hours and minutes pointers in analog clock.
"""

def findAngle(hour, minute):
    #find minutes had position
    m = float(int(minute)*6);
    #find hours hand position
    h = float(int(hour)*(float(360/12))) + (float(int(minute)*360/(12*60)));

    angle = abs(h-m)
    if(angle > 180):
        angle = float(360-angle);

    return angle;

def main():
    hour=input("hour: ");
    minute=input("minute: ");
    print(findAngle(hour,minute));

if __name__ == '__main__':
    main();
