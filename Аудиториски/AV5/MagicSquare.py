from constraint import *


if __name__ == "__main__":

    problem = Problem()

    variables = range(0, 16)
    domain = range(1, 17)

    problem.addVariables(variables, domain)

    problem.addConstraint(AllDifferentConstraint(), variables)


    """
    
    0  1  2   3
    4  5  6   7
    8  9  10 11
    12 13 14 15
    """

    #check all the rows if their sum is exactly 34
    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range (4)])

    # check all the columns if their sum is exactly 34
    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34), [col + 4 * i for i in range(4)])

    # check for the sum of the main diagonal
    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))

    # check for the sum of the opposite diagonal
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

    solution = problem.getSolution()

    print(solution)
