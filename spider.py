import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=1"
}
cookies = {
    "BAIDUID": "0BD26C1910B3D3BCF91B0F2D06AC3753:FG=1",
    "BIDUPSID": "0BD26C1910B3D3BCDC2B36CC27021419",
    "PSTM": "1691393924",
    "COOKIE_SESSION": "329_1_5_4_0_9_1_0_5_4_20_2_0_0_0_0_0_1691393938_1692063826^%^7C5^%^230_1_1691393934^%^7C1",
    "ZFY": "Y4gDmGwEu6CIw3ZIsJtcfXuhb9vGe8xEcAVRmHWhgC8:C",
    "BDUSS": "pHV2c4TDdEY2w3N3V2ZW5senNIWGpYOWJVNWtrYkpJcENSdHkwc0ZBYnB4QU5sRVFBQUFBJCQAAAAAAAAAAAEAAACSVl9OaHa94bvpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOk33GTpN9xkMl",
    "BAIDU_WISE_UID": "wapp_1692689656107_117",
    "H_PS_PSSID": "60325_60334_60297",
    "__bid_n": "18e1d5da6849824297ec7f",
    "RT": "z=1&dm=baidu.com&si=5207fc76-a57d-4ba2-b388-028ca180a635&ss=lxa36to2&sl=1&tt=46x&bcn=https^%^3A^%^2F^%^2Ffclog.baidu.com^%^2Flog^%^2Fweirwood^%^3Ftype^%^3Dperf&ld=4z3&ul=11kt&hd=11p6",
    "BD_UPN": "13314752",
    "BA_HECTOR": "2h0404218h8g0ha00h8h2la41ktb5d1j6ljmq1u"
}
url = "https://www.baidu.com/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)
