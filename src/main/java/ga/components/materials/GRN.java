package ga.components.materials;

import ga.components.genes.EdgeGene;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Zhenyue Qin on 22/04/2017.
 * The Australian National University.
 */
public class GRN extends EdgeMaterial {

    /**
     * Constructs a SimpleMaterial by a list of genes.
     *
     */
    public GRN(List<EdgeGene> edgeList) {
        super(edgeList);
    }


    @Override
    public GRN copy() {
        List<EdgeGene> strand = new ArrayList<>(size);
        for (int i = 0; i < size; i++)
            strand.add((EdgeGene)this.strand[i].copy());
        return new GRN(strand);
    }
}