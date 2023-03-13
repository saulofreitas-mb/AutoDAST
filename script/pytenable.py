import os
from tenable_io.client import TenableIOClient

client = TenableIOClient(access_key=os.environ['TENABLE_ACCESS_KEY'], secret_key=os.environ['TENABLE_SECRET_KEY'])
scan = client.scan_helper.create(name='Saulo AUTODAST SCAN}', text_targets=['http://brokencrystals.com/'], template='basic')
scan.launch().download('Saulo_AUTODAST_SCAN.pdf', scan.histories()[0].history_id) 







# Internal scans

# from tenable_io.client import TenableIOClient
# from tenable_io.api.scans import ScanCreateRequest
# from tenable_io.api.models import ScanSettings
# client = TenableIOClient(access_key='{YOUR ACCESS KEY}', secret_key='{YOUR SECRET KEY}')
# scanners = {scanner.name: scanner.id for scanner in client.scanners_api.list().scanners}
# template = client.scan_helper.template(name='basic')
# scan_id = client.scans_api.create(
#  ScanCreateRequest(
#  template.uuid,
#  ScanSettings(
#  ‘{YOUR SCAN NAME}’,
#  ‘{YOUR SCAN TARGETS}’,
#  scanner_id=scanners['{YOUR SCANNER NAME}']
#  )
#  )
# )
# scan = client.scan_helper.id(scan_id)
# scan.launch()



#another implementation
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
