import requests
from typing import Optional

from bot import ACCESS_TOKEN, GUID


class bitly():
    def __init__(self, link):
        self.link = link
        self.response = True

    def convert_url(self) -> Optional[str]:
        long_url = self.link
        short_url = None
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        url = 'https://api-ssl.bitly.com/v4/shorten'
        shorten_res = requests.post(
            url, json={"group_guid": GUID, "long_url": long_url}, headers=headers
        )
        if shorten_res.status_code == 200:
            short_url = shorten_res.json().get("link")
        else:
            self.response = False
        return short_url
