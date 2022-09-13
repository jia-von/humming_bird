from curses import meta
from enum import auto
from sqlalchemy import create_engine, MetaData, Table, Column, String, inspect
from sql_alchemy import db_connection

# Get organisation name from URL postgres
engine = create_engine(db_connection)

# Testing with reading sql from database using sqlalchemy
# Refer: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
metadata_obj = MetaData()
meta_table = Table('github_url',metadata_obj,autoload=True,autoload_with=engine)
print(meta_table.columns.keys())