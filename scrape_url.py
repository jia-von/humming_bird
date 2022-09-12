from scrape_organisation import link_head, scrape_org
from sqlalchemy import create_engine, inspect
from sql_alchemy import db_connection

# Setup variables
api_url = 'https://api.github.com/organizations?per_page=100'
i = 0

# create sqlalchemy engine, connect using psycopg2
# Refer: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2
engine = create_engine(db_connection)

# GitHub on allow 60 calls perhour for public API
while i < 10:
    # Step 1: Initiate creation of table and inserting first row
    # connect to the PostgreSQL server
    # Refer: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#server-side-cursors
    with engine.connect() as conn:

    # If table 'github_url' exists, append table
    # Refer: https://docs.sqlalchemy.org/en/14/core/reflection.html?highlight=inspector+has_table#fine-grained-reflection-with-inspector
        if inspect(engine).has_table('github_url'):
            result_org = scrape_org(api_url)
            result_org.to_sql('github_url',schema='public', con=conn, index=False, if_exists='append')
            
            # obtain header link for the next pagination
            api_url = link_head(api_url)
            i += 1

            # obtain information in regards to the last pagination before the sequence ends.
            print(api_url)
        else:
            # create 'github_url' if does not exist
            engine.execute('''
            CREATE TABLE github_url (
            url varchar
            )
            ''')
            result_org = scrape_org(api_url)
            result_org.to_sql('github_url',schema='public', con=conn, index=False, if_exists='append')
            api_url = link_head(api_url)
            i += 1
            print(api_url)