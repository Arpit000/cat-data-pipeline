# upload_to_postgres.py
import pandas as pd
from sqlalchemy import create_engine

# -- Step 1: Load DataFrame
df = pd.read_csv("cat_data.csv")

# -- Step 2: Connect to Postgres
user = 'postgres'
password = 'PASSWORD'  # match your Docker run password
host = 'localhost'
port = 5432
database = 'postgres'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# -- Step 3: Upload to Postgres
df.to_sql('cat', engine, if_exists='replace', index=False)
print("✅ Data uploaded to Postgres.")
