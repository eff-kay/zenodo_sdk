import requests
import pickle
key = open('zonodo_key.txt').read().split('\n')[0]
sandbox_key = open('zenodo_key_sandbox.txt').read().split('\n')[0]

def get_bucket_url(sandbox=True):
  url = 'https://zenodo.org/api/deposit/depositions'
  if sandbox:
      url = 'https://sandbox.zenodo.org/api/deposit/depositions'
      key = sandbox_key
  params = {'access_token':key}
  headers = {'Content-Type': 'application/json'}
 
  print(f'{url} {key}')
  r = requests.post(url, json= {}, params=params, headers=headers)
  print(r.status_code)
  r_data = r.json()
  bucket_url = r_data['links']['bucket']
  dep_id = r_data['id']
  return bucket_url, dep_id

def discard_uploads():
  url = 'https://zenodo.org/api/deposit/depositions/4052321/actions/discard'
  params = {'access_token':key}
  headers = {'Content-Type': 'application/json'}
  
  r = requests.get(url, json= {}, params=params, headers=headers)
  print(r.status_code)
  r_data = r.json()
  
  print(r_data)

def all_depositions(sandbox=True):
  url = 'https://zenodo.org/api/deposit/depositions'
  if sandbox_key:
      url = 'https://sandbox.zenodo.org/api/deposit/depositions'
      key = sandbox_key
  
  params = {'access_token':key}
  headers = {'Content-Type': 'application/json'}
  
  r = requests.get(url, json= {}, params=params, headers=headers)
  print(r.status_code)
  r_data = r.json()
  print(r_data)

def upload_file(bucket_url, file_path, deposition_id='', sandbox=True):
  file_name = file_path.split('/')[-1]
  files = {'file': open(file_path, 'rb')}
  data = {'name': file_name}
  #url = f'https://zenodo.org/api/deposit/depositions/{deposition_id}/files'
  #print(url)
  
  if sandbox:
      key = sandbox_key
  url = f'{bucket_url}/{file_name}'
  params = {'access_token':key}

  print(url)
  with open(file_path, 'rb') as fp:
    r = requests.put(url, data=fp, params=params)
    #r = requests.post(url, data=data,files=files, params=params)

  print(r.json())

if __name__=='__main__':
  #bucket_url, deposition_id = get_bucket_url()
  
  #
  bucket_url = 'https://sandbox.zenodo.org/api/files/40f713e0-57fb-431e-bd96-1f456762970d'
  upload_file(bucket_url, 'test_meta.ini')  
  #discard_uploads()
  #all_depositions()
  print('something')
