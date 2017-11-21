import GRNPlotter
import FitnessPlotter
from file_processor import save_a_list_graph
from file_processor import count_number_of_edges


class ModularityDominanceAnalyzer:
    def __init__(self):
        self.grn_plotter = GRNPlotter.GRNPlotter()
        self.fitness_plotter = FitnessPlotter.FitnessPlotter()

    def get_fitness_modularity_pair_of_a_trial(self, a_path):
        phenotypes = self.grn_plotter.get_grn_phenotypes(a_path)
        grns = map(self.grn_plotter.generate_directed_grn, phenotypes)
        modularity_values = map(self.grn_plotter.get_modularity_value, grns)
        fitnesses = self.fitness_plotter.get_fitness_values_of_an_trial(a_path)
        return zip(fitnesses, modularity_values)

    def get_the_fittest_individual_in_the_most_modular_networks(self, a_path, starting_generation):
        tuples = self.get_fitness_modularity_pair_of_a_trial(a_path)

        max_modularity = max(x[1] for x in tuples[starting_generation:])

        tmp_fitness = 0
        target_generation = 0
        for a_tuple_idx in range(starting_generation, len(tuples)):
            if tuples[a_tuple_idx][1] == max_modularity:
                if tuples[a_tuple_idx][0] >= tmp_fitness:
                    tmp_fitness = tuples[a_tuple_idx][0]
                    target_generation = a_tuple_idx
        return target_generation, tuples[target_generation][0], tuples[target_generation][1]

    def get_the_least_modular_individual_in_the_fittest_networks(self, a_path, starting_generation):
        tuples = self.get_fitness_modularity_pair_of_a_trial(a_path)

        max_fitness = max(tuples[starting_generation:])[0]

        tmp_modularity = 1
        target_generation = 0
        for a_tuple_idx in range(starting_generation, len(tuples)):
            if tuples[a_tuple_idx][0] == max_fitness:
                if tuples[a_tuple_idx][1] <= tmp_modularity:
                    tmp_modularity = tuples[a_tuple_idx][1]
                    target_generation = a_tuple_idx
        return target_generation, tuples[target_generation][0], tuples[target_generation][1]

    def get_edge_number_trend(self, a_path):
        phenotypes = self.grn_plotter.get_grn_phenotypes(a_path)
        edge_numbers = []
        for a_phenotype in phenotypes:
            edge_numbers.append(count_number_of_edges(a_phenotype))
        save_a_list_graph(edge_numbers, 'Edge Number', a_path, 'edge_number.png')
