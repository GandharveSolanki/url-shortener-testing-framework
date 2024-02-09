import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        self.url_mapping[short_url] = original_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_mapping.get(short_url)

    def delete_shortened_url(self, short_url):
        if short_url in self.url_mapping:
            del self.url_mapping[short_url]
        else:
            raise KeyError("Short URL not found")
