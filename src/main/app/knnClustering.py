import math
import random

import numpy as np

SQL_ID = 0
SQL_LAT = 1
SQL_LON = 2


def distance(centroid, marker):
    """
    Function to calculate the distance between two points
    """
    c_lat, c_lon = centroid[SQL_LAT], centroid[SQL_LON]
    m_lat, m_lon = marker[SQL_LAT], marker[SQL_LON]

    return math.sqrt((c_lat - m_lat) ** 2 + (c_lon - m_lon) ** 2)


class KnnClustering:
    """
    Class allowing to realize the grouping of markers
    """

    def __init__(self, markers, centroids=4):
        self.markers = markers
        self.nb_centroids = centroids
        self.centroids = []
        if not self.markers:
            return
        for i in range(centroids):
            base_marker = random.choice(markers)

            self.centroids.append((i, base_marker[SQL_LAT], base_marker[SQL_LON], 0))


    def knn_clustering(self):
        """
        Define the knn clustering to regroup marker
        """
        if not self.markers:
            return []

        for _ in range(4):
            group_markers = [[] for _ in range(self.nb_centroids)]
            for marker in self.markers:
                min_dist = math.inf
                min_index = 0
                for index, centroid in enumerate(self.centroids, start=0):
                    curr_distance = distance(centroid, marker)
                    if curr_distance < min_dist:
                        min_dist = curr_distance
                        min_index = index
                group_markers[min_index].append(marker)

            for index, group in enumerate(group_markers):
                if not group:
                    continue


                # print(f"index {index}")#
                # print(np.array(group).shape)
                # print(np.array(group)[:10, 1:3])
                # print(np.array(group)[0])
                # used_group = np.array(np.array(group))

                # new_coords = used_group.mean(axis=0)
                new_coords = np.array([[row[1],row[2]] for row in group]).mean(axis=0)


                # print(f"new_coords {new_coords} and type {type(new_coords)}")
                self.centroids[index] = (index, new_coords[0], new_coords[1], len(group))

        # print(f"self : {self}")
        return self.centroids

    def __str__(self):
        """
        Str
        """
        return "%ld markers \n" \
               "%d centroids \n" \
               "positions : %s" % \
               (len(self.markers), self.nb_centroids, self.centroids)
