class Solution:
    def findMinArrowShots(self, points):

        points.sort(key=lambda z: z[0])

        endpoint = points[0][1]
        arrows = 1

        for idx in range(1, len(points)):
            endpoint = min(endpoint, points[idx][1])

            if points[idx][0] <= endpoint <= points[idx][1]:
                continue
            else:
                arrows += 1
                endpoint = points[idx][1]

        return arrows