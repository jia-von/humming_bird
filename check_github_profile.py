from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Identity
from sql_alchemy import db_connection

# Get organisation name from URL postgres
engine = create_engine(db_connection)

# Testing with reading sql from database using sqlalchemy
# Refer: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
metadata_obj = MetaData()

# Instiate Table using MetaData via sqlalchemy
meta_github_url = Table('github_url',metadata_obj,autoload=True,autoload_with=engine)
meta_org_table = Table('organisations', metadata_obj,
                Column('org_id', Integer, Identity()),
                Column('org_name', String(40), nullable=False),
                Column('org_web', String(250), nullable=True),
                Column('org_email', String(250), nullable=True),
                Column('org_location', String(250))
                )

# Create table if does not exist
meta_org_table.create(bind=engine,checkfirst=True)
