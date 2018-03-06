# lesson 55~56 are important for making net spider
# change header
# 1: Request.headers
# 2: Request.add_header()

# change visit rate
# using time module
import time
time.sleep(5)

# 代理
import urllib
# 1: make a proxy handler
proxy_support =  urllib.request.ProxyHandler({"http":"119.3.122.23:88"}) # ProxyHandler(p1), p1 is a dictionary of {"web type. for example:http,file":"ip : port id"}
# 2: create an opener
opener = urllib.request.build_opener(proxy_support)
# 3(long term solution): install opener
urllib.request.install_opener(opener)
# 3(short term solution): open(p1) method. p1 is the url
opener.open("url")