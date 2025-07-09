import requests

def check_software_version(software: str) -> str:
    versions = {"python": "3.12.5", "java": "21.0.2", "node": "20.11.0"}
    return versions.get(software.lower(), "Unknown software")

def query_vendor_api(endpoint: str, params: dict) -> dict:
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

tools = [check_software_version, query_vendor_api]