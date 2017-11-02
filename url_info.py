# -*- coding: utf-8 -*-

# DISCLAIMER:

# IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

Application to retrieve url-page load infomation and store it in a .har-type file

@author: ioanniskbreier@gmail.com
"""
import json
from selenium import webdriver
from browsermobproxy import Server


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
    server = Server("/path/to/browsermob-proxy")
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
    name = 'wiki'
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    result = get_har_file(url, name)
    save_to_file(result, name)
