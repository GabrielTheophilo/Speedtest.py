import speedtest
import json
import urllib
from datetime import datetime
from os.path import exists
import pywhatkit

servers = []
threads = None

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

stringGroup = str(input("Insert group id: "))

messages = ["Good Internet", "Medium Internet", "Low Internet"]


results_dict = s.results.dict()
Url = results_dict['share']
now = datetime.today().hour
nownow = (datetime.today().minute)+1
nownownow = (datetime.today().minute)+2
webUrl = urllib.request.urlretrieve(Url, "000001.jpg")
pywhatkit.sendwhats_image(stringGroup,"000001.jpg","Aqui esta o teste automatizado de hoje",15)

if(results_dict['download']>100000000):
    pywhatkit.sendwhatmsg_to_group(stringGroup, messages[0], now, nownownow)
elif(results_dict['download']>70000000 and results_dict['download']<100000000):
    pywhatkit.sendwhatmsg_to_group(stringGroup, messages[1], now, nownownow)
else:
    pywhatkit.sendwhatmsg_to_group(stringGroup, messages[2], now, nownownow)
    
js = json.dumps(results_dict)
try:
    if (exists("results.json")):
        f = open("results.json", "a")
        f.write(js)
        f.close()
        print("Operation completed successfully")
    else:
        f = open("results.json", "x")
        f.write(js)
        f.close()
        print("Operation completed successfully")
except:
    print("Operation failed")
    

    

    