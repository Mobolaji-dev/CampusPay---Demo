from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    NOMBA_CLIENT_ID:str
    NOMBA_PRIVATE_KEY:str
    NOMBA_ACCOUNT_ID:str
    NOMBA_BASE_URL:str
    DATABASE_URL:str
    SECRET_KEY:str

    class Config:
        env_file= ".env"

settings=Settings()