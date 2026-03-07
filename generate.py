import requests
import base64

sources = open("sources.txt").read().splitlines()

nodes = []

for url in sources:
    try:
        r = requests.get(url, timeout=20)
        text = r.text

        try:
            text = base64.b64decode(text).decode()
        except:
            pass

        for line in text.splitlines():
            if line.startswith(("vless://","vmess://","trojan://","ss://")):
                nodes.append(line.strip())

    except:
        pass

nodes = list(set(nodes))

with open("sub.txt","w") as f:
    f.write("\n".join(nodes))

encoded = base64.b64encode("\n".join(nodes).encode()).decode()

with open("sub_base64.txt","w") as f:
    f.write(encoded)