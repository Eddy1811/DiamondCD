import requests



username = 'Feez'
token = '9317e671cf61cacaf3c9e912a728e7499506837d'
host = 'www.pythonanywhere.com'
domain_name = "Feez.pythonanywhere.com"


response = requests.post(
    'https://{host}/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        host=host, username=username, domain_name = domain_name
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)




response = requests.get(
    'https://{host}/api/v0/user/{username}/cpu/'.format(
        host=host, username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)



#Gestion des codes erreurs
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))