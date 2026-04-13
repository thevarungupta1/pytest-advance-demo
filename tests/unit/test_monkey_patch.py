import pytest
from unittest.mock import patch, MagicMock
from src.configured_client import get_user_from_env

@pytest.mark.unit
def test_get_user_from_env_with_patch(monkeypatch):
    # patch env
    monkeypatch.setenv("API_BASE_URL", "http://patchedapi.com")
    monkeypatch.setenv("API_TIMEOUT", "10")
    
    # patch the underlying fetch_user function dependency by patching request.get
    fake_response = MagicMock() 
    fake_response.status_code = 200
    fake_response.json.return_value = {"id": 1, "name": "Bob"}
    
    monkeypatch.setattr("src.external_api.requests.get", lambda url, timeout: fake_response)
    
    result = get_user_from_env(1)
    assert result["name"] == "Bob"