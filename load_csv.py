import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///mon_sgbd.db')
df = pd.read_csv('ships.csv', sep=';', nrows=15000)
df.to_sql('navires', engine)

df_journey = pd.read_csv('journey.csv', sep=',')
df_journey.to_sql('trajets', engine)
