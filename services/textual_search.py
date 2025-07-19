import requests

def search_by_text(api_key: str, text: str) -> dict:
    url = "https://engine.prod.bria-api.com/v1/image-search/textual"
    headers = {
        "api_token": api_key,
        "Content-Type": "application/json"
    }
    data = {"query": text}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
