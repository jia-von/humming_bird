from scrape_organisation import scrape_org
from sqlalchemy import create_engine
from sql_alchemy import db_connection

# create sqlalchemy engine
engine = create_engine(db_connection)

# connect to the PostgreSQL server
with engine.connect() as conn:
    if engine.has_table('github_url'):
        result_org = scrape_org('https://api.github.com/organizations?per_page=100')
        result_org.to_sql('github_url',schema='public', con=conn, if_exists='append')
    else:
        engine.execute('''
        CREATE TABLE github_url (
            index int,
            url varchar
        )
        ''')
        result_org = scrape_org('https://api.github.com/organizations?per_page=100')
        result_org.to_sql('github_url',schema='public', con=conn, if_exists='append')
