import http.client
import json
DOMAIN = "DOMAIN-SUPER-COOL"
USER_TEST = "bruh"
# el token se proveera por privado!
conn = http.client.HTTPSConnection(DOMAIN)
access_token = "token_given"


# HEADERS deben ir en cada solicitud
auth_headers = {
    'authorization': f"Bearer {access_token}",
    'content-type': "application/json"
}
#para obtener todos los usuarios
conn.request("GET", f"/api/v2/users/{USER_TEST}", headers=auth_headers)
response = conn.getresponse()
print(response.status)
print(response.read().decode("utf-8"))

#para eliminar un usuario en especifico
conn.request("DELETE",f"/api/v2/users/{USER_TEST}", headers=auth_headers)
response = conn.getresponse()
print(response.status)
print(response.read().decode("utf-8"))

#para actualizar un usuario especifico
body_example = {
  "user_id": "auth0|507f1f77bcf86cd799439020",
  "email": "john.doe@gmail.com",
  "email_verified": "false",
  "username": "johndoe",
  "phone_number": "+199999999999999",
  "phone_verified": "false",
  "created_at": "2023-11-07T05:31:56Z",
  "updated_at": "2023-11-07T05:31:56Z",
  "identities": [
    {
      "connection": "<string>",
      "user_id": "abc",
      "provider": "ad",
      "isSocial": "true",
      "access_token": "<string>",
      "access_token_secret": "<string>",
      "refresh_token": "<string>",
      "profileData": {
        "email": "<string>",
        "email_verified": "true",
        "name": "<string>",
        "username": "johndoe",
        "given_name": "<string>",
        "phone_number": "<string>",
        "phone_verified": "true",
        "family_name": "<string>"
      }
    }
  ],
  "app_metadata": {},
  "user_metadata": {},
  "picture": "<string>",
  "name": "<string>",
  "nickname": "<string>",
  "multifactor": [
    "<string>"
  ],
  "multifactor_last_modified": "2023-11-07T05:31:56Z",
  "last_ip": "<string>",
  "last_login": "2023-11-07T05:31:56Z",
  "last_password_reset": "2023-11-07T05:31:56Z",
  "logins_count": 123,
  "blocked": "true",
  "given_name": "<string>",
  "family_name": "<string>"
}
#también puedes solamente seleccionar un campo en concreto, el body example especifica todo lo que se puede editar
conn.request("PATCH", f"/api/v2/users/{USER_TEST}", headers=auth_headers, body=json.dumps(body_example))
response = conn.getresponse()
print(f"STATUS: {response.status}")
print(response.read().decode("utf-8"))

#body común para los roles
body = {
   "roles":["rol_id"]
}
#para borrar roles
conn.request("POST", f"/api/v2/users/{USER_TEST}/roles", headers=auth_headers, body=json.dumps(body))
response = conn.getresponse()
print(f"POST STATUS: {response.status}")
print(response.read().decode("utf-8"))


#para actualizar los roles de un usuario
conn.request("POST", f"/api/v2/users/{USER_TEST}/roles", headers=auth_headers, body=json.dumps(body))
response = conn.getresponse()
print(f"POST STATUS: {response.status}")
print(response.read().decode("utf-8"))

#para obtener los roles de un usuario
conn.request("GET", f"/api/v2/users/{USER_TEST}/roles", headers=auth_headers)
response = conn.getresponse()
print(f"GET STATUS: {response.status}")
print(response.read().decode("utf-8"))
conn.close()
