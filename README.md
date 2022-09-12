# Using GitHub API to analyse organisations
This project was created out of my desire to automate my job search using GitHub API. The major reason I am using GitHub for my job search is because I can review their quality of their work on public repositories. Additionally, I am able to filter organisations based on the programming languages and stacks they use, so I may communicate my desire to work with them.

## Setup
1. Create a Python [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#). 
2. Setup [PostgreSQL database](https://www.postgresql.org/download/linux/ubuntu/). 
3. Setup [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html).

```bash
# Clone the repository
git clone https://github.com/jia-von/humming_bird.git
cd humming_bird

# Set up a Python virtual environment, venv
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install packages
pip install sqlalchemy pandas psycopg2 apache-airflow apache-airflow-providers-postgres
```
