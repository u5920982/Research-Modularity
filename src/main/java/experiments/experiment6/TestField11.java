package experiments.experiment6;

import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by Zhenyue Qin (秦震岳) on 8/7/17.
 * The Australian National University.
 */
public class TestField11 {
    public static void main(String[] args) {
        final int crossIndex = 5;
        final int matrixSideSize = 10;
        for (int currentCrossIndex=crossIndex; currentCrossIndex<matrixSideSize; currentCrossIndex++) {
            int tmpCrossIndex = currentCrossIndex;
            while (tmpCrossIndex < matrixSideSize * matrixSideSize) {
                System.out.println(tmpCrossIndex);
                tmpCrossIndex += matrixSideSize;
            }
        }
    }
}