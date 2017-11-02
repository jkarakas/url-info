# -*- coding: utf-8 -*-
"""
Application to retrieve url-page load infomation and store it in a .har-type file

@author: ioanniskbreier@gmail.com
"""

import json
from selenium import webdriver
from browsermobproxy import Server
import sys
import os


def get_har_file(url, name):
    """Retrieve page-load information and save as a .har file

    Parameters
    ----------
    url : string
        page url to get the load informtion for
    name : string
        the name of the har file that wil be used

    Returns
    -------
    result : json
        the har file in json format
    """

    # Start a a browserobproxy server instance
    server = Server("./browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()

    # configure selenium webdriver to use chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    chrome_options.add_argument("--disable-infobars")
    browser = webdriver.Chrome(chrome_options=chrome_options)

    # extract the har file
    proxy.new_har(name)
    browser.get(url)
    proxy.har  # returns a HAR JSON blob

    # Convert to json and quit
    result = json.dumps(proxy.har, ensure_ascii=False)
    server.stop()
    browser.quit()

    return result


def save_to_file(result, name):
    """Save result to disk as a .har file

    Parameters
    ----------
    result : json object
        retrieved har in json format
    name : string
        the name of the har file that wil be used

    Returns
    -------
    """
    myFile = open(f'{name}.har', 'w')
    myFile.write(str(result))
    myFile.close()


if __name__ == "__main__":
    # name = 'wiki'
    # url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    name = str(sys.argv[1])
    url = str(sys.argv[2])
    result = get_har_file(url, name)
    save_to_file(result, name)
    print(f'Url load and asset information succesfully retrieved and saved at path {os.path.realpath(name)}.har')
