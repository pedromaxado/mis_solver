import pytest

from labeling_solver import __version__
from labeling_solver.solver.label_solver import solve_labeling_problem


def test_version():
    assert __version__ == '0.1.0'


def test_solve_labeling_problem():
    current_dir = os.path.dirname(__file__)
    example_file = "input001.json"
    example_path = os.path.join(current_dir, example_file)
    print(solve_labeling_problem(example_path))

    assert True
