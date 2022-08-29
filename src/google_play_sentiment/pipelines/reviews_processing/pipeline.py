"""
This is a boilerplate pipeline 'reviews_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import reviews_processing

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(
                reviews_processing,
                inputs="reviews",
                outputs='reviews_processed'
            )
        ]
    )
