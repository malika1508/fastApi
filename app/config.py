from pydantic import BaseSettings

class SettingsConfig(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    DATABASE_URL :str
    DB_USER : str
    DB_PASSWORD : str 
    DB_NAME : str 
    DB_HOST : str 
    
    class Config:
        env_file = ".env"
