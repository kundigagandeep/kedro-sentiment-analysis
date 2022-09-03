import pandas as pd
from datetime import datetime

def reviews_processing(df: pd.DataFrame):

    df = df.drop(columns=['userName','userImage','replyContent','repliedAt'])

    df = df.rename(columns={"at":"date","score":"rating"})

    df['date'] =  pd.to_datetime(df['date'], infer_datetime_format=True)

    return df

# def split_month(df: pd.DataFrame):

#     df['date'] = pd.to_datetime(df['date'], format='%Y%m%d %H:%M:%S')

#     df['month'] = df['date'].dt.month

#     currentMonth = datetime.now().month

#     df2 = df[df['month']==currentMonth]

#     df2 = df2.drop(columns='month')

#     return df2