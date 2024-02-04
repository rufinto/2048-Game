from textual_2048 import *
from pytest import *

def test_read_player_command(monkeypatch):
    def mock_input_return(obj):
        return lambda prompt: obj
        
    monkeypatch.setattr("builtins.input", mock_input_return('g'))
    assert read_player_command() == 'g'

    monkeypatch.setattr('builtins.input', mock_input_return('d'))
    assert read_player_command() == 'd'

    monkeypatch.setattr('builtins.input', mock_input_return('h'))
    assert read_player_command() == 'h'

    monkeypatch.setattr('builtins.input', mock_input_return('b'))
    assert read_player_command() == 'b'