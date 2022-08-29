"""
This is a boilerplate pipeline 'reviews_processing'
generated using Kedro 0.18.2
"""
import pandas as pd

def reviews_processing(df: pd.DataFrame):

    df = df.drop(columns=['userName','userImage','replyContent','repliedAt'])

    df = df.rename(columns={"at":"date"})

    df['date'] =  pd.to_datetime(df['date'], infer_datetime_format=True)

    return df