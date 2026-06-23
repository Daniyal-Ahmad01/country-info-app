import requests

def get_country():
    return input("Enter the country of which u want info of: ")


def fetch_info(country): 
  url=f'https://api.restcountries.com/countries/v5?q={country}'
  response = requests.get(
    url,headers={'Authorization': 'Bearer API_KEY'})

  return response.json()


def display_info(data):
  print(f"Country Name: {data['data']['objects'][0]['names']['official']}")
  print(f"Population: {data["data"]["objects"][0]["population"]}")
  print(f"Capital :{data["data"]["objects"][0]["capitals"][0]["name"]}")
  print(f"Currency: {data["data"]["objects"][0]["currencies"][0]["name"]}")
  print(f"Languages: {data["data"]["objects"][0]["languages"][0]["name"]}")



country=get_country()

data=fetch_info(country)

display_info(data)


