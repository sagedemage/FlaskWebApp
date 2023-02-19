""" Setup Unit Tests """

import os
import pytest
from dotenv import load_dotenv
from app import create_app

load_dotenv()


@pytest.fixture()
def app():
    """ Run App """
    os.environ["TESTING"] = "true"
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False
    })

    yield app


@pytest.fixture()
def client(app):
    """ Start Client """
    return app.test_client()


@pytest.fixture()
def runner(app):
    """ Start Runner """
    return app.test_cli_runner()
