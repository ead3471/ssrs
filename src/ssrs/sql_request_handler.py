import logging
from datetime import datetime, timedelta
import argparse
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from histrory_reader import ItemsHistoryReport
from unit_items import ItemsLists

SCRIPT_LOCATION = os.path.dirname(__file__)
LOG_FOLDER = os.path.join(SCRIPT_LOCATION, "logs")


def get_params() -> argparse.ArgumentParser:
    """
    setup and parse cli
    :return: ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("-unit_name", type=str, help="unit name", default="unit_30")
    parser.add_argument("-unit_id", type=str, help="unit number", default="1")
    parser.add_argument(
        "-start_date",
        type=str,
        help="Start date as dd-mm-yy hh:00:00.000",
        default=datetime.now().strftime("%d-%m-%y 10:00:00.000"),
    )
    parser.add_argument(
        "-end_date",
        type=str,
        help="End date as dd-mm-yy hh:00:00.000",
        default=(datetime.now() + timedelta(days=1)).strftime("%d-%m-%y 08:00:00.000"),
    )
    parser.add_argument(
        "-out_type", type=str, choices=["xml", "json"], default="xml"
    )
    parser.add_argument(
        "-file", type=str, default="", help="out file name"
    )
    parser.add_argument("-debug", help="debug is on", action="store_true", default=True)

    parser.parse_args()
    return parser


def init_logger(level=logging.DEBUG):
    os.makedirs(LOG_FOLDER, exist_ok=True)
    handler = TimedRotatingFileHandler(
        filename=str(os.path.join(LOG_FOLDER, 'handler_log')),
        when="D",
        interval=1,
        backupCount=30,
        encoding="utf-8",
        delay=False,
    )
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    handler.suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(level)


if __name__ == "__main__":
    sys.path.append(SCRIPT_LOCATION)
    run_params = get_params()

    # if run_params.help:
    #run_params.print_help()
    # else:

    if run_params.debug:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.ERROR

    init_logger(logging_level)

    logging.debug("=======================HANDLE REQUEST=============================")
    logging.debug(f"run with params {run_params}")

    try:
        request_items = ItemsLists.get_unit_items(
            run_params.unit_name, run_params.unit_id
        )
        items_report = ItemsHistoryReport(request_items)
        logging.debug("Start read data")
        start_retrieve_timestamp = datetime.now()
        items_report.read_data_from_fast_tools(
            run_params.start_date,
            run_params.end_date
        )

        execution_time_in_ms = (datetime.now() - start_retrieve_timestamp).total_seconds() * 1000
        logging.debug(
            "Data received. Execution time = {:.3f} ms".format(execution_time_in_ms)
        )

        result = "no_data"
        if run_params.out_type == "xml":
            result = items_report.to_xml_string()
        elif run_params.out_type == "json":
            result = items_report.to_json_string()

        if run_params.file:
            with open(run_params.file, "w") as file:
                file.write(result)
        else:
            print(result)

        logging.debug(result)
    except BaseException as ex:
        logging.error(f"Processing request error:{ex}")
