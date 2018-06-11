from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)

my_url = 'http://www.nasdaq.com/symbol/aapl/option-chain'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


# html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class": "OptionsChain-chart borderAll thin"})
underlying_quote = page_soup.find("div", {"id": "qwidget_lastsale"})


filename = "options.csv"
f = open(filename, "w")

headers = ",,,CALL,,, PUT\nDate, Open Interest, bid, ask, last, Symbol, Strike, last, bid, ask, Open Interest\n "
		
f.write(headers)



for container in containers:
	table_container = container.findAll("tr")


for row in table_container:
	
	td_container = row.findAll("td")
	

	
	for td in td_container:
		
		print("date: " + td_container[0].text)

		
		date = td_container[0].text.strip()
		call_last = td_container[1].text
		call_bid = td_container[3].text
		call_ask = td_container[4].text
		call_oi = td_container[6].text

		symbol = td_container[7].text
		strike = td_container[8].text

		put_last = td_container[10].text
		put_bid = td_container[12].text
		put_ask = td_container[13].text
		put_oi = td_container[15].text





		f.write(date.replace(",", " ") + "," + call_oi + "," + call_bid + "," + call_ask + "," + call_last + "," +  symbol + "," + strike + "," + put_last + ","  + put_bid + "," + put_ask + "," + put_oi + "\n")
		
		break

f.write("\n\nSymbol:," + symbol + "\nLast price:, " + underlying_quote.text +  ",")		


		

	
	

f.close()