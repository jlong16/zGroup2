import math
import json

#this is a list of [tag nums, distances] to travel to
aprilTargets = ([41, 80], [36, 80], [24, 60])
    [26, 80], [30, 80], [29, 80], [20, 80], [19, 80], [22, 80])
endOptions = (24, 27, 25, 26, 30, 28, 31, 29, 33, 20, 19, 21, 35,22, 34, 32)

#finds the closes tag to a point
def getClosestTag(x, z, is_inside):
    f = open('worldPoints.json', 'r')
    worldPoints = json.load(f)
    f.close()
    keys = worldPoints.keys()

    best_distance = 100000
    for i in range(0, 49):
        if str(i) in keys: 
            #only look at keys <1  (outside)   
            if (worldPoints[str(i)][0][2] >= 0 and is_inside) or (worldPoints[str(i)][0][2] < 0 and not is_inside): 
                full_tag_dat = worldPoints[str(i)]
                tag_loc = (full_tag_dat[0][0], full_tag_dat[0][2])
                dist = math.sqrt(pow(x - tag_loc[0], 2) + pow(z - tag_loc[1], 2))
                if dist < best_distance:
                    best_distance = dist
                    best_tag = i
    print("selected target:" + str(best_tag))
    return (best_tag, 80)

#finds the index of the last point in the targets
def findEndIndex():
    pass