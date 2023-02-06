from zapv2 import ZAPv2 as ZAP
import time
import requests
import datetime
import os
import urllib
#target url for scan

target =  os.environ['TARGET']
context_name = 'Default Context'
#apikey = '8ij7v7nl0t6d777okrh4kf3icb'  not necessary because api.disablekey=true

 


zap = ZAP(proxies={'http':'http://127.0.0.1:8090','https':'http://127.0.0.1:8090'})

zap.urlopen(target)

# local file api definition approach
#print(zap._request(  
#  zap.base + 'openapi/action/importFile/',  
#  {'file':'/home/user/openapi.json'}))  

#url approach
print(zap._request(  
  zap.base + 'openapi/action/importUrl/',  
  {'url':'https://brokencrystals.com/swagger/json'})) 

#auth functions
def set_include_in_context():
    #exclude_url = 'http://localhost:8090/bodgeit/logout.jsp'
    include_url = 'http://brokencrystals.*'
    zap.context.include_in_context(context_name, include_url)
    #zap.context.exclude_from_context(context_name, exclude_url)
    print('Configured include and exclude regex(s) in context')


def set_logged_in_indicator():
    logged_in_regex = '\Q<a class="get-started-btn scrollto" href="/">Log out test admin</a>\E'
    zap.authentication.set_logged_in_indicator(context_name, logged_in_regex)
    print('Configured logged in indicator regex: ')


def set_form_based_auth():
    login_url = 'https://brokencrystals.com/userlogin'
    login_request_data = 'username={%username%}&password={%password%}'
    form_based_config = 'loginUrl=' + urllib.parse.quote(login_url) + '&loginRequestData=' + urllib.parse.quote(login_request_data)
    zap.authentication.set_authentication_method(context_name, 'formBasedAuthentication', form_based_config)
    print('Configured form based authentication')


def set_user_auth_config():
    user = 'Test admin'
    username = 'admin'
    password = 'admin'

    user_id = zap.users.new_user(context_name, user)
    user_auth_config = 'user=' + urllib.parse.quote(username) + '&password=' + urllib.parse.quote(password)
    zap.users.set_authentication_credentials(context_name, user_id, user_auth_config)
    zap.users.set_user_enabled(context_name, user_id, 'true')
    zap.forcedUser.set_forced_user(context_name, user_id)
    zap.forcedUser.set_forced_user_mode_enabled('true')
    print('User Auth Configured')
    return user_id


def start_spider(user_id):
    zap.spider.scan_as_user(context_name, user_id, target_url, recurse='true')
    print('Started Scanning with Authentication')


set_include_in_context()
set_form_based_auth()
set_logged_in_indicator()
user_id_response = set_user_auth_config()
start_spider(user_id_response)




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
#print(zap.core.alerts())


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