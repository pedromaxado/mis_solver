import json

from labeling_solver.utils.graph import Graph


def read_input(file_path: str) -> dict:
    with open(file_path) as fp:
        problem_data = json.load(fp)
        return problem_data


def build_graph(problem_data: dict) -> Graph:
    g_size = problem_data["size"]

    g = Graph(g_size)

    for u in range(1, g_size+1):
        u_adj = problem_data[u]
        
        for v in u_adj:
            g.add_edge(u, v)

    return g
