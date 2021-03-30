import request
from bs4 import BeautifulSoup

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/"
req = request.get(oyo_url)
content = req.content
soup = BeautifulSoup(content , "html.parser")

 all_hotels = Soup.find_all("div"{"class":"hotelCardListing"})

for hotl in all_hotels:
    hotel_name = hotel.find("h3",{"class":"listingHoyelDescription__hotelName"}).text
    hotel_address = hotel.find("span", {"itemsprop": "streetAddress"}).text
    print(hotel_name,hotel_address)
