from typing import List, Dict


def average(a: float, b: float, c: float) -> float:
    """Gives the average of three numbers

    Arg:
        a: float
        b: float
        c: float
    Returns:
        The average of the three numbers.
        """

    return (a + b + c)/3


def game_results(results: List[str], choice: str) -> int:
    """Gives the number of times a game result has appeared

    Arg:
        results: a list of strings showing game result
        choice: a string of which game result is desired
    Returns:
        The number of times the desired game result has
        appeared.
    """

    count = 0
    for result in results:
        if result == choice:
            count += 1

    return count


def sorted_game_results(results: List[str]) -> Dict:
    """Creates a dictionary of the results and its occurances

    Arg:
        results: a list of strings showing game results
    Returns:
        A dictionary with the result as the key and the
        number of times it appears as the value
        """

    game_results = {"W": 0, "L": 0, "T": 0}

    for result in results:
        if result in game_results.keys():
            game_results[result] += 1

    return game_results


def sorted_game_results_number(results: Dict, choice: str) -> int:
    """Gives the number of a specific game result.

    Arg:
        results: dictionary of sorted game results
        choice: string of the desired game result
    Returns:
        The integer value (number) of a specific game
        results' occurances.
    """

    return results[choice]
