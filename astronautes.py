import requests

contenu = requests.get("http://api.open-notify.org/astros.json")
print(contenu)
for personne in contenu.json()["people"]:
    if personne['craft'] == 'ISS':
        print(personne)