package ga.operations.fitnessFunctions;

import ga.components.materials.Material;
import org.jetbrains.annotations.NotNull;

/*
    GASEE is a Java-based genetic algorithm library for scientific exploration and experiment.
    Copyright 2016 Siu-Kei Muk

    This file is part of GASEE.

    GASEE is free library: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 2.1 of the License, or
    (at your option) any later version.

    GASEE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with GASEE.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * This interface provides an abstraction for the fitness function (objective function) for genetic algorithm.
 *
 * @author Siu Kei Muk (David)
 * @since 27/08/16.
 */
public interface FitnessFunction<P extends Material> {
    /**
     * Evaluates the fitness function value of the given phenotype.
     *
     * @param phenotype phenotype of an individual
     * @return fitness function value
     */
    double evaluate(@NotNull final P phenotype);

    /**
     * Notifies the fitness function to perform pre-defined internal changes to simulate an environmental change.
     */
    void update();
}
