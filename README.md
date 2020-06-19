![NashPhase API](https://github.com/cherkesky/NashPhaseAPI/blob/master/nashphase_logo.png)

### by Guy Cherkesky | [LinkedIn](http://linkedin.com/in/cherkesky) | [Website](http://cherkesky.com)

NashPhase API is a simple endpoint that returns back a freshly scraped (once an hour) JSON with Nashville's current reopening phase including the breakdown of all the current restrictions. 

I built this API after I noticed that there is no easy way to get this information programmatically, and also I looked for an excuse to teach myself some AWS technologies. 

<img src="https://github.com/cherkesky/NashPhaseAPI/blob/master/scraper.gif" height="400" width="600">

## Details


#### Technology Stack: 
- Python: BeautifulSoup4
- AWS Roles: Custom IAM Roles (JSON)
- Certificate: Amazon Certificate Manager, DNS Verified
- Lambda: Lambda Function, EventBridge, Python 3.8 Layer
- Storage: AWS S3
- API: Amazon API Gateway, Custom Domain Names, API Mapping
- Version Control: Git, GitHub

#### Lambda Function Implementation: 
https://gist.github.com/cherkesky/ef777c468233fa30757037ebf56c8b8e

### How to consume the API:
Simply hit the endpoint:
### `https://api.cherkesky.com/nashphase/v1`
No API keys or headers needed

Stay Safe & Healthy!
