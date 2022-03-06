import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple


class Graph:
    def __init__(self, size: int) -> None:
        self.size = size

        self.g: List[int] = []
        self.adj_list: Dict[int, Dict[int, int]] = {}
        self.adj_binrep: List[int] = [0 for _ in range(size+1)]

    def add_edge(self, u, v) -> None:
        if u not in self.g:
            self.g.append(u)

        if v not in self.g:
            self.g.append(v)

        if u not in self.adj_list:
            self.adj_list[u] = dict()

        if v not in self.adj_list[u]:
            self.adj_list[u][v] = 1

        self.adj_binrep[u] |= 1 << v


    def draw_graph(self) -> None:
        G = nx.Graph(self.adj_list)
        nx.draw_networkx(G)
        plt.show()


    def max_clique(self) -> Tuple[int, int]:

        g_comp = [self.adj_binrep[i] ^ ((1 << (self.size))-1) for i in range(self.size)]

        max_clique_by_subset = [0 for _ in range(1 << self.size)]

        half_size = self.size // 2
        all_vertices_mask = (1 << self.size) - 1

        for mask in range(1 << half_size):
            adjacency = all_vertices_mask

            for i in range(half_size):
                if adjacency & (1 << i):
                    adjacency &= g_comp[i]

            if adjacency & mask == mask:
                max_clique_by_subset[mask] = mask.bit_count()

        for mask in range(1 << half_size):
            for i in range(half_size):
                mask_plus_i = mask | (1 << i)
                max_clique_by_subset[mask_plus_i] = max(
                    max_clique_by_subset[mask_plus_i], max_clique_by_subset[mask]
                )

        max_clique = 0
        max_clique_number = 0

        for mask in range(0, 1 << self.size, 1 << half_size):
            adjacency = all_vertices_mask

            for i in range(half_size, self.size):
                if mask & 1 << i:
                    adjacency &= g_comp[i]

            # checks if the subgraph is a clique
            if adjacency & mask == mask:
                other_half_subset = adjacency & ((1 << half_size) - 1)
                merged_clique_size = mask.bit_count() + max_clique_by_subset[other_half_subset]

                if max_clique_number < merged_clique_size:
                    max_clique_number = merged_clique_size
                    max_clique = adjacency

        return max_clique, max_clique_number

    def mis(self) -> List[int]:
        mis_vertices = list()

        mis, mis_size = self.max_clique()

        for i in range(0, self.size+1):
            if mis & (1 << i):
                mis_vertices.append(i)

        return mis_vertices
