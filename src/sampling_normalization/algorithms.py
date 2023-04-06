from typing import Callable


def inv_value(f: Callable, target_value: float, min_guess: float, max_guess: float, num_guesses: int = 50) -> float:
    x_guess = (max_guess + min_guess)/2
    for _ in range(num_guesses):
        guess_value = f(x_guess)
        if guess_value < target_value:
            min_guess = x_guess
            x_guess = (max_guess + x_guess)/2
        else:
            max_guess = x_guess
            x_guess = (min_guess + x_guess)/2

    return x_guess





