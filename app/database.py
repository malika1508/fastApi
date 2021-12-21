from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import app.config as config


# settings = config.SettingsConfig()
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{settings.DB_PWD}@{settings.DOMAINE}/{settings.DB_NAME}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = 'postgres://xldwgasuyjgjvl:5e493c6ace98b9474babdb2200228811e89578798768af8fed9adda8b0b2c01a@ec2-18-204-101-137.compute-1.amazonaws.com:5432/d7rpl0o0l5trsg'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()