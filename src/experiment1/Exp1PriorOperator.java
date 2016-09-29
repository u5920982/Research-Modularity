package experiment1;

import com.sun.istack.internal.NotNull;
import ga.collections.Individual;
import ga.collections.Population;
import ga.collections.PopulationMode;
import ga.components.chromosome.SimpleHaploid;
import ga.operations.mutator.ChromosomeMutator;
import ga.operations.priorOperators.PriorOperator;
import ga.operations.selectors.Selector;

import java.util.List;

/**
 * Created by david on 31/08/16.
 */
public class Exp1PriorOperator implements PriorOperator<SimpleHaploid> {

    private int numOfElites;
    private Selector selector;
    private ChromosomeMutator<SimpleHaploid> chromosomeMutator = null;

    public Exp1PriorOperator(final int numOfElites, Selector selector) {
        if (numOfElites < 1)
            throw new IllegalArgumentException("Number of elites must be a positive integer.");
        this.numOfElites = numOfElites;
        this.selector = selector;
    }

    @Override
    public void preOperate(@NotNull Population<SimpleHaploid> population) {
        population.setMode(PopulationMode.PRIOR);
        /*
        List<Integer> indices = new ArrayList<>(numOfElites);
        List<Double> fitnessValues = population.getFitnessValuesView();
        List<Individual<SimpleHaploid>> individuals = population.getIndividualsView();
        while (indices.size() < numOfElites) {
            final int index = selector.select(fitnessValues);
            if (!indices.contains(index)) indices.add(index);
        }
        System.out.println(indices);
        */
        List<Individual<SimpleHaploid>> individuals = population.getIndividualsView();
        for (int i = 0; i < 20; i++) population.addCandidate(individuals.get(i));
    }

    private void mutate(@NotNull final List<Individual<SimpleHaploid>> mutant,
                        @NotNull final ChromosomeMutator<SimpleHaploid> chromosomeMutator) {
        chromosomeMutator.mutate(mutant);
    }

    public int getNumOfElites() {
        return numOfElites;
    }

    public void setNumOfElites(int numOfElites) {
        this.numOfElites = numOfElites;
    }

    public void setSelector(Selector selector) {
        this.selector = selector;
    }

    public void setChromosomeMutator(final ChromosomeMutator<SimpleHaploid> chromosomeMutator) {
        this.chromosomeMutator = chromosomeMutator;
    }
}
