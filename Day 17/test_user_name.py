import random
from user_name import user_name

def test_user_name_generator(monkeypatch):
    # Mock the user input to return "Gabriel"
    monkeypatch.setattr('builtins.input', lambda _: "Gabriel")
    monkeypatch.setattr(random, 'randint', lambda a, b: 7)

    result = user_name()

    assert result == "leirbaG7"


def test_user_name_with_different_input(monkeypatch):
    
    monkeypatch.setattr('builtins.input', lambda _: "Ben")
    monkeypatch.setattr(random, 'randint', lambda a, b: 0)

    result = user_name()

    assert result == "neB0"

