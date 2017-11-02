# Url Info


Retrieve full page-load and asset information for a given `url` in `.har` format


## Dependencies

[Python 3.6](https://www.python.org/downloads/release/python-360/)

[Selenium 3.6](https://pypi.python.org/pypi/selenium)  

[BrowserMob Proxy](https://github.com/lightbody/browsermob-proxy)	

[browsermob-proxy-py](https://github.com/AutomatedTester/browsermob-proxy-py)	

## Usage

To get information for the page `'https://en.wikipedia.org/wiki/Python_(programming_language)' and save it as  `wiki.har`:

```
python url_info.py 'wiki' 'https://en.wikipedia.org/wiki/Python_(programming_language)'

```

You can visit this site to check the information in the har file : http://www.softwareishard.com/har/viewer/ or use [Haralyzer](https://pypi.python.org/pypi/haralyzer) to parse the information programatically.