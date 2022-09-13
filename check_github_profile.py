from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Identity
from sql_alchemy import db_connection

# Get organisation name from URL postgres
engine = create_engine(db_connection)

# Testing with reading sql from database using sqlalchemy
# Refer: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
metadata_obj = MetaData()
meta_github_url = Table('github_url',metadata_obj,autoload=True,autoload_with=engine)
meta_org = Table('organisations', metadata_obj,
                Column('org_id', Integer, Identity()),
                Column('org_name', String(40), nullable=False),
                )

meta_org.create(engine,checkfirst=True)
