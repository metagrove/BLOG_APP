from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from blog import JWT_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    

    return JWT_token.verify_token(JWT_token,credentials_exception)
