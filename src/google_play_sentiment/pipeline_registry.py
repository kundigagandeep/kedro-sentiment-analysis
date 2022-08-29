"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline



from google_play_sentiment.pipelines import reviews_scraping as scrape

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    scrape_pipeline = scrape.create_pipeline()

    return {
        "__default__": scrape_pipeline
    }

