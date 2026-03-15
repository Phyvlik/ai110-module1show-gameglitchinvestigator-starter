from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and the hint should say to lower the guess
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and the hint should say to raise the guess
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")
