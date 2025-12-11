from werkzeug.security import generate_password_hash
from app.models import User
from app.repositories import UserRepository, JSONStorage


def test_add_user(tmp_path):
    storage = JSONStorage(tmp_path / "users.json")
    repo = UserRepository(storage)

    user = User(
        username="repo",
        email="repo@test.com",
        password_hash=generate_password_hash("123456"),
    )

    repo.add(user)
    assert repo.get_by_username("repo") is not None
