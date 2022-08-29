"""
This is a boilerplate pipeline 'reviews_scraping'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import reviews_scrape

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(reviews_scrape,
                inputs=None,
                outputs="reviews"

                )
        ]
    )