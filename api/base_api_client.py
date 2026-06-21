from abc import ABC, abstractmethod
import requests

class ApiClient(ABC):
    def __init__(self, base_url):
        self._base_url = base_url

    def _make_request(self, url, params=None):
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"API request error: {error}") 
            return None
        
    @abstractmethod
    def get_data(self, query):
        pass