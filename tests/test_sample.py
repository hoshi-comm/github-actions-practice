from src.sample import add
# assert だけのシンプルなテストなら import pytest は不要

def test_add():
    assert add(2, 3) == 5