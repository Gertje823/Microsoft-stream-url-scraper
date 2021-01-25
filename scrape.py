import re, json, requests

cookies = {'Signature':'YOUR_SIGNATURE_COOKIE','Authorization': 'YOUR_AUTHORISATION_COOKIE'}
skip = 0
urls = True
while urls:
    url = f"https://euno-1.api.microsoftstream.com/api/videos?$top=100&$skip={skip}&api-version=1.4-private"
    r = requests.get(url, cookies=cookies)

    data = r.json()
    if not 'value' in data or len(data['value']) == 0:
        urls = False
    f= open("url.txt","a")
    print(skip)
    for video in data['value']:
        id = video['id']
        print(id)
        video_url=f"https://web.microsoftstream.com/video/{id}\n"
        f.write(video_url)
    skip+=100