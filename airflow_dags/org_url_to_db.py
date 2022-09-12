# The DAG object; we'll need this to instantiate a DAG
from distutils.command.upload import upload
from airflow import DAG


# Operators; we need this to operate!
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator

DAG_ID = 'scrape_org_url'

# Work with python within DAG
with DAG(
    dag_id=DAG_ID,
    description='Obtain organisation URL from GitHub via scrape_org function',
    schedule_interval="@once",
    catchup=False,
) as dag:

    # make a callable function 
    # refer: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
    def upload_scrape_org():

        import requests
        import pandas as pd
        from sqlalchemy import create_engine, inspect

        def scrape_org(api_url):
            url = requests.get(api_url).text
            read_json = pd.read_json(url)
            return read_json['url']

        # def link_head(api_url):
        #     dict_head = requests.head(api_url).links['next']
        #     return dict_head['url']

        db_connection = 'postgresql+psycopg2://airflow_user:airflow_pass@localhost:5432/github'
        api_url = 'https://api.github.com/organizations?per_page=100'
        i = 0

        engine = create_engine(db_connection)

        while i < 10:
            with engine.connect() as conn:
                if inspect(engine).has_table('github_url'):
                    result_org = scrape_org(api_url)
                    result_org.to_sql('github_url',schema='public',index=False, con=conn, if_exists='append')
                    # api_url = link_head(api_url)
                    i += 1
                    # print(api_url)
                else:
                        engine.execute('CREATE TABLE github_url (url varchar)')
                        result_org = scrape_org(api_url)
                        result_org.to_sql('github_url',schema='public', con=conn,index=False, if_exists='append')
                        # api_url = link_head(api_url)
                        i += 1
                        # print(api_url)


    run_scrape_org = PythonOperator(
        task_id='run scrape_org',
        python_callable=upload_scrape_org() 
    )