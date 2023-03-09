import os
from tenable_io.client import TenableIOClient

client = TenableIOClient(access_key=os.environ['TENABLE_ACCESS_KEY'], secret_key=os.environ['TENABLE_SECRET_KEY'])
scan = client.scan_helper.create(name='Saulo AUTODAST SCAN}', text_targets='http://brokencrystals.com/', template='basic')
scan.launch().download('Saulo_AUTODAST_SCAN.pdf', scan.histories()[0].history_id) 




# tio = TenableIO (
# vendor= 'Saulo Freitas',
# product='scan ',    
# access_key = os.environ['TENABLE_ACCESS_KEY'],
# secret_key = os.environ['TENABLE_SECRET_KEY'])

# scans = tio.scans.list()
# for scan in scans:
#     print(f'Scan {scan["id"]} is named {scan["name"]}')

# scan = tio.scans.create(
#     name='External Example Scan',
#     targets=['https://brokencrystals.com/']
# )
# tio.scans.launch(scan['id'])    
