from kedro.pipeline import Pipeline, node, pipeline
from .nodes import reviews_sentiment

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(
                reviews_sentiment,
                inputs="reviews_processed",
                outputs='reviews_with_sentiment'
            )
        ]
    )