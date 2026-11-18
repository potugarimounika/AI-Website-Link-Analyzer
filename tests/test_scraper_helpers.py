from app.scraper import _validate_public_url
import pytest

def test_rejects_invalid_scheme():
    with pytest.raises(ValueError):
        _validate_public_url("file:///etc/passwd")

def test_rejects_localhost():
    with pytest.raises(ValueError):
        _validate_public_url("http://localhost:8000")
