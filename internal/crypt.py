from passlib.context import CryptContext
from jose import jwt

from config import get_settings

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def encode_jwt(data_to_encode: dict):
    return jwt.encode(data_to_encode, settings.token_secret_key, algorithm=ALGORITHM)


def decode_jwt(token: str):
    return jwt.decode(token, settings.token_secret_key, algorithms=[ALGORITHM])