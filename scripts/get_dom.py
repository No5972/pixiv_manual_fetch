from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from urllib.parse import quote

# Author Page: https://www.pixiv.net/en/users/32490359/artworks?p=1
# Search Page: https://www.pixiv.net/en/tags/keywords/illustrations?s_mode=s_tag&p=1

# Specify these directly in the file
page = '1'
query = quote('バトルスーツ')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
web = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
print("Opening Website...")
web.get('https://www.pixiv.net/en/tags/' + query + '/illustrations?s_mode=s_tag&p=' + page)
sleep(5)
print('Complete load document: ' + 'https://www.pixiv.net/en/tags/' + query + '/illustrations?s_mode=s_tag&p=' + page)
content = web.execute_script('return document.getElementsByTagName("html")[0].outerHTML;')
fo = open("dom.html", "w")
print ("Output HTML: " + fo.name)
fo.write( content )

fo.close()
web.quit()
