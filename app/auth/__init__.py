
from app.auth.token import generate_token
from app.db.models import User
from app.db import db
from app.db.models import User


def user_login(username, password):
    """implementation starts here"""

    email_exists = User.query.filter_by(email=username).first()
    username_exists = User.query.filter_by(username=username).first()

    msg = {}

    if email_exists is not None:
        if email_exists.check_password(password):
            user_id = email_exists.get_id()
            msg["msg"] = "success"
            msg["token"] = generate_token(user_id)
        else:
            msg["err_msg"] = "wrong credentials"
    elif username_exists is not None:
        if username_exists.check_password(password):
            user_id = username_exists.get_id()
            msg["msg"] = "success"
            msg["token"] = generate_token(user_id)
        else:
            msg["err_msg"] = "wrong credentials"
    elif email_exists is None:
        msg["err_msg"] = "wrong credentials"
    elif username_exists is None:
        msg["err_msg"] = "wrong credentials"

    return msg


def user_registration(email, username, password):
    email_exists = User.query.filter_by(email=email).first()
    username_exists = User.query.filter_by(username=username).first()

    user = User(email=email, username=username, password=password)

    msg = {}

    if email_exists is not None:
        msg["err_msg"] = "email exists"
    elif username_exists is not None:
        msg["err_msg"] = "username exists"
    else:
        db.session.add(user)
        db.session.commit()
        msg["msg"] = "success"

    return msg


