import requests
import base64

headers = {'User-Agent': 'Mozilla/5.0'}

source = ["https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-SNI-RU-all.txt", 
          "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-checked.txt"]

all_url = []

for url in source:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    print(f"Успех: {url.split('/')[-1]}")
    
    # Извлекаем строки из текущего ответа и добавляем в общий список
    for text_line in response.text.splitlines():
        if text_line.startswith(('vless://', 'trojan://')):
            all_url.append(text_line)

print(f"Найдено ссылок: {len(all_url)}")
for line in all_url:
    print(line)

base64_url = '\n'.join(all_url)
#bytes_data = base64_url.encode('utf-8')
#encoded_bytes = base64.b64encode(bytes_data)
encoded_string = base64.b64encode(base64_url.encode('utf-8')).decode('utf-8')

# Сохраняем в файл
with open('links_base64.txt', 'w', encoding='utf-8') as f:
    #f.write('\n'.(encoded_string))
    f.write(encoded_string)
with open('links_standart', 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_url))
