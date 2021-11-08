# Pixiv Manual Fetch
Search and download Pixiv pictures using GitHub Actions

Usage:
1. Specify key words and page parameters in ```/scripts/get_dom.py```
2. Run action workflow "Get Search Result" (Actions -> Get Search Result -> Run workflow)
3. If you encounter "This version of ChromeDriver only supports Chrome version xx" when running "Get Search Result", please replace ```/chrome/chromedriver``` with [driver file of correct version](http://npm.taobao.org/mirrors/chromedriver/), and try again.
4. Open the same page URL in [https://www.site-shot.com](https://www.site-shot.com) and check whether there are any pictures you want, and find the title or the author.
5. Go to generated HTML file and find the same string of the author or the title. Find the artwork ID nearby.
6. Specify artwork ID in ```/scripts/get_single_pic.py```
7. Run action workflow "Get Picture"
8. Check out and download the picture you get from the workflow

The sample picture artwork 93990138 is the artwork by myself. 😜
