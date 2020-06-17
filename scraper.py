from bs4 import BeautifulSoup
import requests
import datetime
import getPhaseInfo


def goScrapePhase():
    try:
        url = 'https://asafenashville.org/roadmap-for-reopening-nashville'
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

        phaseH3 = str(soup.find('h3'))
        print("\n phaseH3", phaseH3)
        phaseText = phaseH3.split('in ')
        print("\n phaseText", phaseText)
        phaseText2 = ''.join(phaseText[1])
        print("\n phaseText2", phaseText2)
        phaseText3 = phaseText2.split(' of')
        print("\n phaseText3", phaseText3)

        finalPhaseText = phaseText3[0]
        print("\n finalPhaseText", finalPhaseText)

        if finalPhaseText == 'Phase One':
            returnObject = {
                'timestamp': str(TimeNow),
                'phase': finalPhaseText,
                'restrictions': getPhaseInfo.getPhase1Info()
            }
        elif finalPhaseText == 'Phase Two':
            returnObject = {
                'timestamp': str(TimeNow),
                'phase': finalPhaseText,
                'restrictions': getPhaseInfo.getPhase2Info()
            }
        elif finalPhaseText == 'Phase Three':
            returnObject = {
                'timestamp': str(TimeNow),
                'phase': finalPhaseText,
                'restrictions': getPhaseInfo.getPhase3Info()
            }
        elif finalPhaseText == 'Phase Four':
            returnObject = {
                'timestamp': str(TimeNow),
                'phase': finalPhaseText,
                'restrictions': getPhaseInfo.getPhase4Info()
            }

        return returnObject

    except Exception as e:
        print(e)


print('\n', goScrapePhase())
