import numpy as np
import math as math

def calculate(list):

    # Create numpy array
    row_1st = [list[0], list[1], list[2]]
    row_2nd = [list[3], list[4], list[5]]
    row_3rd = [list[6], list[7], list[8]]
    matrix = [[row_1st], [row_2nd], [row_3rd]]
    array = np.array(matrix)

    # Create lists for the mean, variance, standard deviation, maximums, minimums and sums.
    # The lists will have the column values in the zeroth index, row values in the first and the flattened values in the second index.
    means = []
    means.append(array.mean(0).tolist()[0])
    means.append([array.mean(2).tolist()[0][0], array.mean(2).tolist()[1][0], array.mean(2).tolist()[2][0]])
    means.append(array.mean())

    vars = []
    vars.append(np.var(array, axis=0).tolist()[0])
    vars.append([np.var(array, axis=2).tolist()[0][0], np.var(array, axis=2).tolist()[1][0], np.var(array, axis=2).tolist()[2][0]])
    vars.append(np.var(array).tolist())

    stds = []
    stds.append([math.sqrt(vars[0][0]), math.sqrt(vars[0][1]), math.sqrt(vars[0][2])])
    stds.append([math.sqrt(vars[1][0]), math.sqrt(vars[1][1]), math.sqrt(vars[1][2])])
    stds.append(math.sqrt(vars[2]))

    maxs = []
    maxs.append(np.max(array, 0).tolist()[0])
    maxs.append([np.max(array, axis=2).tolist()[0][0], np.max(array, axis=2).tolist()[1][0], np.max(array, axis=2).tolist()[2][0]])
    maxs.append(np.max(array))

    mins = []
    mins.append(np.min(array, 0).tolist()[0])
    mins.append([np.min(array, axis=2).tolist()[0][0], np.min(array, axis=2).tolist()[1][0], np.min(array, axis=2).tolist()[2][0]])
    mins.append(np.min(array))

    sums = []
    sums.append(np.sum(array, 0).tolist()[0])
    sums.append([np.sum(array, axis=2).tolist()[0][0], np.sum(array, axis=2).tolist()[1][0], np.sum(array, axis=2).tolist()[2][0]])
    sums.append(np.sum(array))

    # Create dictionary from the previous lists
    dict = {
        'mean': [means[0], means[1], means[2]],
        'variance': [vars[0], vars[1], vars[2]],
        'standard deviation': [stds[0], stds[1], stds[2]],
        'max': [maxs[0], maxs[1], maxs[2]],
        'min': [mins[0], mins[1], mins[2]],
        'sum': [sums[0], sums[1], sums[2]]
    }

    return dict

def main():
    # Input the list here
    test_matrix = [0,1,2,3,4,5,6,7,8]
    dict = calculate(test_matrix)
    print(dict)

if __name__ == "__main__":
    main()