from curses import mousemask
from typing import Dict, List, Tuple


class Graph:
    def __init__(self, size: int) -> None:
        self.size = size

        self.g: List[int] = []
        self.adj_list: Dict[int, Dict[int, int]] = {}
        self.adj_binrep: List[int] = [0 for _ in range(size)]

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

    def max_clique(self) -> Tuple[int, int]:

        g_comp = [~self.adj_binrep[i] for i in self.g]

        max_clique_by_subset = [0 for _ in range(1 << self.size)]

        half_size = self.size / 2
        all_vertices_mask = (1 << self.size) - 1

        for mask in range(1 << half_size):
            adjacency = all_vertices_mask

            for i in range(half_size):
                if adjacency & (1 << i):
                    adj &= g_comp[i]

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
        mis = list()

        mis_size, mis = self.max_clique()

        for i in range(1, self.size):
            if mis & (1 << i):
                mis.append(i)

        return mis