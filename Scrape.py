import lxml.html
import requests

def scrape(url,id):
    target_url = url
    target_id = id
    result_list = []
    
    target_html = requests.get(target_url).text.encode('utf-8')
    root = lxml.html.fromstring(target_html)
    

    target_oya = root.get_element_by_id('epTabTop')
    target_titles = target_oya.xpath('//ul[@class="topics"]/li/div/p[@class="ttl"]/a/text()')
    #target_titles = target_oya.xpath('//ul[@class="topics"]/li/div/p[@class="ttl"]/a/text()')
    #print len(target_titles)
    for elem in target_titles:
        result_list.append(elem.encode('utf-8'))

    return result_list

    #for elem2 in result_list:
    #        print elem2
    #print 'target_titles',lxml.html.tostring(target_titles, method='text', encoding='utf-8')

    #print list(target_oya.text_content())
    #print lxml.html.tostring(target_oya, method='text', encoding='utf-8')
    #root = lxml.html.parse(target_url).getroot()
    #print root.cssselect('#Main > title')
    #outputtxt = root.cssselect(target_id)[0].text
    #print outputtxt.encode('utf-8')
