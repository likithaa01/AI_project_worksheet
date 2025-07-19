import requests

def search_by_image(api_key: str, image_bytes: bytes) -> dict:
    url = "https://engine.prod.bria-api.com/v1/image-search/visual"
    headers = {
        "api_token": api_key,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url, headers=headers, data=image_bytes)
    response.raise_for_status()
    return response.json()
