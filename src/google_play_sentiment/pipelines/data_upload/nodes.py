from sqlalchemy import create_engine
import pandas as pd

def data_upload(df: pd.DataFrame):
    
    engine = create_engine('postgresql://postgres:Speedy3861@localhost:5432/mydb')
    
    return df.to_sql('play_store', engine, if_exists='replace')