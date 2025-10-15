from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated ="auto")

class HASH:
    
    def Bcypt(password : str):
        password_bytes = password.encode("utf-8")
        # Truncate to 72 bytes (bcrypt limit)
        truncated_bytes = password_bytes[:72]
        # Decode back to str safely for passlib
        safe_password = truncated_bytes.decode("utf-8", "ignore")
        return pwd_cxt.hash(safe_password)
        # t_password=password[:72]
        # return pwd_cxt.hash(t_password)
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)