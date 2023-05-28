from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(__file__)

# for sqlite connection
# engine = create_engine('sqlite:////{}/luckydraw.db'.format(current_dir), convert_unicode=True)

# for postgresql connection
engine = create_engine(os.environ.get("POSTGRES_URL"), convert_unicode=True)

#
# engine = conn = psycopg2.connect(
#     host=os.environ.get("POSTGRES_HOST"),
#     database=os.environ.get("POSTGRES_DATABASE"),
#     user=os.environ.get("POSTGRES_USER"),
#     password=os.environ.get("POSTGRES_PASSWORD"))
###
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
    print('We are connected to database successfully')
