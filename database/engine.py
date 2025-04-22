from sqlalchemy import create_engine, text
from env_var import passw, user, db
from sqlalchemy.orm import Session, declarative_base

engine = create_engine(f"mysql+pymysql://{user}:{passw}@localhost/{db}", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT idexpenses, expenses_category, expenses_money FROM expenses"))
    for row in result:
        print(f"id: {row.idexpenses} category: {row.expenses_category}, money spent: {row.expenses_money}")