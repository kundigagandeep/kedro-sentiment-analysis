from kedro.pipeline import Pipeline, node, pipeline
from .nodes import data_upload

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(data_upload,
                inputs="reviews_with_sentiment",
                outputs=None

                )
        ]
    )