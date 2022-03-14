from typing import List

from labeling_solver.input.initializer import build_graph, read_input


def solve_labeling_problem(input_file: str) -> List[int]:

    problem_data = read_input(input_file)
    g = build_graph(problem_data)

#     g.draw_graph()

    mis = g.mis()

    return mis
