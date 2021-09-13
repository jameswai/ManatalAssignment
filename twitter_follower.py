import requests
from bs4 import BeautifulSoup


url = input('Input your account link on Twitter: ') 
req = requests.get(url)

bs = BeautifulSoup(req.text,'html.parser')


try:
    follower_count = bs.find_all('span', {'class' : 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'}) 
    print("{} Followers".format(follower_count))

except:
    print('Account name not found...')
  