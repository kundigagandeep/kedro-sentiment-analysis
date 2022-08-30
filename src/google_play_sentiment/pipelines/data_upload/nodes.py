from sqlalchemy import create_engine
import pandas as pd
from kedro.config import ConfigLoader
from kedro.framework.project import settings

CONF_SOURCE = "new_conf"

conf_path = str("C:/Users/gagan/Python Projects/kedro/kedro-sentiment-analysis/conf")
conf_loader = ConfigLoader(conf_source=conf_path, env="base")
credentials = conf_loader.get("credentials*", "credentials*/**")

creds = credentials['postgres']['con']

def data_upload(df: pd.DataFrame):
    
    engine = create_engine(creds)
    
    return df.to_sql('play_store', engine, if_exists='replace')