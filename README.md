# Pixiv Manual Fetch
Search and download Pixiv pictures using GitHub Actions

Usage:
1. Go to Actions -> Get Search Result -> Run workflow, and enter the key words and page parameters, and run workflow
2. If you encounter "This version of ChromeDriver only supports Chrome version xx" when running "Get Search Result", please replace ```/chrome/chromedriver``` with [driver file of correct version](http://npm.taobao.org/mirrors/chromedriver/), and try again.
3. Open the same page URL in [https://www.site-shot.com](https://www.site-shot.com) (turn on "full-size") and check whether there are any pictures you want, and find the title or the author.
4. Go to generated HTML file ```dom.html``` in the repo and find the same string of the author or the title. Find the artwork ID nearby.
5. Go to Actions -> Get Picture -> Run workflow, and enter the artwork ID, and run workflow
6. Check out and download the picture you get from the workflow

The sample picture artwork [93990138](https://www.pixiv.net/en/artworks/93990138/) is my very first artwork submitted to Pixiv. (Just a copy draw...) 😜
[![93990138](93990138_%5BCOPY1DRAW%5D1Hello1World-by-No.5972.png)](https://www.pixiv.net/en/artworks/93990138/)
