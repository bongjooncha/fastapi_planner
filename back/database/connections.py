from sqlmodel import create_engine, SQLModel, Session
from models.events import Event

db = "sqlite" #sqlite, mysql
if db == "sqlite":
    database_file = "database.db"
    database_connection_string = f"sqlite:///{database_file}"
    connect_args = {"check_same_thread": False}
    engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)
else:
    database_connection_string = "mysql://root:1234@localhost/fastapi"
    engine_url = create_engine(database_connection_string, echo=True)


def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
