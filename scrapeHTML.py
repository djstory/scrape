import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://founders.archives.gov/documents/Hamilton/01-02-02-0051"
req = urllib.request.Request(url)

try:
	with urllib.request.urlopen(req) as f:
		html = f.read()
		soup = BeautifulSoup(html, "html.parser")
		title = BeautifulSoup(str(soup.find(class_="title")), "html.parser")
		body = BeautifulSoup(str(soup.find(class_="docbody")), "html.parser")
		filename = str(title.get_text()).replace(" ", "-").replace(",", "").replace("-[","_").replace("]", "") + ".txt"
		t = str(title.get_text()).replace("From Alexander Hamilton to ", "").split(",")
		recipient = t[0].strip()
		date = t[1].replace("[", "").replace("]", "").strip()
		dateFormat = "%Y-%m-%d"
		#datetime_obj = datetime.strptime(date, dateFormat)
		datetime_obj =datetime.strptime(date, "%d %B %Y")
		filename = str(datetime_obj.date()) + "_to-" + recipient.replace(" ", "-")

		print(filename)
		print(recipient)
		print(datetime_obj.date())
		print(len(body.get_text().split()))
		#print(datetime_obj.date())
		#print(date)

		#with open(filename, "w") as file:
		#	file.write(str(body.get_text()))

		#print("Success")
except:
	print("Failed")