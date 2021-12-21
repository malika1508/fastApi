from pydantic import BaseSettings

class SettingsConfig(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    DB_USER : str
    DB_PWD : str 
    DB_NAME : str 
    DOMAINE : str 
    
    class Config:
        env_file = ".env"
