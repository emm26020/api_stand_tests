import configuration
import requests
import data

def post_new_user(body):
    return requests.post(f'https://cnt-153b7181-209c-4611-ba35-7bdd4b3c6344.containerhub.tripleten-services.com/api/v1/users/',
    json=body,
    headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)