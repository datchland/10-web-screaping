from bs4 import BeautifulSoup
html="""
<a href="/product-1">P1</a>
<a href="/login">L</a>
<img src="a.jpg">
<img src="b.png">
<div class="phone samsung">
</div>
"""
soup=BeautifulSoup(html,"html.parser")
print(soup.select("a"))

print(soup.select('a[href]')) # exist href attribute

print(soup.select('a[href="/login"]')) # exact

print(soup.select('a[href^="/product-"]')) # strat with

print(soup.select('a[href*="/product-"]')) # contains

print(soup.select('img[src$=".jpg"]')) # end with

print(soup.select(".phone.samsung"))
