from zapv2 import ZAPv2 as ZAP
import time
import requests
import datetime
import os

#target url for scan

target =  os.environ['TARGET']
#apikey = '8ij7v7nl0t6d777okrh4kf3icb'  not necessary because api.disablekey=true

#print(zap._request(  
#  zap.base + 'openapi/action/importFile/',  
#  {'file':'/home/user/openapi.json'}))  
 


zap = ZAP(proxies={'http':'http://127.0.0.1:8090','https':'http://127.0.0.1:8090'})

zap.urlopen(target)

#print(zap._request(  
#  zap.base + 'openapi/action/importUrl/',  
#  {'url':'https://brokencrystals.com/swagger/json'})) 

#Spidering the target
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
# Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

#AJAX SPIDER
print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)

#Passive scan

while (int(zap.pscan.records_to_scan) > 0):

    print ('Passive Scan Records %: ' + zap.pscan.records_to_scan)

    time.sleep(5)



print('Passive Scan Completo..!')
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
print(zap.core.alerts())


#Active Scan

active_scan_id = zap.ascan.scan(url=target)

time.sleep(5)

while int(zap.ascan.status(active_scan_id)) < 100:

    print ('Active Scan  %: ' + zap.ascan.status(active_scan_id))

    time.sleep(5)

print ('Active Scan completo..!')

print('\n'.join(map(str, zap.spider.results(scanID))))

# HTML Report
with open ('report.html', 'w') as f:f.write(zap.core.htmlreport())
# XML Report
#with open ('report.xml', 'w') as f:f.write(zap.core.xmlreport(apikey = 'apikey'))


zap.core.shutdown()