import requests
import time
import concurrent.futures

TOKEN="eyJraWQiOiJOaUZYdUVxZkFTaXl1eHhBWGJRMDRNbm1hWTYzeHk4akZFVEliRjhLQ3BVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiNDc4YjQ5OC1lMGYxLTcwNDQtMTJhZi1mZjI4NWFlMzQ0NjUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91WjlERjZmRFUiLCJjb2duaXRvOnVzZXJuYW1lIjoidGhvbWFzLnlhbmcyQGdtYWlsLmNvbSIsIm9yaWdpbl9qdGkiOiI5ZTk2ZmM2OC02NmQ2LTRlMjItYjQzYS0wYmYyN2NjZDc3YmEiLCJhdWQiOiIzbzExMHNjZjE0anRjNHFtaWFiaXJqMWN1NyIsImV2ZW50X2lkIjoiNTMyMzY4MzAtYjdhYS00ZWM3LTg0NWMtNmQ0ZDA0ZTNiZmM4IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3NzMyMDcwOTEsImV4cCI6MTc3MzIxMDY5MSwiaWF0IjoxNzczMjA3MDkxLCJqdGkiOiIxMDNmZTNjZC1kODVkLTQwMjEtOWVjZi1iM2QwY2U1OTQ2MGIiLCJlbWFpbCI6InRob21hcy55YW5nMkBnbWFpbC5jb20ifQ.L-mOGXQfxOiz6w4itvnZQcuFDtp11KUPVrTskcc3OdMOPC88vWsP47f4evXwb7OVrx5EThKzm2QgLrcT3z5C4onSrol7dP9YqX1jtTUeeNrYCWI6WQKa2He8HJHTRLWwRvop6EP-Atv6zqinbQEA7vhm8UOlXvRLomrWZZEredz_2KgQsv6LtA6OBsdu4rpsySKABTsBTncpuFjKzFwcFUwJKe5zrKAGPxJE5fe_VFPLpQhXbkYHyzvVpsKX68mdk-o4KsDWYgQC5tuMcJDJjHnUg0qM-fwgLvEUtriA3Dh-zcdiNrUQmUm0n_U2l9plr-LohtBcvbP53qZlmwdlEQ"

EMAIL = "thomas.yang2@gmail.com"

CLIENT_ID = "129hgecjvg1tghuau8de3j1b4m"

API_US = "https://gx55zruuli.execute-api.us-east-1.amazonaws.com"
API_EU = "https://nuuvabun6f.execute-api.eu-west-1.amazonaws.com"

apis = [
    f"{API_US}/greet",
    f"{API_EU}/greet"
]

def call_api(url):

    start = time.time()

    r = requests.post(
        url,
        headers={"Authorization":TOKEN}
    )

    latency = time.time() - start

    return url, r.text, latency

with concurrent.futures.ThreadPoolExecutor() as executor:

    results = executor.map(call_api, apis)

for r in results:
    print(r)