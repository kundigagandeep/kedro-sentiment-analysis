"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from google_play_sentiment.pipelines import reviews_scraping as scrape,\
                                            reviews_sentiment as sent,\
                                            reviews_processing as prep,\
                                            data_validation as rdv,\
                                            final_data_validation as fdv


def register_pipelines() -> Dict[str, Pipeline]:
    
    scrape_pipeline = scrape.create_pipeline()

    data_validation = rdv.create_pipeline()

    process_reviews = prep.create_pipeline()

    reviews_sentiment = sent.create_pipeline()

    final_data_validation = fdv.create_pipeline()

    return {

        "__default__": scrape_pipeline + data_validation + process_reviews + reviews_sentiment + final_data_validation,
        "scrape": scrape_pipeline + data_validation,
        "preprocessing": process_reviews,
        "sentiment": reviews_sentiment + final_data_validation
    }

