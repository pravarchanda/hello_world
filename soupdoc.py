import time
import subprocess
import urllib
from bs4 import BeautifulSoup
while True:
    sock = urllib.urlopen("http://www.espncricinfo.com/ci/engine/match/index.html?view=live") 
    htmlSource = sock.read()                            
    soup = BeautifulSoup(htmlSource, 'html.parser')
    data=soup.find("div",{"class":"innings-info-1"})
    print data.contents[0]
    children = data.find("span")
    y = children.text
    subprocess.Popen(['notify-send',y])
    print children.text
    time.sleep(5)
