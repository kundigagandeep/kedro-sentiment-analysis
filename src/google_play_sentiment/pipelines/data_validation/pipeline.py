from kedro.pipeline import Pipeline, node, pipeline
from .nodes import raw_data_validation, final_data_validation

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(func=raw_data_validation,inputs="reviews",outputs=None),
            node(func=final_data_validation,inputs="reviews_with_sentiment",outputs=None)

        ]
    )