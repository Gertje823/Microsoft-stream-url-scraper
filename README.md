# Microsoft Streams URL Scraper

This script scrapes all video urls on Microsoft Streams.
It put all the urls in a single text file so you can easaly download the videos with [destreamer](https://github.com/snobu/destreamer)

# How to use

Go [here](https://euno-1.api.microsoftstream.com/api/videos?$top=10&$skip=0&api-version=1.4-private) and copy your Signature and Authorization cookie and put them in the python script.
Now you can run `python3 scrape.py` and the script will scrape al the urls.
Use [destreamer](https://github.com/snobu/destreamer) to download the actual videos.