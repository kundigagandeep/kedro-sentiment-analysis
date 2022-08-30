import sys
import logging
from kedro.framework.hooks import hook_impl
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
from great_expectations.data_context import DataContext


def raw_data_validation(dataset_name:str)-> None:
    data_context = DataContext(
        context_root_dir="C:/Users/gagan/Python Projects/kedro/kedro-sentiment-analysis/great_expectations"
    )

    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name="raw_data_warning",
        batch_request=None,
        run_name=None,
    )

    if result["success"]==False:
        logging.warning("Validation failed!")
        sys.exit(1)

    logging.info("Validation succeeded!")
    data_context.open_data_docs()
    #sys.exit(0)

def final_data_validation(dataset_name:str)-> None:
    data_context = DataContext(
        context_root_dir="C:/Users/gagan/Python Projects/kedro/kedro-sentiment-analysis/great_expectations"
    )

    result: CheckpointResult = data_context.run_checkpoint(
        checkpoint_name="final_warning",
        batch_request=None,
        run_name=None,
    )

    if result["success"]==False:
        logging.warning("Validation failed!")
        sys.exit(1)

    logging.info("Validation succeeded!")
    data_context.open_data_docs()
    #sys.exit(0)