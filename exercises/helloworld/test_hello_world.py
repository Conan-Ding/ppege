from unittest.mock import patch, call
from hello_world import main


def test_main_prints_hello_world_and_greeting():
    # patch("builtins.input") simulates the user typing "Alice"
    # patch("builtins.print") captures all print() calls so we can inspect them
    with patch("builtins.input", return_value="Alice"), \
         patch("builtins.print") as mock_print:
        main()

    # Assert the two print() calls happened in the correct order
    mock_print.assert_has_calls([
        call("Hello, world!"),
        call("Hello, Alice"),
    ])


def test_main_asks_for_name():
    with patch("builtins.input", return_value="Bob") as mock_input, \
         patch("builtins.print"):
        main()

    # Assert input() was called with the expected prompt
    mock_input.assert_called_once_with("What is your name? ")
