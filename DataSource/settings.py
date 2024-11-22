# Scrapy settings for DataSource project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import logging
from datetime import datetime

BOT_NAME = "DataSource"

SPIDER_MODULES = ["DataSource.spiders"]
NEWSPIDER_MODULE = "DataSource.spiders"

time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
LOG_FILE = f'logs/{time}.log'
LOG_LEVEL = logging.INFO


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "DataSource (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Cookie':
#         'mac_overlay_count=68; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct'
#         '+29+2024+15%3A45%3A00+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87'
#         '%86%E6%97%B6%E9%97%B4)&version=202409.2.0&browserGpcFlag=0&isIABG'
#         'lobal=false&hosts=&consentId=18a3fbdd-e489-4130-a63f-2e54e5cfc53b&'
#         'interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C'
#         '0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1%2COSSTA_B'
#         'G%3A1&intType=1&geolocation=US%3BCA&AwaitingReconsent=false&GPPCoo'
#         'kiesCount=1; OTGPPConsent=DBABLA~BVQqAAAACZA.QA; _ga_38V2BZ2HMF=GS1'
#         '.1.1730187896.30.1.1730187898.58.0.0; _ga=GA1.1.1004982678.17269876'
#         '24; mp_942a098c72ecbdd6c0d9c00fe8308319_mixpanel=%7B%22distinct_id%'
#         '22%3A%20%22%24device%3A19284348610118a-03c0e1ab50492a-48193d01-1ce2'
#         '6a-19284348610118a%22%2C%22%24device_id%22%3A%20%2219284348610118a-03c'
#         '0e1ab50492a-48193d01-1ce26a-19284348610118a%22%2C%22%24initial_refe'
#         'rrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%2'
#         '0%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7'
#         'B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referr'
#         'ing_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%'
#         '22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B'
#         '%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _frPl=5bzHsWqW2S47UmsFs_vCbm-Uwcb'
#         'KgDq5AMkg6rxsDbU; __cfruid=f4362bd1f465dc8dac9f7a33be18a179cab92243-173'
#         '0180995; _sharedid=040b859a-dda4-4cfb-baad-bef07a78be7f; _sharedid_'
#         'cst=zix7LPQsHA%3D%3D; hasConsentedToTerms=yes; FR24SID=9tg0lj25q2qj77'
#         's6amdlbgdc8p33tgt2h23o9kts5klbcj9iquon; _frpk=5bzHsWqW2S47UmsFs_vCb'
#         'g; FCNEC=%5B%5B%22AKsRol_-cpJwKRirOVerAeXfnyGsHOfC97S2qO0yeBeS7BKqeyhq'
#         '4JnJYD9WzTPvgCahAKjIoByl-86kV3xUrbQ-YtD8awyhfZX1shEdT4yTDT99FvMmK0C'
#         'D3ERnzzvefUmqkKMeEf0lyZXeas3c2pR154OGJ-YLlg%3D%3D%22%5D%5D; showAds=ye'
#         's; _cc_id=16e4c66af0153c7eaa43c2aaad6aff6a; _ga_EPEHK8NQRN=GS1.1.172'
#         '8479821.1.0.1728480447.0.0.0; _frc=RYp-qr9AbYk8yL_JyJlEx3-LU8JnwJOV5TC'
#         'nz8xSFF_Ppdq_wpS_IEI2HZ9s0kA-OqnksiLgeHgYWQappoMGw3pyC-btpPvj1XRkQkAZV2'
#         'INQS6cI-yBwAal2k094TW8eDjbHbTDA-hofnZ_F1lU-jKKuTz3czed7Wlt65RiK8WWu9kx'
#         'HLQvJYew-fncrD9ECG9gpdHz-UKZhbaVmbSv4xdoc67DYV-lmi3qlclBK95-a4JBkYey1v'
#         '-RHXQIdbqz; _frr=1; OptanonAlertBoxClosed=2024-09-22T06:47:31.570Z',
#     'Referer':
#         'https://www.flightradar24.com/',
#     'User-Agent':
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
#         '(KHTML, like Gecko) Version/18.0.1 Safari/605.1.15',
#
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "DataSource.middlewares.DatasourceSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "DataSource.middlewares.DatasourceDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "DataSource.pipelines.DatasourcePipeline": 400,
   # "DataSource.pipelines.RoughinfoPipeline": 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
