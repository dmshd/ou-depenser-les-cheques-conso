# où-depenser-les-cheques-conso

Ok, mais où les dépenser ? L'outil permet de rechercher une catégorie mais à priori ne permet pas visualiser une liste exhaustive de ses catégories de commerces. Certains commerces semblent mis en avant. Difficile d'avoir une vue sur l'ensemble des commerçants. Il faut "jouer" avec la carte, cliquer sur un marqueur pour avoir l'information et passer un certain à chercher quelque chose qui nous intéresse. Ce n'est vraiment pas optimisé pour faciliter l'accès à l'ensemble de l'information par l'utilisateur et je trouve personnellement cela très frustrant.

N'étant pas du tout satisfait de l'outil "passmap_conso" de Sodexo (https://sodexo4you.be/fr/passmap_conso), je décide d'extraire le data pour avoir une vraie liste exhaustive et facilement consultable. Leur moteur de recherche suggère que l'on recherche une catégorie par exemple, alors qu'on a pas de liste exhaustive des catégories. Or, cette information est bien présente dans le JSON qui est apellé.

Je me suis donc demandé s'il était possible d'extraire les data d'une carte intégrée à un site web. Stackoverflow m'indique qu'il faut utiliser l'inspecteur, via l'onglet "Network", en filtrant sur "XHR". Il y a effectivement deux requêtes qui sont effectuées par un code JavaScript vers des endpoints "affiliates" (je suppose qu'il s'agirait de commencers ayant payés pour être vu en premier ?" et "map" qui semble contenir une liste beaucoup plus exhaustive.


## affiliates.json
```
curl 'https://sodexo4you.be/passmap_conso/ajax/affiliates2' \
  -H 'Connection: keep-alive' \
  -H 'Accept: */*' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: https://sodexo4you.be' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://sodexo4you.be/fr/passmap_conso' \
  -H 'Accept-Language: fr-BE,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6' \
  -H 'Cookie: has_js=1' \
  --data-raw 'affiliate%5Bwhere%5D=&affiliate%5Bwhat%5D=&affiliate%5Bproduct%5D=conso&affiliate%5Bpage%5D=0&affiliate%5Bcategory_id%5D=&affiliate%5Bgroup_id%5D=&affiliate%5Baffiliate_id%5D=&affiliate%5Blatitude%5D=50.694827&affiliate%5Blongitude%5D=4.54&affiliate%5Bzoom%5D=8&lang=fr' \
  --compressed > affiliates.json
 ```
 
 ## map.json
``` 
 curl 'https://sodexo4you.be/passmap_conso/ajax/map' \
  -H 'Connection: keep-alive' \
  -H 'Accept: */*' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: https://sodexo4you.be' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://sodexo4you.be/fr/passmap_conso' \
  -H 'Accept-Language: fr-BE,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6' \
  -H 'Cookie: has_js=1' \
  --data-raw 'affiliate%5Bwhere%5D=&affiliate%5Bwhat%5D=&affiliate%5Bproduct%5D=conso&affiliate%5Bpage%5D=0&affiliate%5Bcategory_id%5D=&affiliate%5Bgroup_id%5D=&affiliate%5Baffiliate_id%5D=&affiliate%5Blatitude%5D=50.694827&affiliate%5Blongitude%5D=4.54&affiliate%5Bzoom%5D=8&lang=fr' \
  --compressed > map.json
  ```
## 01-json_to_csv.py
It's just a script that convert all json files he can find in the current directory and convert them to csv recursively.

## 02-get_location_from_lat_lon.py
It's a POC file that reverse Latitude Longitude to full address using geopy.

## 03-json_to_csv_rich.py
Here I am using csv, geopy and the initial json data to generate an enriched file with more data and a google map link for each shop.
