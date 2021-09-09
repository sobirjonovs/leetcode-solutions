# Read the description, please!

matrix = [
	[75,21,13,24,8],
	[24,100,40,49,62], 
	[45, 34, 12, 33, 54], 
	[98, 76, 99, 100, 1]
]

def sort_diagonally(matrix):
    current_iteration = 0
    iterations = 0
    mats = list(enumerate(matrix))
    sub_matrix = mats[current_iteration][1]
    index = len(sub_matrix) - 1
    diagonals_finder = {}

    while True:

        if (len(mats) * len(sub_matrix)) == iterations:
            break

        if index == -1:
            current_iteration += 1
            sub_matrix = mats[current_iteration][1]
            index = len(sub_matrix) - 1

        head_value = sub_matrix[index]
        current_list = mats[current_iteration][0] + 1
        diagonals_count = len(mats) - index

        if current_list > index:
            diagonals_count = diagonals_count - (current_list - index)

        if iterations < len(sub_matrix) or index + iterations == iterations:
            c_in = f"{head_value}-{current_list - 1}-{index}"
            diagonals_finder[c_in] = []
            temp_diagonals = diagonals_count
            next_list = current_list
            next_diagonal_value = index - len(mats)
            while temp_diagonals >= 0:
                if temp_diagonals == 0:
                    diagonals_finder[c_in].insert(0, head_value)
                else:
                    diagonals_finder[c_in].append(matrix[next_list][next_diagonal_value])
                temp_diagonals -= 1
                next_list += 1
                next_diagonal_value += 1

        index -= 1
        iterations += 1

    diagonals_finder = {key: sorted(item) for key, item in diagonals_finder.items()}

    for key, item in diagonals_finder.items():
        diagonals_count = len(item)
        info = key.split('-')
        value_index = int(info.pop())
        list_index = int(info.pop())
        for i in range(diagonals_count):
            matrix[list_index][value_index] = item[i]
            list_index += 1
            value_index += 1

    return matrix

print(sort_diagonally(matrix))
