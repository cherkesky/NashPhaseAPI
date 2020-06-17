from bs4 import BeautifulSoup
import requests, datetime, getPhaseInfo

def goScrapePhase ():
  try:
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
        'all_residents': ['Age 65+ and High-risk stay at home', 'All work from home if possible','All residents wear masks in public', 'Schools closed', 'No gatherings over 10'],
        'restaurants_and_bars_serving_food': ['Open at 1/2 capacity', 'Clean all surfaces after every use', 'Employees screened daily and required to wear face masks', 'Bar areas closed and no live music'],
        'bars_and_entertainment_venues':['Closed'],
        'retail_stores_and_commercial_businesses': ['Open at 1/2 capacity', 'Employees screened daily and wear masks'],
        'nail_salons_hair_salons_massage_etc': ['Closed'],
        'healthcare_and_dental': ['Follow State of Tennessee Guidance'],
        'gyms_and_fitness': ['Closed'],
        'playgrounds_tennis_and_basketball_courts': ['Closed'],
        'sports_venues': ['Closed']
      }
    elif finalPhaseText == 'Phase Two':
        returnObject = {
        'timestamp': str(TimeNow),
        'phase': finalPhaseText,
        'restrictions': getPhaseInfo.getPhase2Info()
        # 'all_residents': ['Age 65+ and High-risk stay at home', 'All work from home if possible','All residents wear masks in public', 'Schools closed', 'Small gatherings up to 25'],
        # 'restaurants_and_bars_serving_food': ['Open at 1/2 capacity', 'Clean all surfaces after every use', 'Employees screened daily and required to wear face masks', 'Bar areas remain closed', 'Live entertainment allowed with proper social distancing –  dance floors remain closed'],
        # 'socially_driven_businesses': ['Closed','This includes: Bars, clubs, karaoke bars, tours,  transportainment, live entertainment'],
        # 'bars_and_entertainment_venues':['Closed'],
        # 'retail_stores_and_commercial_businesses': ['Open at 1/2 capacity', 'Customers in waiting areas count towards capacity totals', 'Employees screened daily and wear masks' ],
        # 'personal_care_services_nail_salons_hair_salons_massage_tattoo_tanning_etc': ['Open at 1/2 capacity','Customers in waiting areas count towards capacity totals','Employees screened daily and wear masks'],
        # 'healthcare_and_dental': ['Follow State of Tennessee Guidance'],
        # 'gyms_fitness_and_recreation': ['Metro Parks may reopen community centers, golf course clubhouses, museums, Sportsplex and nature centers at 50% capacity.', 'Tennis courts are now open with social distancing.', 'Dog parks, basketball courts, playgrounds, sports and recreations leagues, skate parks and splash pads shall remain closed.' ],
        # 'museums_and_attractions': ['Open at 1/2 capacity', 'Employees screened daily and required to wear face masks', 'Interactive exhibits closed', 'Arcades closed', 'Tours closed'],
        # 'day_camps': ['Buses run at 1/2 capacity', 'Employees screened daily and required to wear face masks', 'Cafeterias closed; packed or box lunches only', 'No overnight camps' ],
        # 'large_sports_and_entertainment_venues':['Closed']
      }
    elif finalPhaseText == 'Phase Three':
            returnObject = {
            'timestamp': str(TimeNow),
            'phase': finalPhaseText,
            'all_residents': ['Age 65+ and High-risk stay at home', 'All work from home if possible','All residents wear masks in public', 'Nonresidential K-12 schools can reopen', 'Gathering size to be determined (including but not limited to events, meetings, weddings, etc.'],
            'restaurants_and_bars_serving_food': ['Open at full capacity', 'Clean all surfaces after every use', 'Employees screened daily and required to wear face masks', 'Bars open at 1/2 capacity; no standing at bars', 'Live music permitted with proper social distancing'],
            'socially_driven_businesses': ['Open at 1/2 capacity','This includes: Bars, clubs, karaoke bars, tours, transportainment, live entertainment'],
            'retail_stores_and_commercial_businesses': ['Open at full capacity','Employees screened daily and wear masks'],
            'personal_care_services_nail_salons_hair_salons_massage_tattoo_tanning_etc': ['Open at full capacity','Employees screened daily and wear masks'],
            'healthcare_and_dental': ['Follow State of Tennessee Guidance'],
            'gyms_fitness_and_recreation_order_2': ['Open at 3/4 capacity', 'Employees screened daily','Limit use of shared equipment', 'For aerobic activities, increase social distancing to 10 ft.','Pools open at 3/4 capacity', 'Sports facilities open', 'Playgrounds open', 'Recreation leagues open'],
            'museums_and_attractions': ['Open at 3/4 capacity', 'Employees screened daily and required to wear face masks', 'Interactive exhibits open', 'Arcades open at 1/2 capacity', 'Tours open 1/2 capacity'],
            'day_camps': ['Buses run at full capacity', 'Employees screened daily and required to wear face masks', 'Cafeterias closed; packed or box lunches only'],
            'large_sports_and_entertainment_venues':['Closed']
          }
    elif finalPhaseText == 'Phase Four':
                returnObject = {
                'timestamp': str(TimeNow),
                'phase': finalPhaseText,
                'all_residents': ['Age 65+ and High-risk stay at home', 'All work from home if possible','Wearing masks is optional, but recommended', 'Nonresidential K-12 schools can reopen', 'Gatherings sizes to be determined'],
                'restaurants_and_bars_serving_food': ['Open at full capacity', 'Clean all surfaces after every use', 'Employees screened daily','Employees wearing masks is optional, but recommended', 'Bars open at full capacity'],
                'socially_driven_businesses': ['Open at full capacity','This includes: Bars, clubs, karaoke bars, tours, transportainment, live entertainment'],
                'retail_stores_and_commercial_businesses': ['Open at full capacity','Employees screened daily', 'Employees wearing masks is optional, but recommended'],
                'personal_care_services_nail_salons_hair_salons_massage_tattoo_tanning_etc': ['Open at full capacity','Employees wearing masks is optional, but recommended'],
                'healthcare_and_dental': ['Follow State of Tennessee Guidance'],
                'gyms_fitness_and_recreation_order_2': ['Open at full capacity', 'Clean equipment after every use', 'Employees screened daily','Employees wearing masks is optional, but recommended', 'Pool open at full capacity', 'Sports courts open'],
                'museums_and_attractions': ['Open at full capacity', 'Employees screened daily and required to wear face masks', 'Interactive exhibits open', 'Arcades open', 'Tours open'],
                'day_camps': ['Buses run at full capacity', 'Employees screened daily and required to wear face masks', 'Cafeterias open' 'Overnight camps open'],
                'large_sports_and_entertainment_venues':['Open at full capacity', 'Employees screened daily', 'Employees wearing masks is optional, but recommended']
              }

    return returnObject

  except Exception as e: print(e)

print('\n', goScrapePhase())