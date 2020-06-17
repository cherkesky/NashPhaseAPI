from bs4 import BeautifulSoup
import requests, datetime

url ='https://asafenashville.org/roadmap-for-reopening-nashville'
headers = {
    'authority': 'scrapeme.live',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
} 

source = requests.get(url, headers=headers).text
soup = BeautifulSoup(source, features='html.parser')
TimeNow = datetime.datetime.now()

phase1Table = soup.find('h2', id="phaseone").next_sibling.next_sibling
phase2Table = soup.find('h2', id="phasetwo").next_sibling.next_sibling
phase3Table = soup.find('h2', id="phasethree").next_sibling.next_sibling
phase4Table = soup.find('h2', id="phasefour").next_sibling.next_sibling

def getPhase1Info():
  phaseInfoList = []
  for h4 in phase1Table.findAll('tr'):
    phaseTempDictionary = {}
    phaseTempDictionaryKey = ""
    phaseTempLi =""
    phaseTempDictionaryValue=[]
    currentH4 = h4.find_next('h4')
    phaseTempDictionaryKey = currentH4.text
    phaseTempLi = currentH4.find_next('ul')
    
    for li in phaseTempLi.findAll('li'):
      noCommasLi = str(li.text).replace(',', '')
      noXa0Li = noCommasLi.replace('\xa0', ".")
      phaseTempDictionaryValue.append(noXa0Li)
    phaseTempDictionary[phaseTempDictionaryKey]=phaseTempDictionaryValue
    phaseInfoList.append(phaseTempDictionary)
  return (phaseInfoList)

def getPhase2Info():
  phaseInfoList = []
  for h4 in phase2Table.findAll('tr'):
    phaseTempDictionary = {}
    phaseTempDictionaryKey = ""
    phaseTempLi =""
    phaseTempDictionaryValue=[]
    currentH4 = h4.find_next('h4')
    phaseTempDictionaryKey = currentH4.text
    phaseTempLi = currentH4.find_next('ul')
    
    for li in phaseTempLi.findAll('li'):
      noCommasLi = str(li.text).replace(',', '')
      noXa0Li = noCommasLi.replace('\xa0', ".")
      phaseTempDictionaryValue.append(noXa0Li)
    phaseTempDictionary[phaseTempDictionaryKey]=phaseTempDictionaryValue
    phaseInfoList.append(phaseTempDictionary)
  return (phaseInfoList)

def getPhase3Info():
  phaseInfoList = []
  for h4 in phase3Table.findAll('tr'):
    phaseTempDictionary = {}
    phaseTempDictionaryKey = ""
    phaseTempLi =""
    phaseTempDictionaryValue=[]
    currentH4 = h4.find_next('h4')
    phaseTempDictionaryKey = currentH4.text
    phaseTempLi = currentH4.find_next('ul')
    
    for li in phaseTempLi.findAll('li'):
      noCommasLi = str(li.text).replace(',', '')
      noXa0Li = noCommasLi.replace('\xa0', ".")
      phaseTempDictionaryValue.append(noXa0Li)
    phaseTempDictionary[phaseTempDictionaryKey]=phaseTempDictionaryValue
    phaseInfoList.append(phaseTempDictionary)
  return (phaseInfoList)

def getPhase4Info():
  phaseInfoList = []
  for h4 in phase4Table.findAll('tr'):
    phaseTempDictionary = {}
    phaseTempDictionaryKey = ""
    phaseTempLi =""
    phaseTempDictionaryValue=[]
    currentH4 = h4.find_next('h4')
    phaseTempDictionaryKey = currentH4.text
    phaseTempLi = currentH4.find_next('ul')
    
    for li in phaseTempLi.findAll('li'):
      noCommasLi = str(li.text).replace(',', '')
      noXa0Li = noCommasLi.replace('\xa0', ".")
      phaseTempDictionaryValue.append(noXa0Li)
    phaseTempDictionary[phaseTempDictionaryKey]=phaseTempDictionaryValue
    phaseInfoList.append(phaseTempDictionary)
  return (phaseInfoList)