# coding:utf-8

import hashlib
import urllib
import json
import random
# q = 'translate'

# 百度翻译
def translate(q):
    appid = '20180104000112084'
    secretKey = 'UA2xlar2XnJVOEzim7tv'  # 秘钥
    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    response = urllib.urlopen(myurl).read().decode('utf8')
    getJson = json.loads(response)
    getInfo = getJson['trans_result']
    s = getInfo[0]
    re = s['dst']
    print(re)


# 获得IP所在国家


def getcountry(ip):
    response = urllib.urlopen("http://freegeoip.net/json/" + ip).read().decode('utf-8')
    responsejson = json.loads(response)
    return responsejson.get("country_code")

# 主函数


if __name__ == "__main__":
    print(getcountry("50.78.253.58"))
    while 1:
        print "请输入英文单词"
        words = raw_input()
        translate(words)