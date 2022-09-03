from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generating_report

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
        node(func=generating_report,inputs="reviews_processed",outputs=None,namespace="silver_data_processed"),
        node(func=generating_report,inputs="reviews_with_sentiment",outputs=None,namespace="final_data_processed")
        ]
    )