# coding:utf-8
import wx
import urllib
import random
import hashlib
import json


class Frame(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='translate', size=(400, 200))
        panel = wx.Panel(self)
        wx.StaticText(panel, label='单词:', pos=(20, 10))
        self.input = wx.TextCtrl(panel, pos=(150, 10))
        wx.StaticText(panel, label='翻译:', pos=(20, 50))
        self.out = wx.TextCtrl(panel, pos=(150, 50))
        self.btn = wx.Button(panel, label='确定', pos=(150, 100), size=(50, 30))
        self.Bind(wx.EVT_BUTTON, self.translate1, self.btn)

    def translate1(self, even):
        q = self.input.GetValue()
        appid = '20180104000112084'
        secretKey = 'UA2xlar2XnJVOEzim7tv'  # 秘钥
        httpClient = None
        myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        m1 = hashlib.md5()
        m1.update(sign.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(q) + '&from=' + \
                fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        response = urllib.urlopen(myurl).read().decode('utf8')
        getJson = json.loads(response)
        getInfo = getJson['trans_result']
        s = getInfo[0]
        re = s['dst']
        self.out.SetValue(re)
        print(re)


if __name__=='__main__':
    app = wx.App()
    frame = Frame(None)
    frame.Show()
    app.MainLoop()