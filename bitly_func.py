import requests
from typing import Optional

from bot import ACCESS_TOKEN, GUID


class bitly():
    def __init__(self, link):
        self.link = link
        self.response = True
        self.error = None

    def convert_url(self) -> Optional[str]:
        long_url = self.link
        short_url = None
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        url = 'https://api-ssl.bitly.com/v4/shorten'
        shorten_res = requests.post(
            url, json={"group_guid": GUID, "long_url": long_url}, headers=headers
        )
        if shorten_res.status_code == 400:
            if "INVALID_ARG_LONG_URL" in shorten_res.json().get("message"):
                self.response, self.error = False, shorten_res.json().get("description")
            else:
                self.response = False
        else:
            short_url = shorten_res.json().get("link")
        return short_url
