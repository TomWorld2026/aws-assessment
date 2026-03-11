import requests
import time
import concurrent.futures

TOKEN="eyJraWQiOiJOaUZYdUVxZkFTaXl1eHhBWGJRMDRNbm1hWTYzeHk4akZFVEliRjhLQ3BVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiNDc4YjQ5OC1lMGYxLTcwNDQtMTJhZi1mZjI4NWFlMzQ0NjUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91WjlERjZmRFUiLCJjb2duaXRvOnVzZXJuYW1lIjoidGhvbWFzLnlhbmcyQGdtYWlsLmNvbSIsIm9yaWdpbl9qdGkiOiIyMjJjYjI1Ni03NDcwLTQ5ZTMtYTEyNy1jYzU1NjcwNTE2ZjIiLCJhdWQiOiIxMjloZ2VjanZnMXRnaHVhdThkZTNqMWI0bSIsImV2ZW50X2lkIjoiYmM1YWJiMjMtYTZkZS00YjAyLWJhMGEtMWYwYjdmMTk0NDliIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3NzMxODQ5NTIsImV4cCI6MTc3MzE4ODU1MiwiaWF0IjoxNzczMTg0OTUyLCJqdGkiOiI3Njg0ZTZkMC0wM2E0LTRmYWUtYTI0OC0xNzBjNTZhZTZlZmQiLCJlbWFpbCI6InRob21hcy55YW5nMkBnbWFpbC5jb20ifQ.BFayhgtSa2cYFUThO1_bJPWhsw2Zy-uYDm4PJhfsY-Thj0tFFaIo6vtZfY6uL6FDsjreppB-BL92KuYeIrTb_0P8FukU7WeTrz3YhQWTAjMZRbWQtrhwNh-aq_jgU-7FMP2PeTehGSZvu_G-Sg3MDcUyaanl5ZS-gm2U8WVeZAe42eG4a0l0yaM6cbx3hGOyJG-1uRX_Yv58kQTT0-cyX9YvaUPP3jHktfiiePEBbxdOxmWhyIj1HHWdiOiuVQjfsFCzXMISDXqPx446L847eyaktxmpEwFXc4tZ5LW_4idiB8ipGmu4RuuAiVRxg3zYIw0w58PgC4QotDQFPNt8Rw"

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