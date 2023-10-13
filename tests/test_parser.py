'''This module need for test parser'''
from my_parser import get_anime_data
import pytest

@pytest.mark.parametrize(
    "link, code",
    [
        ("https://animego.org/anim", 404),
        ("https://animego.org/review/4175/new", 500),
    ]
)
def test_get_anime_data(link, code):
    '''tests for function get_anime_data'''
    assert get_anime_data(link) == code
