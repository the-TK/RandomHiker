import lxml.html
import requests

#target_url = 'http://www.asahi.com/articles/ASJ3L2TC1J3LUHBI00W.html?iref=comtop_list_int_n03'
#target_html = requests.get(target_url).text.encode('utf-8')
#str（バイト）文字列判定
#print isinstance(target_html,str)

#root = lxml.html.fromstring(target_html)
#root = lxml.html.parse(target_url).getroot()
#print root.cssselect('#Main > title')
#print root.cssselect('title')[0].text
