"""
Given two arrays of equal size. First Array represents in the arrival timings of trains.
Second array represents the departure timings of the same trains.
Now with the above two arrays data, give the number of platforms required to accommodate the trains.
"""

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

n = len(arr)

def findPlatforms(arr, dep, n):
    arr.sort()
    dep.sort()

    platformsNeeded = 1
    result = 1
    i = 1
    j = 0

    while (i < n and j < n):
        if (arr[i] < dep[j]):
            platformsNeeded += 1
            i += 1

            if (platformsNeeded > result):
                result = platformsNeeded

        else:
            platformsNeeded -= 1
            j += 1

    return result

print("Arrival Timings: ",arr)
print("Departure Timings: ",dep)

print("Min. no.of platforms required = ",findPlatforms(arr,dep,n))
