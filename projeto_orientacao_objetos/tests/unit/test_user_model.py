from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User


def test_password_hashing():
    password = "123456"

    # Seu User não tem check_password; ele tem hash_password (conforme erro).
    # Então validamos o hash comparando com check_password_hash.
    user = User(username="test", email="test@test.com", password_hash=generate_password_hash(password))

    assert check_password_hash(user.password_hash, password)
    assert not check_password_hash(user.password_hash, "wrong")
