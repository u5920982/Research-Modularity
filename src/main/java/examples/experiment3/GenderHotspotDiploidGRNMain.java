package examples.experiment3;

import ga.collections.DetailedGenderStatistics;
import ga.collections.Population;
import ga.components.chromosomes.GenderDiploid;
import ga.components.chromosomes.GenderHotspotDiploid;
import ga.components.hotspots.Hotspot;
import ga.frame.DiploidHotspotFrame;
import ga.frame.Frame;
import ga.frame.SimpleGenderHotspotState;
import ga.frame.State;
import ga.operations.dominanceMapMutators.DiploidDominanceMapMutator;
import ga.operations.dominanceMapMutators.ExpressionMapMutator;
import ga.operations.fitnessFunctions.FitnessFunction;
import ga.operations.fitnessFunctions.GRNFitnessFunction;
import ga.operations.hotspotMutators.HotspotMutator;
import ga.operations.hotspotMutators.RandomHotspotMutator;
import ga.operations.initializers.GenderHotspotDiploidGRNInitializer;
import ga.operations.mutators.GRNEdgeMutator;
import ga.operations.mutators.Mutator;
import ga.operations.postOperators.PostOperator;
import ga.operations.postOperators.SimpleFillingOperatorForNormalizable;
import ga.operations.priorOperators.PriorOperator;
import ga.operations.priorOperators.SimpleGenderElitismOperator;
import ga.operations.reproducers.GenderHotspotReproducer;
import ga.operations.reproducers.Reproducer;
import ga.operations.reproducers.SimpleGenderHotspotReproducer;
import ga.operations.selectionOperators.selectionSchemes.SimpleTournamentScheme;
import ga.operations.selectionOperators.selectors.Selector;
import ga.operations.selectionOperators.selectors.SimpleTournamentSelector;

import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by zhenyueqin on 15/6/17.
 */
public class GenderHotspotDiploidGRNMain {
    private static final int[] target = {-1, 1, -1, 1, -1, 1, -1, 1, -1, 1};
    private static final int maxCycle = 100;
    private static final int edgeSize = 20;
    private static final int perturbations = 300;
    private static final int hotspotSize = 9;
    private static final double geneMutationRate = 0.002;
    private static final double dominanceMutationRate = 0.001;
    private static final double hotspotMutationRate = 0.0005;
    private static final int numElites = 10;

    private static final int size = 200;
    private static final int tournamentSize = 3;
    private static final double selectivePressure = 1.0;
    private static final double reproductionRate = 0.8;
    private static final int maxGen = 1000;

    private static final double maxFit = 300;
    private static final double epsilon = .5;

    private static final int numberOfChildren = 2;

    private static final String summaryFileName = "Gender-Hotspot-Diploid-GRN.sum";
    private static final String csvFileName = "Gender-Hotspot-Diploid-GRN.csv";
    private static final String outputDirectory = "gender-hotspot-diploid-grn";
    private static DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss");
    private static Date date = new Date();

    private static final String plotTitle = "Gender Hotspot GRN Summary";
    private static final String plotFileName = "Gender-Hotspot-GRN-Chart.png";

    public static void main(String[] args) throws IOException {
        // Fitness Function
        FitnessFunction fitnessFunction = new GRNFitnessFunction(target, maxCycle, perturbations);

        // Initializer
        GenderHotspotDiploidGRNInitializer initializer = new GenderHotspotDiploidGRNInitializer(size, target, edgeSize, hotspotSize);

        // Population
        Population<GenderHotspotDiploid> population = initializer.initialize();

        // Mutator for chromosomes
        Mutator mutator = new GRNEdgeMutator(geneMutationRate);

        // Selector for reproduction
        Selector<GenderHotspotDiploid> selector = new SimpleTournamentSelector<>(tournamentSize, selectivePressure);

        PriorOperator<GenderHotspotDiploid> priorOperator = new SimpleGenderElitismOperator<>(numElites);

        PostOperator<GenderHotspotDiploid> fillingOperator = new SimpleFillingOperatorForNormalizable<>(new SimpleTournamentScheme(tournamentSize, selectivePressure));

        DetailedGenderStatistics<GenderHotspotDiploid> statistics = new DetailedGenderStatistics<>();

        ExpressionMapMutator expressionMapMutator = new DiploidDominanceMapMutator(dominanceMutationRate);

        HotspotMutator hotspotMutator = new RandomHotspotMutator(hotspotMutationRate);

        Reproducer<GenderHotspotDiploid> reproducer = new SimpleGenderHotspotReproducer(numberOfChildren);

        State<GenderHotspotDiploid> state = new SimpleGenderHotspotState<>(population, fitnessFunction, mutator,
                reproducer, selector, 2, reproductionRate, expressionMapMutator, hotspotMutator);

        state.record(statistics);

        Frame<GenderHotspotDiploid> frame = new DiploidHotspotFrame<>(state, fillingOperator, statistics, priorOperator);

        statistics.print(0);
        statistics.setDirectory(outputDirectory + "/" + dateFormat.format(date));
        for (int i = 0; i < maxGen; i++) {
            frame.evolve();
            statistics.print(i);
            if (statistics.getOptimum(i) > maxFit - epsilon) {
                break;
            }
        }
        statistics.save(summaryFileName);
        statistics.generateCSVFile(csvFileName);
        statistics.generatePlot(plotTitle, plotFileName);

    }
}
