from sqlalchemy import create_engine, text
from env_var import passw, user, db
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"mysql+pymysql://{user}:{passw}@localhost/{db}", echo=True)
SessionLocal =  sessionmaker(bind=engine)
Base = declarative_base()
