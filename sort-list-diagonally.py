def sort_diagonally(matrix):
    matrix_length = len(matrix)
    sub_matrix_length = len(matrix[0])
    diagonals_counter = {}

    for key, sub_matrix in enumerate(matrix):
      diagonals = []
      outer_diagonals = []

      diagonals_counter[key] = []
      
      for sub_key, sub_element in reversed(list(enumerate(sub_matrix))):

        list_counter = key

        next_diagonal_index = sub_key - sub_matrix_length
          
        while next_diagonal_index < 0:

          if list_counter < matrix_length:
            diagonal = matrix[list_counter][next_diagonal_index]
            diagonals.append(diagonal)

          next_diagonal_index += 1
          list_counter += 1
        
        outer_diagonals = sorted(diagonals)

        if key == 0:
          diagonals_counter[key].append(outer_diagonals)
        diagonals = []

      if key != 0:
        diagonals_counter[key].append(outer_diagonals)
      outer_diagonals = []
    
    show_diagonals = []
    for key, values in diagonals_counter.items():
      diagonals = list(diagonals_counter.values())
      diagonals = diagonals[0:key + 1]
      current = []
      for i, diagonal in enumerate(diagonals):
        index = key - i
        if index >= len(diagonal):
          that = diagonal[:index]
        else:
          that = diagonal[index:]
        for d_key, d_value in enumerate(that):
          if index < len(d_value):
            current.append(d_value[index])
      show_diagonals.append(list(reversed(current)))
    
    return show_diagonals
