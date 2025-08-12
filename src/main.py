import re

import requests
from bs4 import BeautifulSoup


response = requests.get('https://techcrunch.com/')

soup = BeautifulSoup(response.content, 'html.parser')
soupped = soup.prettify()

clean_html = re.sub(r"<script.*?>.*?</script>", "",
                    soupped, flags=re.DOTALL | re.IGNORECASE)


try:
    f = open("db/index.html", "x")
except FileExistsError:
    with open("db/index.html", "w") as f:
        f.write(clean_html)
    print("save to db/index.html")
