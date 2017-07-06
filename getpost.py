import urllib
import urllib2

params = urllib.urlencode(dict({'hello': 'there'}))
myurl = 'http://127.0.0.1:5000/'

# GET is the default action
response = urllib2.urlopen(myurl+params)  

# Output from the GET assuming response code was 200
data = response.read() 
print data