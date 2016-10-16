package ga.operations.dominanceMap;

import com.sun.istack.internal.NotNull;
import ga.components.materials.GeneticMaterial;

import java.util.List;

/**
 * A projection mapping object returns one of the given genetic material as the phenotype.
 * It is mainly used for identity mapping for haploids.
 *
 * @author Siu Kei Muk (David)
 * @since 12/09/16.
 */
public class ProjectionMap<M extends GeneticMaterial> implements DominanceMap<M,M> {

    private int projectionIndex;

    public ProjectionMap(final int projectionIndex) {
        setProjectionIndex(projectionIndex);
    }

    private void filter(final int projectionIndex) {
        if (projectionIndex < 0)
            throw new IllegalArgumentException("Projection index must be non-negative.");
    }

    @Override
    public DominanceMap<M, M> copy() {
        return new ProjectionMap<>(projectionIndex);
    }

    @Override
    public M map(@NotNull List<M> materials) {
        return materials.get(projectionIndex);
    }

    public int getProjectionIndex() {
        return projectionIndex;
    }

    public void setProjectionIndex(final int projectionIndex) {
        filter(projectionIndex);
        this.projectionIndex = projectionIndex;
    }
}