import logging
from datetime import datetime, timedelta
import argparse
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from histrory_reader import ItemsHistoryReport
from unit_items import ItemsLists


def get_params():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("-unit_name", type=str, help="unit name", default="unit_30")
    parser.add_argument("-unit_id", type=str, help="unit number", default="1")
    parser.add_argument(
        "-start_date",
        type=str,
        help="Start date as %dd-%mm-%yy hh:00:00.000",
        default=datetime.now().strftime("%d-%m-%y 10:00:00.000"),
    )
    parser.add_argument(
        "-end_date",
        type=str,
        help="End date as %dd-%mm-%yy hh:00:00.000",
        default=(datetime.now() + timedelta(days=1)).strftime("%d-%m-%y 08:00:00.000"),
    )
    parser.add_argument(
        "-out_type", type=str, choices=["xml", "json", "list"], default="xml"
    )
    parser.add_argument("-debug", help="debug is on", action="store_true", default=True)

    return parser.parse_args()


if __name__ == "__main__":

    run_params = get_params()

    if run_params.debug:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.ERROR

    location = os.path.dirname(__file__)
    sys.path.append(location)
    logging.basicConfig(
        filename=f"{location}/logs/{datetime.today().strftime('%Y-%m-%d')}.log",
        level=logging_level,
        format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # create handler
    handler = TimedRotatingFileHandler(
        filename=f"{location}/logs/runtime.log",
        when="D",
        interval=1,
        backupCount=3,
        encoding="utf-8",
        delay=False,
    )

    # create formatter and add to handler
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # add the handler to named logger
    logging.getLogger("sql_handler").addHandler(handler)

    logging.debug("=======================HANDLE REQUEST=============================")
    logging.debug("run with params = " + str(run_params))

    try:
        request_items = ItemsLists.get_unit_items(
            run_params.unit_name, run_params.unit_id
        )
        items_report = ItemsHistoryReport(request_items)
        logging.debug("Start read data")
        start_retrieve_timestamp = datetime.now()
        items_report.read_data_from_fast_tools(
            run_params.start_date, run_params.end_date
        )

        execution_time_in_ms = (
            datetime.now() - start_retrieve_timestamp
        ).total_seconds() * 1000
        logging.debug(
            "Data received. Execution time = {:.3f} ms".format(execution_time_in_ms)
        )

        result = "no_data"
        if run_params.out_type == "xml":
            result = items_report.to_xml_string()
            print(result)
        else:
            result = items_report.to_json_string()
            print(result)
            logging.debug(result)
    except Exception:
        logging.exception("exception ", exc_info=1)
        # logging.error(str(ex)+str(ex.with_traceback(Tr)))
