from src.email import is_valid_email # テストしたい関数の入ったファイル名から作った関数をimportする　from 〇〇 import 〇〇
import pytest

def test_valid_emails():
    assert is_valid_email("user@example.com")
    assert is_valid_email("test.user123@domain.co.jp")

def test_invalid_emails():
    assert not is_valid_email("userexample.com")   # @がない
    assert not is_valid_email("user@.com")        # ドメイン不正
    assert not is_valid_email("user@domain")      # .がない

def test_empty_string():
    assert not is_valid_email("")

def test_non_string_input():
    with pytest.raises(TypeError):
        is_valid_email(123)  # 数値を渡したらエラーにする想定