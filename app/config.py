from pydantic   import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    database_url: str
    database_url_alembic:str
    secrete_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file = ".env"

settings = Settings()


class Settings_test(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    database_url: str
    database_url_alembic:str
    secrete_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file = ".env_test"

settings_test = Settings_test()