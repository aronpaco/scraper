import requests

url_list = [
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=GqjPP2zRcEitEbsK4wsFXw',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=QTpJ4JPuyk2TMdNpor368g',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=cCSb7rnbxUuc8c-fFPza4A',
]

for url in url_list:
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Successfully processed {url}")
        else:
            print(f"Failed to process {url} with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing {url}: {str(e)}")
