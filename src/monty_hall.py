"""
Author: Mohammad Amin Kazemi
Date: 2026-05-28
Description: This script simulates the Monty Hall problem, where a player chooses 
one of three doors, behind one of which is a car and behind the other two are goats. 
The host, who knows what's behind the doors, opens one of the remaining doors to 
reveal a goat. The player then has the option to switch to the other unopened door 
or stick with their original choice. The script simulates multiple games to calculate 
the probabilities of winning by switching or sticking with the original choice.
"""

import random
from typing import Tuple


def monty_hall_game(switch_doors: bool) -> bool:
    """Simulate a single round of the Monty Hall game.

    This function utilizes set operations to elegantly model the host's logic
    of opening a remaining door and the player's logic of switching.

    :param switch_doors: Determines if the player changes their initial choice.
    :type switch_doors: bool
    :return: ``True`` if the player wins the car, ``False`` otherwise.
    """
    car_door = random.randint(0, 2)
    initial_choice = random.randint(0, 2)

    if not switch_doors:
        return initial_choice == car_door

    # The host opens a door that is not the car and not the initial choice.
    available_for_host = {0, 1, 2} - {initial_choice, car_door}
    host_opened = random.choice(list(available_for_host))

    # The player switches to the only remaining closed door.
    final_choice = ({0, 1, 2} - {initial_choice, host_opened}).pop()
    
    return final_choice == car_door


def simulate_games(num_games: int, switch_doors: bool) -> Tuple[float, float]:
    """Simulate multiple Monty Hall games and calculate the win/loss probabilities.

    Utilizes a generator expression and the built-in sum() function for a more
    Pythonic and efficient calculation of total wins.

    :param num_games: The number of game iterations to simulate.
    :param switch_doors: Determines if the simulated player switches doors.
    :return: A tuple containing the win probability and loss probability.
    """
    # In Python, True evaluates to 1 and False to 0. 
    # We can sum a generator expression to get the total number of wins quickly.
    wins = sum(monty_hall_game(switch_doors) for _ in range(num_games))
    
    win_rate = wins / num_games
    loss_rate = 1.0 - win_rate
    
    return win_rate, loss_rate


if __name__ == "__main__":
    games_to_play = 1_000_000

    # Simulate without switching
    stay_wins, stay_losses = simulate_games(games_to_play, switch_doors=False)
    print(f"Not switching doors: Wins: {stay_wins:.2%}, Losses: {stay_losses:.2%}")

    # Simulate with switching
    switch_wins, switch_losses = simulate_games(games_to_play, switch_doors=True)
    print(f"Switching doors: Wins: {switch_wins:.2%}, Losses: {switch_losses:.2%}")
