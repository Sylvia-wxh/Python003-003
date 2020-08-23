# Scrapy settings for maoyanone project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyanone'

SPIDER_MODULES = ['maoyanone.spiders']
NEWSPIDER_MODULE = 'maoyanone.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'maoyanone (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
    'Cookie': '__mta=120028983.1593306417025.1593328161781.1593328782311.6; uuid_n_v=v1; uuid=A8E24090B8DB11EA97185D50074468A7AD136205F3834F5588B9FFE0B8978DFB; _csrf=2ba9f02a91105f6413cf4a4b471ec45e80a5aa26ed18d6a66837decbd673ac03; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593306417; mojo-uuid=9a19d0f417bd6ba12509d96bc0f89e3b; _lxsdk_cuid=172f8768738c8-0d70d070e88c78-4353760-1fa400-172f8768738c8; _lxsdk=A8E24090B8DB11EA97185D50074468A7AD136205F3834F5588B9FFE0B8978DFB; mojo-session-id={"id":"ff9cc14c607982f5f9b67cd983da1b3e","time":1593328161635}; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593329047; __mta=120028983.1593306417025.1593328782311.1593329047002.7; _lxsdk_s=172f9c250de-024-d31-ab9%7C%7C11'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyanone.middlewares.MaoyanoneSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyanone.middlewares.MaoyanoneDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyanone.pipelines.MaoyanonePipeline': 300,
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
