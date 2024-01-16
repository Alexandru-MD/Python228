import pytest


@pytest.fixture(autouse=True)
def clean_text():
    with open('test/test_file.txt', 'w'):
        pass
