"""
This is a boilerplate pipeline 'reviews_scraping'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import reviews_scrape, reviews_sentiment


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(reviews_scrape,
                inputs="reviews",
                outputs="reviews_processed"

                ),
                node(
                reviews_sentiment,
                inputs="reviews_processed",
                outputs='reviews_with_sentiment'
            )
        ]
    )