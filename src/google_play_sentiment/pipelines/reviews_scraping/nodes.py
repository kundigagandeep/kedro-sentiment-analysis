"""
This is a boilerplate pipeline 'reviews_scraping'
generated using Kedro 0.18.2
"""
import pandas as pd
import numpy as np
from google_play_scraper import app, Sort, reviews_all
from transformers import pipeline

def reviews_scrape(df: pd.DataFrame) -> pd.DataFrame:
    hk_project = reviews_all( 'com.hikingproject.android', 
                            sleep_milliseconds=0, 
                            lang ='en',
                            country='US', 
                            sort=Sort.NEWEST)

    reviews = pd.json_normalize(hk_project)

    return reviews

def reviews_sentiment(df):
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")

    df['content'] = df['content'].astype('str')

    df['result'] = df['content'].apply(lambda x: sentiment_analysis(x))

    df['sentiment']= df['result'].apply(lambda x: (x[0]['label']))

    df['score']= df['result'].apply(lambda x: (x[0]['score']))

    return df