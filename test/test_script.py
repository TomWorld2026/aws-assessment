import requests
import time
import concurrent.futures

TOKEN="JWT_TOKEN"

apis = [
    "API_US/greet",
    "API_EU/greet"
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