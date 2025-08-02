import requests

response = requests.get("https://discordbot-na7u.onrender.com")
if response.ok:
    data = response.json()
    for embed in data:
        print("Title:", embed.get("title"))
        print("Description:", embed.get("description"))
        for field in embed.get("fields", []):
            print(f"{field['name']}: {field['value']}")
        print("---")
