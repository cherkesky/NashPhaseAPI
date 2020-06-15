from bs4 import BeautifulSoup
import requests

url ='https://asafenashville.org/roadmap-for-reopening-nashville'

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

phaseH3 = str(soup.find('h3'))
phaseText = phaseH3.split('in')
phaseText2 = ''.join(phaseText[1])
phaseText3 = phaseText2.split('of')
finalPhaseText = phaseText3[0]
print (finalPhaseText)