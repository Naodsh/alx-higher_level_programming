#!/usr/bin/python3
"""
N Queens puzzle
"""

import sys


class NQueens:

    """
    Class to solve the N Queens problem.
    """

    def __init__(self, n):
        """
        Initialize the NQueens object.

        Parameters:
        - n (int): The size of the chessboard and the number of queens.
        """
        self._n = 0  # Private attribute
        self.n = n
        self._solution = []

    @property
    def n(self):
        """
        Getter method for the 'n' attribute.

        Returns:
        - int: The size of the chessboard and the number of queens.
        """
        return self._n

    @n.setter
    def n(self, value):
        """
        Setter method for the 'n' attribute.

        Parameters:
        - value (int): The new value for the 'n' attribute.

        Raises:
        - ValueError: If the value is not an integer or is less than 4.
        """
        if not isinstance(value, int):
            raise ValueError("N must be a number")
        if value < 4:
            raise ValueError("N must be at least 4")
        self._n = value

    @property
    def solution(self):
        """
        Getter method for the 'solution' attribute.

        Returns:
        - list: List of solutions for the N Queens problem.
        """
        return self._solution

    def is_safe(self, row, col, placed_queens):
        """
        Check if placing a queen at a given position is safe.

        Parameters:
        - row (int): The row to check.
        - col (int): The column to check.
        - placed_queens (list): List of queens already placed.

        Returns:
        - bool: True if it's safe to place a queen, False otherwise.
        """
        for queen in placed_queens:
            if queen[1] == col or \
               queen[0] + queen[1] == row + col or \
               queen[0] - queen[1] == row - col:
                return False
        return True

    def solve(self, row, placed_queens):
        """
        Recursively solve the N Queens problem.

        Parameters:
        - row (int): The current row to consider.
        - placed_queens (list): List of queens already placed.
        """
        if row == self.n:
            self.solution.append(list(placed_queens))
            return

        for col in range(self.n):
            if self.is_safe(row, col, placed_queens):
                placed_queens.append([row, col])
                self.solve(row + 1, placed_queens)
                placed_queens.pop()

    def print_solution(self):
        """Print all solutions found for the N Queens problem."""
        for solution in self.solution:
            print(solution)


def main():

    """
    Main function to handle command line arguments and execute the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    try:
        n_queens = NQueens(n)
        n_queens.solve(0, [])
        n_queens.print_solution()
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
