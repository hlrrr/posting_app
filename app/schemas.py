'''  VALIDATION ERROR WARING
schema inheritance or with config > response_model > ex)fields.exclude, validation error possibility
'''
from pydantic   import BaseModel, EmailStr, SecretStr, conint
from datetime   import datetime
from enum   import Enum

from app.models import Post


class Vote(BaseModel):
    post_id: int
    direction: conint(le=1)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenInfo(BaseModel):
    id: int|None
    # create_at: datetime


class SnsType(str, Enum):
    email: str = "email"
    facebook: str = "facebook"
    google: str = "google"
    kakao: str = "kakao"


class UserBase(BaseModel):
    email: EmailStr
    password: str
    
    
class UserInfo(UserBase):
    id: int
    create_at: datetime
    updated_at: datetime|None
    password: SecretStr   # field.exclude로 대체

    class Config:
        orm_mode = True
        # fields = {'password': {'exclude': True}}

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        orm_mode = True

class PostInfo(PostBase):
    id: int
    create_at: datetime
    updated_at: datetime|None
    owner_id: int
    owner: UserInfo
    
    class Config:
        orm_mode = True
    # to support models that map to ORM objects
    # response_model로 설정시 필요. 
    # DB에는 들어가지만, response body 표시에 문제. 
    # 상속한 클래스에도 영향.
    # https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode
    # https://docs.pydantic.dev/latest/usage/models/#orm-mode-aka-arbitrary-class-instances


class PostLikey(BaseModel):
    Post: PostInfo      # _asdict()로 필드명 확인 후 선언. -> {'Post': <app.models.Post object at 0x1065089d0>, 'likey': 2}
    likey: int

    class Config:
        orm_mode = True