"""
This is a boilerplate pipeline 'reviews_scraping'
generated using Kedro 0.18.2
"""
import pandas as pd
import numpy as np
from google_play_scraper import app, Sort, reviews_all
from transformers import pipeline

def reviews_scrape():
    hk_project = reviews_all( 'com.hikingproject.android', 
                            sleep_milliseconds=0, 
                            lang ='en',
                            country='US', 
                            sort=Sort.NEWEST)

    reviews = pd.json_normalize(hk_project)

    return reviews