from kedro.pipeline import Pipeline, node, pipeline
from .nodes import final_data_validation

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(final_data_validation,
                inputs="reviews_with_sentiment",
                outputs=None

                )
        ]
    )