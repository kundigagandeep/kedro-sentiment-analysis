"""
This is a boilerplate pipeline 'reviews_sentiment'
generated using Kedro 0.18.2
"""
from transformers import pipeline

def reviews_sentiment(df):
    
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")

    df['content'] = df['content'].astype('str')

    df['result'] = df['content'].apply(lambda x: sentiment_analysis(x))

    df['sentiment']= df['result'].apply(lambda x: (x[0]['label']))

    df['score']= df['result'].apply(lambda x: (x[0]['score']))

    df['score'] = round(df['score'],3)

    df = df.rename(columns={"score":"sentiment_score"})

    df = df.drop(columns="result")

    df = df[['reviewId', 'date', 'content', 'rating', 'thumbsUpCount', 'reviewCreatedVersion','sentiment','sentiment_score']]

    return df