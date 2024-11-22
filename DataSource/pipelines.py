# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import DatasourceItem
from datetime import datetime, timedelta
import csv
import os
import pandas as pd
import shutil


yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

airports = [
    'CKG', 'TFU', 'CTU', 'SHA', 'PVG', 'TNA', 'PEK', 'PKX', 'CAN', 'FUO',
    'SZX', 'HKG', 'MFM', 'ZUH', 'NKG', 'HGH', 'WUH', 'CSX', 'HRB', 'DLC',
    'XMN', 'TSN', 'HFE', 'KHN', 'HAK', 'KWE', 'KMG', 'LHW', 'NGB', 'URC',
    'FOC', 'JJN', 'XIY', 'INC', 'TYN', 'SJW', 'CGO', 'TAO', 'YNT', 'NNG',
    'SYX', 'WNZ', 'HET', 'XUZ', 'WEH', 'CGQ', 'BAV', 'KWL', 'LJG', 'YNJ',
]


class DatasourcePipeline:
    def open_spider(self, spider):
        self.start = datetime.now()
        self.count = 0

        headlines = [
            'identification_id', 'identification_number', 'identification_callsign', 'aircraft_code', 'Airline',
            'airport_origin_icao', 'airport_origin_latitude', 'airport_origin_longitude', 'airport_origin_offset',
            'airport_destination_icao', 'airport_destination_latitude', 'airport_destination_longitude', 'airport_destination_offset',
            'median_time', 'median_delay', 'median_timestamp', 'status_text',
            'track_latitude', 'track_longitude', 'track_altitude', 'track_heading', 'track_speed',
            'track_timestamp', 'track_vertical_speed',
            'time_estimated_departure', 'time_estimated_arrival', 'time_real_departure', 'time_real_arrival',
            'time_scheduled_departure', 'time_scheduled_arrival', 'time_other_eta', 'time_other_duration'
        ]

        os.makedirs(f'flights/{yesterday}', exist_ok=True)

        for airport in airports:
            with open(f"flights/{yesterday}/{yesterday}-{airport}.csv", 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headlines)
            print(f'The CSV file of {airport} on {yesterday} has been initialized.')

        print()

    def process_item(self, item, spider):
        if isinstance(item, DatasourceItem):
            item_dict = ItemAdapter(item).asdict()

            for trail in item_dict['track']:
                trail['timestamp'] = datetime.fromtimestamp(trail['timestamp']).strftime('%Y.%m.%d, %H:%M:%S')

            with open(f"flights/{yesterday}/{yesterday}-{item_dict['airport']}.csv", 'a',
                      encoding='utf-8') as f:
                writer = csv.writer(f)
                for i in range(len(item_dict['track'])):
                    content = [
                        item_dict['flight_id'], item_dict['id_number'], item_dict['callsign'],
                        item_dict['aircraft_icao'], item_dict['airline'],
                        item_dict['origin_icao'], item_dict['origin_latitude'], item_dict['origin_longitude'],
                        item_dict['origin_offset'],
                        item_dict['destination_icao'], item_dict['destination_latitude'],
                        item_dict['destination_longitude'], item_dict['destination_offset'],
                        item_dict['median_time'], item_dict['median_delay'], item_dict['median_timestamp'],
                        item_dict['status_text'],
                        item_dict['track'][i]['latitude'], item_dict['track'][i]['longitude'],
                        item_dict['track'][i]['altitude']['feet'], item_dict['track'][i]['heading'],
                        item_dict['track'][i]['speed']['kmh'],
                        item_dict['track'][i]['timestamp'], item_dict['track'][i]['verticalSpeed']['fpm'],
                        item_dict['time_estimated_departure'], item_dict['time_estimated_arrival'],
                        item_dict['time_real_departure'], item_dict['time_real_arrival'],
                        item_dict['time_scheduled_departure'], item_dict['time_scheduled_arrival'],
                        item_dict['time_other_eta'], item_dict['time_other_duration'],
                    ]
                    writer.writerow(content)

            self.count += 1

        return item

    def close_spider(self, spider):
        # concatenate_files()
        # zip_files()
        self.end = datetime.now()
        interval = self.end - self.start

        print()
        print(f'{self.count} flights have been stored in the directory: "../../flights/{yesterday}".')
        print(f'The procedure started at {self.start.strftime("%Y-%m-%d, %H:%M:%S")} and ended at {self.end.strftime("%Y-%m-%d, %H:%M:%S")},')
        print(f'which takes roughly {interval.total_seconds() / 60:.2f} minutes.')
        print()


# class RoughinfoPipeline:
#     def open_spider(self, spider):
#         headlines = [
#             'time_estimated_departure', 'time_estimated_arrival', 'time_real_departure', 'time_real_arrival',
#             'time_scheduled_departure', 'time_scheduled_arrival', 'time_other_eta', 'time_other_duration',
#         ]
#
#         os.makedirs(f'../../flights/{yesterday}', exist_ok=True)
#
#         for airport in airports:
#             with open(f"../../flights/{yesterday}/{yesterday}-{airport}-brief.csv", 'w', encoding='utf-8') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(headlines)
#
#     def process_item(self, item, spider):
#         if isinstance(item, RoughinfoItem):
#             item_dict = ItemAdapter(item).asdict()
#
#             with open(f"../../flights/{yesterday}/{yesterday}-{item_dict['airport']}-brief.csv", 'a',
#                       encoding='utf-8') as f:
#                 writer = csv.writer(f)
#                 for i in range(len(item_dict['track'])):
#                     content = [
#                         item_dict['time_estimated_departure'], item_dict['time_estimated_arrival'],
#                         item_dict['time_real_departure'], item_dict['time_real_arrival'],
#                         item_dict['time_scheduled_departure'], item_dict['time_scheduled_arrival'],
#                         item_dict['time_other_eta'], item_dict['time_other_duration'],
#                     ]
#                     writer.writerow(content)
#
#         return item


# def concatenate_files():
#     for airport in airports:
#         main = pd.read_csv(f'../../flights/{yesterday}/{yesterday}-{airport}.csv')
#         brief = pd.read_csv(f'../../flights/{yesterday}/{yesterday}-{airport}-brief.csv')
#         main = pd.concat([main, brief], axis=1)
#         main.to_csv(f'../../flights/{yesterday}/{yesterday}-{airport}.csv', index=False)
#
#         try:
#             os.remove(f'../../flights/{yesterday}/{yesterday}-{airport}-brief.csv')
#         except FileNotFoundError:
#             pass

def zip_files():
    path = f'flights/{yesterday}'
    try:
        shutil.make_archive(base_name=yesterday, format='zip', root_dir=path)
    except Exception:
        print(f'Regret to tell you that you failed to zip the files in the directory: {path}.')
    else:
        print(f'You successfully zip the files in the directory: {path}.')
