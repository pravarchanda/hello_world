import urllib
from bs4 import BeautifulSoup
sock = urllib.urlopen("https://www.snapdeal.com/product/youth-club-brown-analog-watch/672156232420?vendorCode=S580a0&pa=true&fv=true&supc=SDL077300270&isSellerPage=true") 
htmlSource = sock.read()                            
soup = BeautifulSoup(htmlSource, 'html.parser')
product_name=soup.find("h1")
prod_name=product_name.text.strip()
print "name_of_the_product : " + prod_name
avg_rating=soup.find("span",{"class":"avrg-rating"})
print "average-rating : " + avg_rating.text
cut_price = soup.find("div",{"class":"pdpCutPrice"})
cut_pr = cut_price.text.strip()
print "cut-price: " + cut_pr
final_price=soup.find("span",{"class":"pdp-final-price"})
final_price_children = final_price.find("span")
print "final-price: " + final_price_children.text
discount=soup.find("span",{"class":"pdpDiscount"})
dsc = discount.text.strip()
print "discount: " + dsc