from evaluation import *
import evaluation as e


def test_average():
    assert e.average(1.0, 1.0, 1.0) == 1.0
    assert e.average(-2.5, -3.5, -1.5) == -2.5
    assert e.average(0.5, 2.3, 1.7) == 1.5


def test_game_results():
    assert e.game_results(["W", "L", "L", "T"], "T") == 1
    assert e.game_results(["W", "W", "T"], "W") == 2
    assert e.game_results(["T", "L", "L", "T"], "L") == 2


def test_sorted_game_results():
    given_list = ["W", "W", "T"]
    expected = {"W": 2, "L": 0, "T": 1}
    result = e.sorted_game_results(given_list)
    assert result == expected

    given_list = ["T", "L", "W"]
    expected = {"W": 1, "L": 1, "T": 1}
    result = e.sorted_game_results(given_list)
    assert result == expected

    given_list = ["T", "T", "T"]
    expected = {"W": 0, "L": 0, "T": 3}
    result = e.sorted_game_results(given_list)
    assert result == expected


def test_sorted_game_results_number():
    given_dict = {"W": 2, "L": 1, "T": 0}
    choice = "W"
    expected = 2
    result = e.sorted_game_results_number(given_dict, choice)
    assert result == expected

    given_dict = {"W": 0, "L": 0, "T": 0}
    choice = "L"
    expected = 0
    result = e.sorted_game_results_number(given_dict, choice)
    assert result == expected

    given_dict = {"W": 1, "L": 1, "T": 1}
    choice = "T"
    expected = 1
    result = e.sorted_game_results_number(given_dict, choice)
    assert result == expected
