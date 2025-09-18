import re #re は「regular expression（正規表現）」の略 
def is_valid_email(email: str) -> bool:
    """
    メールアドレスが簡易的に正しい形式かどうか判定する関数
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None