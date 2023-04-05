




def inv_value(f, target_value: float, min_guess: float, max_guess: float, num_guesses: int = 50):
    x_guess = (max_guess + min_guess)/2
    for _ in range(num_guesses):
        guess_value = f(x_guess)
        x_guess = (max_guess + x_guess)/2 if guess_value < target_value else (min_guess + x_guess)/2
    return x_guess





