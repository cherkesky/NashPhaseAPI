from bs4 import BeautifulSoup
import requests

source = requests.get('https://asafenashville.org/roadmap-for-reopening-nashville').text

soup = BeautifulSoup(source, 'lxml')

phase = str(soup.find('h3'))
phaseText = phase.split('in')
phaseText2 = ''.join(phaseText[1])
phaseText3 = phaseText2.split('of')
print (phaseText3[0])