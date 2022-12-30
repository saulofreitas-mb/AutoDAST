from zapv2 import ZAPv2 as ZAP
import time
import requests
import datetime
import os

#target url for scan

target = os.environ['TARGET']
#apikey = '8ij7v7nl0t6d777okrh4kf3icb'  not necessary because api.disablekey=true



zap = ZAP(proxies={'http':'http://127.0.0.1:8090','https':'http://127.0.0.1:8090'})

zap.urlopen(target)



#Passive scan

while (int(zap.pscan.records_to_scan) > 0):

    print ('Passive Scan Records %: ' + zap.pscan.records_to_scan)

    time.sleep(5)



print('Passive Scan Completo..!')

#Active Scan

active_scan_id = zap.ascan.scan(url=target)

time.sleep(5)

while int(zap.ascan.status(active_scan_id)) < 100:

    print ('Active Scan  %: ' + zap.ascan.status())

    time.sleep(5)

print ('Active Scan completo..!')



# HTML Report
with open ('report.html', 'w') as f:f.write(zap.core.htmlreport())
# XML Report
#with open ('report.xml', 'w') as f:f.write(zap.core.xmlreport(apikey = 'apikey'))


zap.core.shutdown()