import math

#this is a list of [tag nums, distances] to travel to
aprilTargets = ([2, 70], [46, 80], [37, 80])

#finds the closes tag to a point
def getClosestTag(x, z):
    best_distance = 100000
    for i in range(0, 49): #TODO change this range to exclude undesirable endgame tags (aka in the room)
        if str(i) in keys:
            full_tag_dat = world_coords[str(i)]
            tag_loc = (full_tag_dat[0][0], full_tag_dat[0][2])
            dist = math.sqrt(pow(x - tag_loc[0], 2) + pow(z - tag_loc[1], 2))
            if dist < best_distance:
                best_distance = dist
                best_tag = i
    print("selected target:" + best_tag)
    return (best_tag, 80)

world_coords = {
    "0": [[0, 0, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0]], 
    "1": [[5, 0, 0], [6, 0, 0], [6, -1, 0], [5, -1, 0]], 
    "2": [[10, 0, 0], [11, 0, 0], [11, -1, 0], [10, -1, 0]], 
    "3": [[15, 0, 0], [16, 0, 0], [16, -1, 0], [15, -1, 0]], 
    "4": [[20, 0, 0], [21, 0, 0], [21, -1, 0], [20, -1, 0]], 
    "5": [[25, 0, 0], [26, 0, 0], [26, -1, 0], [25, -1, 0]], 
    "6": [[30, 0, 0], [31, 0, 0], [31, -1, 0], [30, -1, 0]], 
    "7": [[35, 0, 0], [36, 0, 0], [36, -1, 0], [35, -1, 0]], 
    "8": [[40, 0, 0], [41, 0, 0], [41, -1, 0], [40, -1, 0]], 
    "9": [[45, 0, 0], [46, 0, 0], [46, -1, 0], [45, -1, 0]], 
    "10": [[50, 0, 0], [51, 0, 0], [51, -1, 0], [50, -1, 0]], 
    "11": [[55, 0, 4], [55, 0, 5], [55, -1, 5], [55, -1, 4]], 
    "12": [[73, 0, 15], [-73, 0, 16], [73, -1, 16], [73, -1, 15]], 
    "13": [[73, 0, 20], [-73, 0, 21], [73, -1, 21], [73, -1, 20]],
    "14": [[73, 0, 25], [-73, 0, 26], [73, -1, 26], [73, -1, 25]], 
    "15": [[73, 0, 30], [-73, 0, 31], [73, -1, 31], [73, -1, 30]], 
    "36": [[-63, 0, 30], [-63, 0, 29], [-63, -1, 29], [-63, -1, 30]], 
    "37": [[-63, 0, 25], [-63, 0, 24], [-63, -1, 24], [-63, -1, 25]], 
    "38": [[-63, 0, 20], [-63, 0, 19], [-63, -1, 19], [-63, -1, 20]], 
    "39": [[-63, 0, 15], [-63, 0, 14], [-63, -1, 14], [-63, -1, 15]], 
    "40": [[-45, 0, 3], [-45, 0, 2], [-45, -1, 2], [-45, -1, 3]], 
    "41": [[-45, 0, 10], [-45, 0, 9], [-45, -1, 9], [-45, -1, 10]], 
    "42": [[-40, 0, 0], [-39, 0, 0], [-39, -1, 0], [-40, -1, 0]], 
    "43": [[-35, 0, 0], [-34, 0, 0], [-34, -1, 0], [-35, -1, 0]], 
    "44": [[-30, 0, 0], [-29, 0, 0], [-29, -1, 0], [-30, -1, 0]], 
    "45": [[-25, 0, 0], [-24, 0, 0], [-24, -1, 0], [-25, -1, 0]], 
    "46": [[-20, 0, 0], [-19, 0, 0], [-19, -1, 0], [-20, -1, 0]], 
    "47": [[-15, 0, 0], [-14, 0, 0], [-14, -1, 0], [-15, -1, 0]], 
    "48": [[-10, 0, 0], [-9, 0, 0], [-9, -1, 0], [-10, -1, 0]], 
    "49": [[-5, 0, 0], [-4, 0, 0], [-4, -1, 0], [-5, -1, 0]]}

keys = world_coords.keys()