import pytest

from labeling_solver import __version__
from labeling_solver.solver.label_solver import solve_labeling_problem


def test_version():
    assert __version__ == '0.1.0'


def test_solve_labeling_problem():
    example_file = "/home/pedro/Dropbox/Teste Mercado Livre/Q2/labeling-solver/tests/input001.json"

    print(solve_labeling_problem(example_file))

    assert True
