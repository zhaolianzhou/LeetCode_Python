import math
import operator
def nearestVegetarianRestaurant(totalRestaurants, allLocations, numRestaurants):
    # WRITE YOUR CODE HERE
    distance_list = {}
    for i in range(0, totalRestaurants):
        x = allLocations[i][0]
        y = allLocations[i][1]
        distance_list[i] = x*x + y*y

    sorted_distances = sorted(distance_list.items(), key = operator.itemgetter(1))

    result_rests = []
    for j in range(0, numRestaurants):
        result_rests.append(allLocations[sorted_distances[j][0]])
    return result_rests

if __name__ == "__main__":
    strs = [[2, 4], [3, 6], [5, 3], [2,7],[1, 8], [7,9]]
    print(nearestVegetarianRestaurant(6, strs, 3))