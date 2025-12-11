import os
import tempfile
import pytest

from app import create_app


@pytest.fixture
def app():
    tmpdir = tempfile.TemporaryDirectory()
    os.environ["APP_DATA_DIR"] = tmpdir.name

    app = create_app()
    app.config.update(TESTING=True, SECRET_KEY="test-secret")

    yield app
    tmpdir.cleanup()


@pytest.fixture
def client(app):
    return app.test_client()
