MYSQL_DB = {

}

#REDIS = {
#     'url': None,
# #     'host': '',
#     'host': '',
#     'port': ,
#     'password': ''
#     }


BXS_COOKIE_POOL = 'bxs_cookies' # HASH
MOBILE_UA_POOL = 'mobile_ua'    # LIST
HTTPS_PROXY_IP_POOL = 'https_proxy' # HASH
BXS_RESOURCE_POOL = 'bxs_resource'  # LIST
INVALID_BXS_RESOURCE_POOL = 'invalid_bxs_resource' # LIST
INVALID_BXS_RESOURCE_HISTORY_POOL = 'invalid_history_bxs_resource' # LIST
INVALID_BXS_COOKIE_HISTORY_POOL = 'invalid_history_bxs_cookie' # HASH
INVALID_BXS_PROXY_HISTORY_POOL = 'invalid_history_bxs_proxy' # HASH

CHECK_INVALID_POOL_CYCLE = 30
CHECK_RESOURCE_POOL_CYCLE = 60
TEST_RESOURCE_CYCLE = 60
FILL_RESOURCE_THRESHOLD = 25

# PROXY_REQUEST_URL = 'http://webapi.http.zhimacangku.com/getip?type=2&pro=&city=0&yys=0&port=11&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions=&'
# PROXY_REQUEST_URL = 'http://webapi.http.zhimacangku.com/getip?type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='

#PROXY_REQUEST_URL = 'http://webapi.http.zhimacangku.com/getip?type=2&pro=&city=0&yys=0&port=1&pack=44051&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
#PROXY_REQUEST_URL = 'http://http.tiqu.qingjuhe.cn/getip?type=2&pro=&city=0&yys=0&port=11&pack=28637&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=0&regions='
PROXY_REQUEST_URL = 'http://http.tiqu.qingjuhe.cn/getip?type=2&pro=&city=0&yys=0&port=11&pack=29237&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=0&regions='
PROXY_REQUEST_CHUNK = 25

PROXY_TABLE = 'proxy_zhima'
