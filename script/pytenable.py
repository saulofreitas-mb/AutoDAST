from tenable.io import TenableIO
import os


tio = TenableIO (
access_key = os.environ['TENABLE_ACCESS_KEY'],
secret_key = os.environ['TENABLE_SECRET_KEY'])

scans = tio.scans.list()
for scan in scans:
    print(f'Scan {scan["id"]} is named {scan["name"]}')

scan = tio.scans.create(
    name='External Example Scan',
    targets=['https://brokencrystals.com/']
)
tio.scans.launch(scan['id'])    