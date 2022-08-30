"""
This is a boilerplate pipeline 'data_validation'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import raw_data_validation

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
                node(raw_data_validation,
                inputs="reviews",
                outputs=None

                )
        ]
    )