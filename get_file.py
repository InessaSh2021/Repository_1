import requests

def getdata(passportlist):
  response = requests.get('https://disk.yandex.ru/d/kVdTaY8TuGvBkw')
  if response.status_code == 200:
    print('Success!')
  elif response.status_code == 404:
    print('Not Found.')
  print(response.json())
