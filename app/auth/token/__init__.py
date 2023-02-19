""" Token Encoder and Decoder """

import os
import jwt
from dotenv import load_dotenv

load_dotenv()


def generate_token(user_id):
    """ Generate an encoded token """
    secret = os.getenv("JWT_SECRET")
    encoded_token = jwt.encode({"auth": True, "user_id": user_id}, secret, algorithm="HS256")
    return encoded_token


def decode_token(token):
    """ Decode a token """
    secret = os.getenv("JWT_SECRET")
    token_data = jwt.decode(token, secret, algorithms=["HS256"])
    return token_data
