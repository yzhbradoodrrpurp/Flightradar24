# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatasourceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    airport = scrapy.Field()

    flight_id = scrapy.Field()
    id_number = scrapy.Field()
    callsign = scrapy.Field()

    aircraft_icao = scrapy.Field()
    airline = scrapy.Field()

    origin_icao = scrapy.Field()
    origin_latitude = scrapy.Field()
    origin_longitude = scrapy.Field()
    origin_offset = scrapy.Field()

    destination_icao = scrapy.Field()
    destination_latitude = scrapy.Field()
    destination_longitude = scrapy.Field()
    destination_offset = scrapy.Field()

    median_time = scrapy.Field()
    median_delay = scrapy.Field()
    median_timestamp = scrapy.Field()

    status_text = scrapy.Field()
    track = scrapy.Field()

    time_estimated_departure = scrapy.Field()
    time_estimated_arrival = scrapy.Field()
    time_real_departure = scrapy.Field()
    time_real_arrival = scrapy.Field()
    time_scheduled_departure = scrapy.Field()
    time_scheduled_arrival = scrapy.Field()
    time_other_eta = scrapy.Field()
    time_other_duration = scrapy.Field()


# class RoughinfoItem(scrapy.Item):
#     airport = scrapy.Field()
#     track = scrapy.Field()
#
#     time_estimated_departure = scrapy.Field()
#     time_estimated_arrival = scrapy.Field()
#     time_real_departure = scrapy.Field()
#     time_real_arrival = scrapy.Field()
#     time_scheduled_departure = scrapy.Field()
#     time_scheduled_arrival = scrapy.Field()
#     time_other_eta = scrapy.Field()
#     time_other_duration = scrapy.Field()
