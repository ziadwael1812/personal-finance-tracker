from datetime import datetime, timedelta
from typing import Any, Union, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings
from app.schemas.token import TokenPayload # Assuming TokenPayload is in schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = settings.ALGORITHM

def create_access_token(
    subject: Union[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_token(token: str, credentials_exception) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_sub: Optional[str] = payload.get("sub")
        token_exp: Optional[int] = payload.get("exp") # type: ignore
        if token_sub is None or token_exp is None:
            raise credentials_exception
        
        # Check if token is expired - this is handled by jwt.decode as well
        # but an explicit check can be added if needed.
        # if datetime.fromtimestamp(token_exp) < datetime.utcnow():
        #     raise credentials_exception
            
        return TokenPayload(sub=token_sub, exp=token_exp)
    except JWTError:
        raise credentials_exception 