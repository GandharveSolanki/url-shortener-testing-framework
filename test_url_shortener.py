import pytest
from url_shortener import URLShortener

@pytest.fixture
def url_shortener():
    return URLShortener()

def test_shorten_url(url_shortener):
    original_url = "https://www.example.com"
    short_url = url_shortener.shorten_url(original_url)
    assert short_url is not None

def test_get_original_url(url_shortener):
    original_url = "https://www.example.com"
    short_url = url_shortener.shorten_url(original_url)
    assert url_shortener.get_original_url(short_url) == original_url

def test_get_original_url_nonexistent(url_shortener):
    assert url_shortener.get_original_url("nonexistent") is None

def test_delete_shortened_url(url_shortener):
    original_url = "https://www.example.com"
    short_url = url_shortener.shorten_url(original_url)
    url_shortener.delete_shortened_url(short_url)
    assert url_shortener.get_original_url(short_url) is None

def test_delete_nonexistent_shortened_url(url_shortener):
    with pytest.raises(KeyError):
        url_shortener.delete_shortened_url("nonexistent")
