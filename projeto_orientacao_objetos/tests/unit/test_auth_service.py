from app.services import AuthService
from app.repositories import UserRepository, JSONStorage


def test_register_and_login(tmp_path):
    storage = JSONStorage(tmp_path / "users.json")
    repo = UserRepository(storage)
    service = AuthService(repo)

    user = service.register("user1", "u1@test.com", "123456")
    assert user.username == "user1"

    logged = service.login("user1", "123456")
    assert logged is not None
