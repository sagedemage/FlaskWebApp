import dotenv
import jwt
import os

dotenv.load_dotenv()


def generate_token(user_id):
    secret = os.getenv("JWT_SECRET")
    encoded_token = jwt.encode({"auth": True, "user_id": user_id}, secret, algorithm="HS256")
    return encoded_token


def decode_token(token):
    secret = os.getenv("JWT_SECRET")
    token_data = jwt.decode(token, secret, algorithms=["HS256"])
    return token_data
