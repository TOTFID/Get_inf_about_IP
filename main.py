import requests
import folium


def get_inf(ip='some_ip'):
   try:
      resp = requests.get(url=f'http://ip-api.com/json/{ip}').json()
   
      data = {
			'[IP]': resp.get('query'),
			'[Country]': resp.get('country'),
			'[City]': resp.get('city'),
			'[Timezone]': resp.get('timezone'),
			'[Lat]': resp.get('lat'),
			'[Lon]': resp.get('lon')
		}
		
      map = folium.Map(location=[resp.get('lat'),  resp.get('lon')])
      map.save(f'map/{resp.get("query")}_{resp.get("city")}.html')

      for i, v in data.items():
         print(f'{i}:{v}')
         with open('data/file.txt', 'w') as file:
             file.write(str(data))
   except requests.exceptions.ConnectionError: print('Break connect')
