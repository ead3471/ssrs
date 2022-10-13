from typing import Dict, List
import dss
import json
import xml.etree.ElementTree as xml
import logging
from sys import getdefaultencoding
import codecs



class FastToolsAggregationItem:
    report_fields = ['H_0', 'H_2', 'H_4', 'H_6', 'H_8', 'H_10', 'H_12', 'H_14', 'H_16', 'H_18', 'H_20', 'H_22',
                     'Q_H_0', 'Q_H_2', 'Q_H_4', 'Q_H_6', 'Q_H_8', 'Q_H_10', 'Q_H_12', 'Q_H_14', 'Q_H_16', 'Q_H_18',
                     'Q_H_20',
                     'Q_H_22']

    @staticmethod
    def check_fields_and_set_zero_if_not_present(data: dict):
        for field in FastToolsAggregationItem.report_fields:
            if field not in data:
                data[field] = '0'

    def __init__(self, item_specification: dict, order_number=1):
        if 'NAME' not in item_specification:
            raise ValueError('Bad item spec for:' + dict)
        else:
            self.item_name = item_specification['NAME']
            self.integration_type = item_specification['INT_TYPE'] or 'i'
        self.group_id = item_specification['GROUP_ID'] or '1'
        self.order_number = order_number

    def get_item_properties(self, conn) -> dict:
        item_data = {}
        item_dataset = dss.openDataset(conn, 'ITEM_DF', ['NAME', 'HIGH_LIMIT', 'LOW_LIMIT','ENG_UNIT'], 'r')
        item_properties = dss.readEqual(conn, item_dataset, self.item_name + '.PV')
        item_data['NAME'] = self.item_name
        item_data['GROUP_ID'] = self.group_id
        item_data['ORDER_NUMBER'] = self.order_number

        str2=str(item_properties['ENG_UNIT'].encode('unicode_escape').decode('ascii',errors='ignore')).replace("\\xb","")
        item_data['ENG_UNIT'] = str2
        if self.integration_type == 'i':
            item_data['HIGH_LIMIT'] = item_properties['HIGH_LIMIT']*2
            item_data['LOW_LIMIT'] = item_properties['LOW_LIMIT']*2
        else:
            item_data['HIGH_LIMIT'] = item_properties['HIGH_LIMIT']
            item_data['LOW_LIMIT'] = item_properties['LOW_LIMIT']

        dss.closeDataset(conn, item_dataset)
        return item_data

    def get_2_hour_item_history(self, conn, start, end) -> dict:
        history_samples = dss.getItemHistory(conn, self.item_name + '.2_HOUR', 'AGGREGATION', start, end, 24)
        data = {}
        interval_sum = 0
        samples_count = 0
        for sample in history_samples:
            if not (sample is None):
                sample_time = dss.dateConvert(conn, sample[0], 'GMT_TO_LCT')
                # fields like H_0 and Q_H_0:
                sample_hour = 'H_' + str(dss.dateString(conn, sample_time, 'h'))
                sample_hour_quality = 'Q_' + sample_hour

                current_hour_value = float(str((sample[1])))
                interval_sum = interval_sum + current_hour_value
                samples_count += 1
                data[sample_hour] = str((sample[1]))
                data[sample_hour_quality] = sample[4]

        FastToolsAggregationItem.check_fields_and_set_zero_if_not_present(data)

        if samples_count == 0:
            data['SUM'] = 0.0
        elif self.integration_type == 'i':
            data['SUM'] = interval_sum
        else:
            data['SUM'] = interval_sum / samples_count
        return data


    def get_empty_report(self):
        item_params={}
        item_params['NAME'] = self.item_name
        item_params['GROUP_ID'] = self.group_id
        item_params['ORDER_NUMBER'] = self.order_number
        item_params['ENG_UNIT'] = '-'
        item_params['HIGH_LIMIT'] = '0'
        item_params['LOW_LIMIT'] = '0'

        item_params['SUM']=0
        for hour in (10,12,14,16,18,20,22,0,2,4,6,8):
            item_params[f'H_{hour}']=0
            item_params[f'Q_{hour}'] = 0

        return item_params

    def get_2_hour_item_report(self, conn, start_date, end_date) -> dict:

        item_params = self.get_item_properties(conn)
        item_his = self.get_2_hour_item_history(conn, start_date, end_date)

        return {**item_his, **item_params}


class ItemsHistoryReport:
    def __init__(self, items_for_read: List[Dict]):
        self.items = []
        self.report_data = []
        items_count = 1
        for item_spec in items_for_read:
            self.items.append(FastToolsAggregationItem(item_spec, items_count))
            items_count += 1



    def read_data_from_fast_tools(self, start_date: str, end_date: str):
        conn = dss.connect()
        start = dss.dateDSS(conn, start_date)
        corrected_start = dss.dateConvert(conn, start, 'LCT_TO_GMT')
        end = dss.dateDSS(conn, end_date)
        corrected_end = dss.dateConvert(conn, end, 'LCT_TO_GMT')

        self.report_data = []

        for item in self.items:
            try:
                item_report = item.get_2_hour_item_report(conn, corrected_start, corrected_end)
            except Exception as ex:
                logging.error('Item report read error for ' + item.item_name + ":" + str(ex))
                item_report=item.get_empty_report()
            self.report_data.append(item_report)

        dss.close(conn)

    def to_xml_string(self) -> str:
        root = xml.Element('Unit')
        for item_record in self.report_data:
            item_element = xml.Element("item")
            root.append(item_element)
            for field in item_record.keys():
                field_element = xml.Element(field)
                field_element.text = str(item_record[field])
                item_element.append(field_element)

        tree = xml.ElementTree(root)
        xml_string = xml.tostring(tree.getroot(), encoding='unicode')
        return xml_string

    def to_json_string(self) -> str:
        return json.dumps(self.report_data)
