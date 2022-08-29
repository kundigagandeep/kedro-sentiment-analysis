"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline



from google_play_sentiment.pipelines import reviews_scraping as scrape, reviews_sentiment as sent, reviews_processing as prep


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    scrape_pipeline = scrape.create_pipeline()

    process_reviews = prep.create_pipeline()

    reviews_sentiment = sent.create_pipeline()

    return {

        "__default__": scrape_pipeline + process_reviews + reviews_sentiment,
        "scrape": scrape_pipeline,
        "preprocessing": process_reviews,
        "sentiment": reviews_sentiment
    }

