import os
import file_processor as fp
import math
import numpy as np
import ast
from StatisticsToolkit import StatisticsToolkit
from scipy import spatial


class MatrixSimilarityAnalyzer:
    def __init__(self):
        self.prefix_path = os.path.expanduser("~")
        self.starting_path_1 = self.prefix_path + '/Portal/generated-outputs/zhenyue-balanced-combinations-p00'
        self.starting_path_2 = self.prefix_path + '/Portal/generated-outputs/zhenyue-balanced-combinations-p01'
        self.sample_size = 99

    @staticmethod
    def convert_a_list_grn_to_a_matrix(a_grn_phenotype):
        grn_side_size = int(math.sqrt(len(a_grn_phenotype)))
        return np.array(a_grn_phenotype).reshape([grn_side_size, grn_side_size])

    def evaluate_grn_distances(self, a_type, root_directory_path, dist_type):
        list_phenotypes = fp.get_last_grn_phenotypes(self.sample_size, a_type, root_directory_path)
        matrix_phenotypes = list([self.convert_a_list_grn_to_a_matrix(a_phe) for a_phe in list_phenotypes])

        dists = []
        for i in range(len(matrix_phenotypes)):
            for j in range(i+1, len(matrix_phenotypes)):
                if dist_type == 'manhattan':
                    dists.append(np.sum(abs(matrix_phenotypes[i] - matrix_phenotypes[j])))
                elif dist_type == 'cosine':
                    a_cos_dist = spatial.distance.cosine((np.asarray(matrix_phenotypes[i])).reshape(-1),
                                                             (np.asarray(matrix_phenotypes[j])).reshape(-1))
                    dists.append(a_cos_dist)
        return dists

    def statistically_compare_two_group_grn_distances(self, a_type, dist_type):
        dists_1 = self.evaluate_grn_distances(a_type, self.starting_path_1, dist_type)
        dists_2 = self.evaluate_grn_distances(a_type, self.starting_path_2, dist_type)
        print(StatisticsToolkit.calculate_statistical_significances(dists_1, dists_2))


matrix_similarity_analyzer = MatrixSimilarityAnalyzer()
matrix_similarity_analyzer.statistically_compare_two_group_grn_distances('fit', dist_type='manhattan')
