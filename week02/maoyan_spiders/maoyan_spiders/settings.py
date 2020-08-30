# Scrapy settings for maoyan_spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan_spiders'

SPIDER_MODULES = ['maoyan_spiders.spiders']
NEWSPIDER_MODULE = 'maoyan_spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 用random user agent
from fake_useragent import UserAgent
USER_AGENT = UserAgent().chrome

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
    'Cookie': '__mta=146119307.1597673420335.1597936594203.1597936642218.11; uuid_n_v=v1; uuid=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; mojo-uuid=aa9712850706c7e51a8894479bdf751a; _lxsdk_cuid=173fcc1b5d0c8-05591201a0b616-b7a1334-100200-173fcc1b5d0c8; _lxsdk=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; _csrf=ffd2b0f4f7176c4788b99810b3b5066039ec8522edd9e88b652305a37c33cec7; mojo-session-id={"id":"6fcfbd3bf79462d361bb1ef2872fab52","time":1597935738498}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597754709,1597847150,1597912637,1597935739; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597936698; __mta=146119307.1597673420335.1597936642218.1597936697980.12; mojo-trace-id=26; _lxsdk_s=1740c645f01-42a-862-7e5%7C%7C39'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan_spiders.middlewares.MaoyanSpidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'maoyan_spiders.middlewares.MaoyanSpidersDownloaderMiddleware': 543,
    'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'maoyan_spiders.middlewares.RandomHttpProxyMiddleware': 400,
}

HTTP_PROXY_LIST= [
    'http://175.42.122.186:9999',
    'http://115.218.211.79:9000'
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'maoyan_spiders.pipelines.MaoyanSpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
