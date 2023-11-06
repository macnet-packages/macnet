import requests
import sys
import string
url = "https://raw.githubusercontent.com/macnet-packages/macnet-packages/main/" + sys.argv[1]
r = requests.get(url, allow_redirects=True)
open(url.split("/")[-1], 'wb').write(f"/opt/macnet/bin{r.content}")
