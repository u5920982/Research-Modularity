package experiments.exp3_larson_work_reproduction;

import ga.collections.DetailedStatistics;
import ga.collections.Population;
import ga.components.chromosomes.SimpleHaploid;
import ga.frame.frames.Frame;
import ga.frame.frames.SimpleHaploidFrame;
import ga.frame.states.SimpleHaploidState;
import ga.frame.states.State;
import ga.operations.fitnessFunctions.FitnessFunction;
import ga.operations.fitnessFunctions.GRNFitnessFunctionMultipleTargetsFast;
import ga.operations.initializers.HaploidGRNInitializer;
import ga.operations.initializers.Initializer;
import ga.operations.mutators.GRNEdgeMutator;
import ga.operations.mutators.Mutator;
import ga.operations.postOperators.PostOperator;
import ga.operations.postOperators.SimpleFillingOperatorForNormalizable;
import ga.operations.priorOperators.PriorOperator;
import ga.operations.priorOperators.SimpleElitismOperator;
import ga.operations.reproducers.Reproducer;
import ga.operations.reproducers.GRNHaploidMatrixFixedXReproducer;
import ga.operations.selectionOperators.selectionSchemes.SimpleTournamentScheme;
import ga.operations.selectionOperators.selectors.Selector;
import ga.operations.selectionOperators.selectors.SimpleTournamentSelector;

import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

/**
 * Created by Zhenyue Qin on 23/04/2017.
 * The Australian National University.
 */
public class HaploidGRN2Target10MatrixLarsonSPXMain {
    /* The two targets that the GA evolve towards */
    private static final int[] target1 = {
            1, -1, 1, -1, 1,
            -1, 1, -1, 1, -1
    };
    private static final int[] target2 = {
            1, -1, 1, -1, 1,
            1, -1, 1, -1, 1
    };

    /* Parameters of the GRN */
    private static final int maxCycle = 20;
    private static final int edgeSize = 20;
    private static final int perturbations = 300;
    private static final double perturbationRate = 0.15;
    private static final int perturbationCycleSize = 300;

    /* Parameters of the GA */
    private static final double geneMutationRate = 0.05;
    private static final int numElites = 10;
    private static final int populationSize = 100;
    private static final int tournamentSize = 3;
    private static final double reproductionRate = 0.9;
    private static final int maxGen = 1050;
    private static final List<Integer> thresholds = Arrays.asList(0, 300);

    /* Settings for text outputs */
    private static final String summaryFileName = "Haploid-GRN-2-Target-10-Matrix-Larson-Fixed-Point.txt";
    private static final String csvFileName = "Haploid-GRN-2-Target-10-Matrix-Larson-Fixed-Point.csv";
    private static final String outputDirectory = "haploid-grn-2-target-10-matrix-larson-fixed-point";
    private static final String mainFileName = "HaploidGRN2Target10MatrixLarsonSPXMain.java";
    private static DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss");
    private static Date date = new Date();

    /* Settings for graph outputs */
    private static final String plotTitle = "Haploid GRN 2 Target 10 Matrix Larson Fixed Point";
    private static final String plotFileName = "Haploid-GRN-2-Target-10-Matrix-Larson-Fixed-Point.png";

    public static void main(String[] args) throws IOException {
        int[][] targets = {target1, target2};

        /* Fitness function */
        FitnessFunction fitnessFunction = new GRNFitnessFunctionMultipleTargetsFast(
                targets, maxCycle, perturbations, perturbationRate, thresholds, perturbationCycleSize);

        /* It is not necessary to write an initializer, but doing so is convenient to
        repeat the experiment using different parameter */
        Initializer<SimpleHaploid> initializer = new HaploidGRNInitializer(populationSize, target1.length, edgeSize);

        /* Population */
        Population<SimpleHaploid> population = initializer.initialize();

        /* Mutator for chromosomes */
        Mutator mutator = new GRNEdgeMutator(geneMutationRate);

        /* Selector for reproduction */
        Selector<SimpleHaploid> selector = new SimpleTournamentSelector<>(tournamentSize);

        /* Selector for elites */
        PriorOperator<SimpleHaploid> priorOperator = new SimpleElitismOperator<>(numElites);

        /* PostOperator is required to fill up the vacancy */
        PostOperator<SimpleHaploid> postOperator = new SimpleFillingOperatorForNormalizable<>(
                new SimpleTournamentScheme(tournamentSize));

        /* Reproducer for reproduction */
        Reproducer<SimpleHaploid> reproducer = new GRNHaploidMatrixFixedXReproducer(target1.length, 8);

        /* Statistics for keeping track the performance in generations */
        DetailedStatistics<SimpleHaploid> statistics = new DetailedStatistics<>();

        /* The state of an GA */
        State<SimpleHaploid> state = new SimpleHaploidState<>(
                population, fitnessFunction, mutator, reproducer, selector, 2, reproductionRate);
        state.record(statistics);

        /* The frame of an GA to change states */
        Frame<SimpleHaploid> frame = new SimpleHaploidFrame<>(state,postOperator,statistics, priorOperator);

        /* Set output paths */
        statistics.setDirectory(outputDirectory + "/" + dateFormat.format(date));
        statistics.copyMainFile(mainFileName, System.getProperty("user.dir") +
                "/src/main/java/experiments/exp3_larson_work_reproduction/" + mainFileName);

        statistics.print(0); // print the initial state of an population
        /* Actual GA evolutions */
        for (int i = 1; i <= maxGen; i++) {
            frame.evolve();
            statistics.print(i);
        }

        /* Generate output files */
        statistics.save(summaryFileName);
        statistics.generateNormalCSVFile(csvFileName);
        statistics.generatePlot(plotTitle, plotFileName);
    }
}
