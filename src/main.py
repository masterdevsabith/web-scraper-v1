import re

import requests
from bs4 import BeautifulSoup


response = requests.get('https://techcrunch.com/')

soup = BeautifulSoup(response.content, 'html.parser')
soupped = soup.prettify()

clean_html = re.sub(r"<script.*?>.*?</script>", "",
                    soupped, flags=re.DOTALL | re.IGNORECASE)


print(clean_html)
try:
    f = open("index.html", "x")
except FileExistsError:
    with open("index.html", "w") as f:
        f.write(clean_html)
