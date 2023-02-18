import pytest
import os
from app import create_app
import dotenv

dotenv.load_dotenv()


@pytest.fixture()
def app():
    os.environ["TESTING"] = "true"
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()