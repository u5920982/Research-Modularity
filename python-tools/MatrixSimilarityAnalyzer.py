import os
import file_processor as fp
import math
import numpy as np
import ast
from StatisticsToolkit import StatisticsToolkit
from scipy import spatial
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from time import gmtime, strftime


class MatrixSimilarityAnalyzer:
    def __init__(self):
        self.prefix_path = os.path.expanduser("~")
        self.starting_path_1 = self.prefix_path + '/Portal/generated-outputs/record-zhenyue-balanced-combinations-p00'
        self.starting_path_2 = self.prefix_path + '/Portal/generated-outputs/record-zhenyue-balanced-combinations-p01'
        self.sample_size = 50

    @staticmethod
    def convert_a_list_grn_to_a_matrix(a_grn_phenotype):
        grn_side_size = int(math.sqrt(len(a_grn_phenotype)))
        return np.array(a_grn_phenotype).reshape([grn_side_size, grn_side_size])

    def evaluate_grn_distances(self, list_phenotypes, dist_type):
        matrix_phenotypes = list([self.convert_a_list_grn_to_a_matrix(a_phe) for a_phe in list_phenotypes])

        dists = []
        for i in range(len(matrix_phenotypes)):
            for j in range(i + 1, len(matrix_phenotypes)):
                if dist_type == 'manhattan':
                    dists.append(np.sum(abs(matrix_phenotypes[i] - matrix_phenotypes[j])))
                elif dist_type == 'cosine':
                    a_cos_dist = spatial.distance.cosine((np.asarray(matrix_phenotypes[i])).reshape(-1),
                                                         (np.asarray(matrix_phenotypes[j])).reshape(-1))
                    dists.append(a_cos_dist)
        return dists

    def evaluate_inter_file_grn_distances(self, a_type, root_directory_path, dist_type):
        list_phenotypes = fp.get_last_grn_phenotypes(self.sample_size, a_type, root_directory_path)
        return self.evaluate_grn_distances(list_phenotypes, dist_type)

    def get_pop_phe_lists_of_a_trial(self, file_path, starting_gen=0, ending_gen=None):
        txt_files = []
        phenotypes = []

        for root, dirs, files in os.walk(file_path):
            for a_file in files:
                if a_file.endswith('.lists'):
                    txt_files.append(root + os.sep + a_file)

        if ending_gen is None:
            ending_gen = len(txt_files)

        txt_files = txt_files[starting_gen:ending_gen]

        for a_txt_file in txt_files:
            a_gen_phe = []
            for an_ind in fp.read_a_file_line_by_line(a_txt_file):
                a_gen_phe.append(ast.literal_eval(an_ind))
            phenotypes.append(a_gen_phe)

        return phenotypes

    def get_pop_phe_lists_of_an_experiment(self, root_path, sample_size, starting_gen=0, ending_gen=None):
        pop_phe_lists_list = []
        for a_trial_dir in fp.get_immediate_subdirectories(root_path, no_limitation=5)[:sample_size]:
            print(a_trial_dir)
            pop_phe_lists_list.append(self.get_pop_phe_lists_of_a_trial(a_trial_dir, starting_gen, ending_gen))
        return pop_phe_lists_list

    def evaluate_inter_ind_grn_distances(self, exp_list, dict_type, use_average=True):
        gen_dist_dict = {}
        for pop_phe_lists in exp_list:
            for i in range(len(pop_phe_lists)):
                if gen_dist_dict.has_key(i):
                    if use_average:
                        gen_dist_dict[i].append(np.mean(self.evaluate_grn_distances(pop_phe_lists[i], dict_type)))
                    else:
                        gen_dist_dict[i].append(self.evaluate_grn_distances(pop_phe_lists[i], dict_type))
                else:
                    if use_average:
                        gen_dist_dict[i] = [np.mean(self.evaluate_grn_distances(pop_phe_lists[i], dict_type))]
                    else:
                        gen_dist_dict[i] = [self.evaluate_grn_distances(pop_phe_lists[i], dict_type)]

        return gen_dist_dict

    @staticmethod
    def plot_dist_gen_curve(dist_dict, dpi=500, save_path=None, save_name=None):
        dist_list = []
        if isinstance(dist_dict, dict):
            set_idxs = sorted(dist_dict.keys())
            for a_gen in set_idxs:
                dist_list.append(np.mean(dist_dict[a_gen]))
            fp.plot_a_list_graph(dist_list, 'Avg dist', dpi=dpi, save_path=save_path, save_name=save_name)

        elif isinstance(dist_dict, list):
            set_idxs = sorted(dist_dict[0].keys())
            for a_dist_dict in dist_dict:
                a_dist_list = []
                for a_gen in set_idxs:
                    a_dist_list.append(np.mean(a_dist_dict[a_gen]))
                dist_list.append(a_dist_list)
            fp.save_lists_graph(dist_list, ['sym', 'asym'], path=save_path, file_name=save_name, dpi=dpi)

    def launch_inter_ind_dists(self, starting_gen, dist_type, use_average=True, to_plot=False):
        exp_list_1 = self.get_pop_phe_lists_of_an_experiment(self.starting_path_1, sample_size=self.sample_size, starting_gen=starting_gen)
        exp_list_2 = self.get_pop_phe_lists_of_an_experiment(self.starting_path_2, sample_size=self.sample_size, starting_gen=starting_gen)

        if use_average:
            dist_dict_1 = self.evaluate_inter_ind_grn_distances(exp_list_1, dist_type, use_average=True)
            dist_dict_2 = self.evaluate_inter_ind_grn_distances(exp_list_2, dist_type, use_average=True)

            # print(dist_dict_1)
            # print(dist_dict_2)

            set_idxs_1 = sorted(dist_dict_1.keys())
            set_idxs_2 = sorted(dist_dict_2.keys())

            cur_time = strftime("-%Y-%m-%d-%H-%M-%S", gmtime())

            import json
            with open('./generated_images/dict_1' + cur_time + '.json', 'w') as a_f:
                json.dump(dist_dict_1, a_f, sort_keys=True, indent=4)
            a_f.close()

            with open('./generated_images/dict_2' + cur_time + '.json', 'w') as a_f:
                json.dump(dist_dict_2, a_f, sort_keys=True, indent=4)
            a_f.close()

            if to_plot:
                self.plot_dist_gen_curve(dist_dict_1, dpi=500,
                                         save_path='./generated_images/', save_name=('avg_dist_1' + cur_time + '.png'))
                self.plot_dist_gen_curve(dist_dict_2, dpi=500,
                                         save_path='./generated_images/', save_name=('avg_dist_2' + cur_time + '.png'))
                self.plot_dist_gen_curve([dist_dict_1, dist_dict_2], dpi=500,
                                         save_path='./generated_images/', save_name=('avg_dist_1_2' + cur_time + '.png'))

            print(StatisticsToolkit.calculate_statistical_significances(dist_dict_1[set_idxs_1[-1]],
                                                                        dist_dict_2[set_idxs_2[-1]]))

        else:
            dists_dict_1 = self.evaluate_inter_ind_grn_distances(exp_list_1, dist_type, use_average=False)
            dists_dict_2 = self.evaluate_inter_ind_grn_distances(exp_list_2, dist_type, use_average=False)

            set_idxs_1 = sorted(dists_dict_1.keys())
            set_idxs_2 = sorted(dists_dict_2.keys())

            for dists_1, dists_2 in zip(dists_dict_1[set_idxs_1[-1]], dists_dict_2[set_idxs_2[-1]]):
                print(StatisticsToolkit.calculate_statistical_significances(dists_1, dists_2))

    def statistically_compare_two_inter_file_grn_distances(self, a_type, dist_type):
        dists_1 = self.evaluate_inter_file_grn_distances(a_type, self.starting_path_1, dist_type)
        dists_2 = self.evaluate_inter_file_grn_distances(a_type, self.starting_path_2, dist_type)
        print(StatisticsToolkit.calculate_statistical_significances(dists_1, dists_2))

    def k_means_analysis(self, max_cluster, phenotypes):
        np_phenotypes = np.array(phenotypes)
        previous_score = -1
        for a_cluster in range(2, max_cluster):
            kmeans = KMeans(n_clusters=a_cluster, random_state=2)
            cluster_labels = kmeans.fit_predict(np_phenotypes)
            silhouette_avg = silhouette_score(np_phenotypes, cluster_labels)
            if silhouette_avg < previous_score:
                return a_cluster
            else:
                previous_score = silhouette_avg
        return max_cluster

    def evaluate_k_means_inter_ind(self, exp_list, max_cluster):
        cluster_nos = {}
        for pop_phe_lists in exp_list:
            for i in range(len(pop_phe_lists)):
                if cluster_nos.has_key(i):
                    cluster_nos[i].append(self.k_means_analysis(max_cluster, pop_phe_lists[i]))
                else:
                    cluster_nos[i] = [self.k_means_analysis(max_cluster, pop_phe_lists[i])]
        return cluster_nos

    def launch_k_means_evaluation(self, starting_gen, max_cluster):
        exp_list_1 = self.get_pop_phe_lists_of_an_experiment(self.starting_path_1, sample_size=self.sample_size,
                                                             starting_gen=starting_gen)
        exp_list_2 = self.get_pop_phe_lists_of_an_experiment(self.starting_path_2, sample_size=self.sample_size,
                                                             starting_gen=starting_gen)

        ks_dict_1 = self.evaluate_k_means_inter_ind(exp_list_1, max_cluster)
        ks_dict_2 = self.evaluate_k_means_inter_ind(exp_list_2, max_cluster)

        print(ks_dict_1)
        print(ks_dict_2)

        set_idxs_1 = sorted(ks_dict_1.keys())
        set_idxs_2 = sorted(ks_dict_2.keys())

        print(StatisticsToolkit.calculate_statistical_significances(ks_dict_1[set_idxs_1[-1]],
                                                                    ks_dict_2[set_idxs_2[-1]]))


matrix_similarity_analyzer = MatrixSimilarityAnalyzer()
# matrix_similarity_analyzer.statistically_compare_two_inter_file_grn_distances('fit', dist_type='manhattan')
matrix_similarity_analyzer.launch_inter_ind_dists(starting_gen=1, dist_type='manhattan', use_average=True, to_plot=True)
# matrix_similarity_analyzer.launch_k_means_evaluation(2000, 32)
