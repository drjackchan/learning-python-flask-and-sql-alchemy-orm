from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

if (os.environ.get("POSTGRES_URL") is None):
    load_dotenv()

print('Connecting to database...')

# for sqlite connection
# current_dir = os.path.dirname(__file__)
# engine = create_engine('sqlite:////{}/luckydraw.db'.format(current_dir), convert_unicode=True)

# for postgresql connection
engine = create_engine(os.environ.get("POSTGRES_URL"), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    print('We are connected to database successfully')
