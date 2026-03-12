import requests

with open("sources.json", "r", encoding="utf-8") as f:
    sources = [line.strip() for line in f if line.strip() and not line.startswith("#")]


#raw_url = "https://github.com/igareck/vpn-configs-for-russia/raw/main/WHITE-SNI-RU-all.txt"

headers = {'User-Agent': 'Mozilla/5.0'}

source = ["https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-SNI-RU-all.txt", 
          "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-checked.txt"]

#for line in source:
#    response = requests.get(line, headers=headers)
#    response.encoding = 'utf-8'
#    print("успех")

all_url = []

for url in source:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    print(f"Успех: {url.split('/')[-1]}")
    
    # Извлекаем строки из текущего ответа и добавляем в общий список
    for text_line in response.text.splitlines():
        if text_line.startswith(('vless://', 'trojan://')):
            all_url.append(text_line)

# Извлекаем строки, начинающиеся с vless:// или trojan://
#links = []
#for line in response.text.splitlines():
#    if line.startswith(('vless://', 'trojan://')):
#        links.append(line)

print(f"Найдено ссылок: {len(all_url)}")
for line in all_url:
    print(line)

# Сохраняем в файл
with open('vless_links.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_url))
