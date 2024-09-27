from fastapi import FastAPI, Depends, HTTPException, status
from .routers import transactions
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional

# 비밀 키, 알고리즘, 만료 시간 설정
SECRET_KEY = "f33dde7bee16a2a741b4cb125d62f7547d4723a06f8a031eab0130e854d2dc41"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions.router)

# 패스워드 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 사용자 모델
class User:
    def __init__(self, username: str):
        self.username = username

class UserInDB(User):
    def __init__(self, username: str, hashed_password: str):
        super().__init__(username)
        self.hashed_password = hashed_password

# 사용자 DB (테스트 용도)
fake_users_db = {
    "testuser": UserInDB(username="testuser", hashed_password=pwd_context.hash("password123")),
}

# 패스워드 확인 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 사용자 가져오기 함수
def get_user(db, username: str):
    if username in db:
        return db[username]

# JWT 생성 함수
def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 로그인 엔드포인트
@app.post("/token")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = get_user(fake_users_db, form.username)
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# 예제 보호된 엔드포인트
@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"username": username}

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Finance App!"}