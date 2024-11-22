import scrapy
import json
import time
from datetime import datetime, timedelta
from ..items import DatasourceItem


class Flightradar24Spider(scrapy.Spider):
    name = "flightradar24"
    allowed_domains = []
    start_urls = []

    def start_requests(self):
        self.headers = {
            'Cookie':
                'mac_overlay_count=68; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct'
                '+29+2024+15%3A45%3A00+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87'
                '%86%E6%97%B6%E9%97%B4)&version=202409.2.0&browserGpcFlag=0&isIABG'
                'lobal=false&hosts=&consentId=18a3fbdd-e489-4130-a63f-2e54e5cfc53b&'
                'interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C'
                '0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1%2COSSTA_B'
                'G%3A1&intType=1&geolocation=US%3BCA&AwaitingReconsent=false&GPPCoo'
                'kiesCount=1; OTGPPConsent=DBABLA~BVQqAAAACZA.QA; _ga_38V2BZ2HMF=GS1'
                '.1.1730187896.30.1.1730187898.58.0.0; _ga=GA1.1.1004982678.17269876'
                '24; mp_942a098c72ecbdd6c0d9c00fe8308319_mixpanel=%7B%22distinct_id%'
                '22%3A%20%22%24device%3A19284348610118a-03c0e1ab50492a-48193d01-1ce2'
                '6a-19284348610118a%22%2C%22%24device_id%22%3A%20%2219284348610118a-03c'
                '0e1ab50492a-48193d01-1ce26a-19284348610118a%22%2C%22%24initial_refe'
                'rrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%2'
                '0%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7'
                'B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referr'
                'ing_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%'
                '22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B'
                '%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _frPl=5bzHsWqW2S47UmsFs_vCbm-Uwcb'
                'KgDq5AMkg6rxsDbU; __cfruid=f4362bd1f465dc8dac9f7a33be18a179cab92243-173'
                '0180995; _sharedid=040b859a-dda4-4cfb-baad-bef07a78be7f; _sharedid_'
                'cst=zix7LPQsHA%3D%3D; hasConsentedToTerms=yes; FR24SID=9tg0lj25q2qj77'
                's6amdlbgdc8p33tgt2h23o9kts5klbcj9iquon; _frpk=5bzHsWqW2S47UmsFs_vCb'
                'g; FCNEC=%5B%5B%22AKsRol_-cpJwKRirOVerAeXfnyGsHOfC97S2qO0yeBeS7BKqeyhq'
                '4JnJYD9WzTPvgCahAKjIoByl-86kV3xUrbQ-YtD8awyhfZX1shEdT4yTDT99FvMmK0C'
                'D3ERnzzvefUmqkKMeEf0lyZXeas3c2pR154OGJ-YLlg%3D%3D%22%5D%5D; showAds=ye'
                's; _cc_id=16e4c66af0153c7eaa43c2aaad6aff6a; _ga_EPEHK8NQRN=GS1.1.172'
                '8479821.1.0.1728480447.0.0.0; _frc=RYp-qr9AbYk8yL_JyJlEx3-LU8JnwJOV5TC'
                'nz8xSFF_Ppdq_wpS_IEI2HZ9s0kA-OqnksiLgeHgYWQappoMGw3pyC-btpPvj1XRkQkAZV2'
                'INQS6cI-yBwAal2k094TW8eDjbHbTDA-hofnZ_F1lU-jKKuTz3czed7Wlt65RiK8WWu9kx'
                'HLQvJYew-fncrD9ECG9gpdHz-UKZhbaVmbSv4xdoc67DYV-lmi3qlclBK95-a4JBkYey1v'
                '-RHXQIdbqz; _frr=1; OptanonAlertBoxClosed=2024-09-22T06:47:31.570Z',
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
                '(KHTML, like Gecko) Version/18.0.1 Safari/605.1.15'

        }

        # 得到当前时间戳，转换为int类型去掉小数。
        # 大概是因为网站的一些反爬虫机制，只有用当前时间进行查询才能成功得到数据。
        self.now = int(datetime.now().timestamp())
        print(f'Now is {datetime.fromtimestamp(self.now).strftime("%Y-%m-%d %H:%M:%S")}.')

        # 由于得到的航班并不全是昨天的，所以需要进行进一步的筛选。
        # 得到昨天的datetime对象，从00:00到00:00。
        self.yesterday_ending = datetime.combine(datetime.fromtimestamp(self.now), datetime.min.time())
        self.yesterday_starting = self.yesterday_ending - timedelta(days=1)
        print(f'Yesterday started at {self.yesterday_starting.strftime("%Y-%m-%d %H:%M:%S")} and ended at {self.yesterday_ending.strftime("%Y-%m-%d %H:%M:%S")}.')
        print()

        # 将昨日开始和结束时间转换为时间戳。
        self.yesterday_starting = int(datetime.timestamp(self.yesterday_starting))
        self.yesterday_ending = int(datetime.timestamp(self.yesterday_ending))

        # 得到机场的代号。
        self.airports = [
            'CKG', 'TFU', 'CTU', 'SHA', 'PVG', 'TNA', 'PEK', 'PKX', 'CAN', 'FUO',
            'SZX', 'HKG', 'MFM', 'ZUH', 'NKG', 'HGH', 'WUH', 'CSX', 'HRB', 'DLC',
            'XMN', 'TSN', 'HFE', 'KHN', 'HAK', 'KWE', 'KMG', 'LHW', 'NGB', 'URC',
            'FOC', 'JJN', 'XIY', 'INC', 'TYN', 'SJW', 'CGO', 'TAO', 'YNT', 'NNG',
            'SYX', 'WNZ', 'HET', 'XUZ', 'WEH', 'CGQ', 'BAV', 'KWL', 'LJG', 'YNJ',
        ]

        print(f'The total number of airports are {len(self.airports)}.')
        print(f'The airports planned to crawl are as follows:')
        print(f'{self.airports}')
        print()

        for airport in self.airports:
            url = f'https://api.flightradar24.com/common/v1/airport.json?code={airport}&plugin[]=schedule&plugin-setting[schedule][mode]=arrivals&plugin-setting[schedule][timestamp]={str(self.now)}&limit=100&page=1&token=kcwaIAYjUVY_Kf7m7DUD8U15YnkB6Y2WatzcaQ7qvjo'
            # 将单独的机场代号传送给下一个方法，便于知道数据来源于哪一个机场。
            meta = {
                'airport': airport
            }
            yield scrapy.Request(url=url, callback=self.parse_pages, headers=self.headers, meta=meta)
            meta = {
                'airport': airport,
                'page': 1
            }
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers, meta=meta)

    # 这个方法用于得到机场的全部页面数。
    def parse_pages(self, response):
        data = json.loads(response.text)
        # 定位到json中的能够得到当前机场的全部页面数。
        pages = data['result']['response']['airport']['pluginData']['schedule']['arrivals']['page']['total']
        # 接收start_requests()方法传来的当前机场。
        airport = response.meta['airport']
        print(f'The airport {airport} has a total of {pages} pages.')
        print()

        # 页面数是-1，-2，....
        for page in range(1, pages):
            url = f'https://api.flightradar24.com/common/v1/airport.json?code={airport}&plugin[]=schedule&plugin-setting[schedule][mode]=arrivals&plugin-setting[schedule][timestamp]={str(self.now)}&limit=100&page={str(-page)}&token=kcwaIAYjUVY_Kf7m7DUD8U15YnkB6Y2WatzcaQ7qvjo'
            # 将机场代号和每个机场的过往页面数传送给下一个方法，便于展示。
            meta = {
                'airport': airport,
                'page': -page
            }
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers, meta=meta)

    # 这个方法用于获得降落航班的航班号和一般信息。
    def parse(self, response):
        data = json.loads(response.text)
        airport = response.meta['airport']
        page = response.meta['page']

        arrival_flights = data['result']['response']['airport']['pluginData']['schedule']['arrivals']['data']

        for arrival_flight in arrival_flights:
            # 截取出航班号。
            try:
                flight_id = arrival_flight['flight']['identification']['id']
            except Exception:
                flight_id = None

            try:
                time_estimated_departure = datetime.fromtimestamp(arrival_flight['flight']['time']['estimated']['departure']).strftime('%Y.%m.%d, %H:%M:%S')
            except Exception:
                time_estimated_departure = None
            try:
                time_estimated_arrival = datetime.fromtimestamp(arrival_flight['flight']['time']['estimated']['arrival']).strftime('%Y.%m.%d, %H:%M:%S')
            except Exception:
                time_estimated_arrival = None
            try:
                time_real_departure = datetime.fromtimestamp(arrival_flight['flight']['time']['real']['departure'])
            except Exception:
                time_real_departure = None
            try:
                time_real_arrival = datetime.fromtimestamp(arrival_flight['flight']['time']['real']['arrival'])
            except Exception:
                time_real_arrival = None
            try:
                time_scheduled_departure = datetime.fromtimestamp(arrival_flight['flight']['time']['scheduled']['departure'])
            except Exception:
                time_scheduled_departure = None
            try:
                time_scheduled_arrival = datetime.fromtimestamp(arrival_flight['flight']['time']['scheduled']['arrival'])
            except Exception:
                time_scheduled_arrival = None
            try:
                time_other_eta = datetime.fromtimestamp(arrival_flight['flight']['time']['other']['eta'])
            except Exception:
                time_other_eta = None

            time_other_duration = arrival_flight['flight']['time']['other']['duration']

            if flight_id is not None:
                if (time_real_arrival is None) or (self.yesterday_starting < int(datetime.timestamp(time_real_arrival)) < self.yesterday_ending):
                    url = f'https://api.flightradar24.com/common/v1/flight-playback.json?flightId={flight_id}&timestamp=&token=&pk='
                    meta = {
                        'airport': airport,
                        'page': page,
                        'time_estimated_departure': time_estimated_departure,
                        'time_estimated_arrival': time_estimated_arrival,
                        'time_real_departure': time_real_departure,
                        'time_real_arrival': time_real_arrival,
                        'time_scheduled_departure': time_scheduled_departure,
                        'time_scheduled_arrival': time_scheduled_arrival,
                        'time_other_eta': time_other_eta,
                        'time_other_duration': time_other_duration
                    }
                    yield scrapy.Request(url=url, callback=self.parse_flight, headers=self.headers, meta=meta)

        print(f'The flight ids of arrivals in {airport} of page {page} are successfully obtained.')
        print(f'Now we\'ll obtain the detailed information about the flights in {airport} of page {page}.')
        print()

    # 获得某个航班号的具体信息。
    def parse_flight(self, response):
        data = json.loads(response.text)
        airport = response.meta['airport']
        page = response.meta['page']

        # 这个是航班降落的时间戳。
        timestamp = data['result']['response']['data']['flight']['status']['generic']['eventTime']['utc']

        # 根据时间戳筛选出昨天00:00～00:00的航班。
        if (timestamp is not None) and (self.yesterday_starting < timestamp and timestamp < self.yesterday_ending):
            flight_id = data['result']['response']['data']['flight']['identification']['id']

            try:
                id_number = data['result']['response']['data']['flight']['identification']['number']['default']
            except TypeError:
                id_number = None
            try:
                callsign = data['result']['response']['data']['flight']['identification']['callsign']
            except TypeError:
                callsign = None

            try:
                aircraft_icao = data['result']['response']['data']['flight']['aircraft']['model']['code']
            except TypeError:
                aircraft_icao = None
            try:
                airline = data['result']['response']['data']['flight']['airline']['name']
            except TypeError:
                airline = None

            try:
                origin_icao = data['result']['response']['data']['flight']['airport']['origin']['code']['icao']
            except TypeError:
                origin_icao = None
            try:
                origin_latitude = data['result']['response']['data']['flight']['airport']['origin']['position']['latitude']
            except TypeError:
                origin_latitude = None
            try:
                origin_longitude = data['result']['response']['data']['flight']['airport']['origin']['position']['longitude']
            except TypeError:
                origin_longitude = None
            try:
                origin_offset = data['result']['response']['data']['flight']['airport']['origin']['timezone']['offset']
            except TypeError:
                origin_offset = None

            try:
                destination_icao = data['result']['response']['data']['flight']['airport']['destination']['code']['icao']
            except TypeError:
                destination_icao = None
            try:
                destination_latitude = data['result']['response']['data']['flight']['airport']['destination']['position']['latitude']
            except TypeError:
                destination_latitude = None
            try:
                destination_longitude = data['result']['response']['data']['flight']['airport']['destination']['position']['longitude']
            except TypeError:
                destination_longitude = None
            try:
                destination_offset = data['result']['response']['data']['flight']['airport']['destination']['timezone']['offset']
            except TypeError:
                destination_offset = None

            try:
                median_time = data['result']['response']['data']['flight']['median']['time']
                median_delay = data['result']['response']['data']['flight']['median']['delay']
                median_timestamp = datetime.fromtimestamp(data['result']['response']['data']['flight']['median']['timestamp'])
            except TypeError:
                median_time, median_delay, median_timestamp = None, None, None

            try:
                status_text = data['result']['response']['data']['flight']['status']['text']
            except TypeError:
                status_text = None

            track = data['result']['response']['data']['flight']['track']

            print(f'{flight_id} landed at {datetime.fromtimestamp(timestamp)} in {airport} on page {page}, which has {len(track)} track points.')

            time_estimated_departure = response.meta['time_estimated_departure']
            time_estimated_arrival = response.meta['time_estimated_arrival']
            time_real_departure = response.meta['time_real_departure']
            time_real_arrival = response.meta['time_real_arrival']
            time_scheduled_departure = response.meta['time_scheduled_departure']
            time_scheduled_arrival = response.meta['time_scheduled_arrival']
            time_other_eta = response.meta['time_other_eta']
            time_other_duration = response.meta['time_other_duration']

            # yield RoughinfoItem(
            #     airport=airport, track=track,
            #     time_estimated_departure=time_estimated_departure, time_estimated_arrival=time_estimated_arrival,
            #     time_real_departure=time_real_departure, time_real_arrival=time_real_arrival,
            #     time_scheduled_departure=time_scheduled_departure, time_scheduled_arrival=time_scheduled_arrival,
            #     time_other_eta=time_other_eta, time_other_duration=time_other_duration
            # )

            yield DatasourceItem(
                airport=airport, flight_id=flight_id, id_number=id_number, callsign=callsign, aircraft_icao=aircraft_icao, airline=airline,
                origin_icao=origin_icao, origin_latitude=origin_latitude, origin_longitude=origin_longitude, origin_offset=origin_offset,
                destination_icao=destination_icao, destination_latitude=destination_latitude, destination_longitude=destination_longitude, destination_offset=destination_offset,
                median_time=median_time, median_delay=median_delay, median_timestamp=median_timestamp, status_text=status_text, track=track,
                time_estimated_departure=time_estimated_departure, time_estimated_arrival=time_estimated_arrival,
                time_real_departure=time_real_departure, time_real_arrival=time_real_arrival,
                time_scheduled_departure=time_scheduled_departure, time_scheduled_arrival=time_scheduled_arrival,
                time_other_eta=time_other_eta, time_other_duration=time_other_duration
            )
