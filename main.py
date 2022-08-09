import sys

from munkres import Munkres, print_matrix

m = Munkres()

# hun algor
# class hun_algor():
#     def hun_algor_1():
#         matrix = [[5, 9, 1],
#                   [10, 3, 2],
#                   [8, 7, 4]]
#         indexes = m.compute(matrix)
#         print_matrix(matrix, msg='Lowest cost through this matrix:')    
matrix = [[5, 9, 1],
                [10, 3, 2],
                [8, 7, 4]]        

# sol = hun_algor()
# ans = sol.hun_algor_1()
# print(ans)
class hun_algor():
    def __init__(self) -> None:
        pass
    def best_cost() -> None:
        
        print('------------')
        print(matrix)
        print(type(matrix))
        print('------------')
        m = Munkres()
        indexes = m.compute(matrix)
        print_matrix(matrix, msg='Lowest cost through this matrix:')
        total = 0
        for row, column in indexes:
            value = matrix[row][column]
            total += value
            print(f'({row}, {column}) -> {value}')
        print(f'total cost: {total}')
        

    def best_profit() -> None:
        
        cost_matrix = []
        for row in matrix:
            cost_row = []
            for col in row:
                cost_row += [sys.maxsize - col]
            cost_matrix += [cost_row]

        indexes = m.compute(cost_matrix)
        print_matrix(matrix, msg='Highest profit through this matrix:')
        total = 0
        for row, column in indexes:
            value = matrix[row][column]
            total += value
            print(f'({row}, {column}) -> {value}')

        
        print(f'total cost: {total}')
    
    best_cost()
    best_profit()
        
if __name__ == "main":
    hun_algor()
        
        
# sol.
# sol.
