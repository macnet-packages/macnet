import requests
import sys
import string
try:
    url = "https://raw.githubusercontent.com/macnet-packages/macnet-packages/main/" + sys.argv[1]
    r = requests.get(url, allow_redirects=True)
    open(url.split("/")[-1], 'wb').write(f"/opt/macnet/bin{r.content}")
except IndexError:
    print("Usage: macnet <package>")
except KeyboardInterrupt:
    print("Exiting on user request.")
except:
    print("Somthing went wrong, an that's all we know.")

