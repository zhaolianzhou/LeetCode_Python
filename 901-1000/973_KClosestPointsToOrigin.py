import operator

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance_list = {}
        for i in range(0, len(points)):
            x = points[i][0]
            y = points[i][1]
            distance_list[i] = x * x + y * y

        sorted_distances = sorted(distance_list.items(), key=operator.itemgetter(1))

        result_rests = []
        for j in range(0, K):
            result_rests.append(points[sorted_distances[j][0]])
        return result_rests