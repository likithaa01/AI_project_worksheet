from typing import Dict, Any
import requests

def generate_caption(
        api_key: str,
        image_bytes: bytes,
        file_name: str = "uploaded.jpg",
        mime_type: str = "image/jpeg",
        **kwargs
) -> Dict[str, Any]:
    """
    Args:
        api_key: Bria API key
        image_bytes: Byte content of the uploaded image
        file_name: Optional filename to send to the API
        mime_type: MIME type of the image (default: image/jpeg)
        **kwargs: Additional parameters for future extension

    Returns:
        A dictionary with the caption result or error
    """
    url = "https://engine.prod.bria-api.com/v1/image/caption"

    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
    }

    files = {
        'file': (file_name, image_bytes, mime_type)
    }

    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")

        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()

        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        return response.json()

    except Exception as e:
        print(f"Error generating caption: {str(e)}")
        return {"error": str(e)}