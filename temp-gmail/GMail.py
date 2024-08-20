from curl_cffi import requests


class GMail:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": "https://www.emailnator.com",
            "Referer": "https://www.emailnator.com/",
            "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A Brand";v="8", "Chromium";v="117"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.email = None
        self.session.get("https://www.emailnator.com/")
        self.update_tokens()

    def update_tokens(self):
        xsrf = self.session.cookies.get("XSRF-TOKEN")
        sesh = self.session.cookies.get("gmailnator_session")
        self.headers["X-Xsrf-Token"] = xsrf.replace("%3D", "=")
        self.headers["Cookie"] = f"XSRF-TOKEN={xsrf}; gmailnator_session={sesh};"

    def create_email(self):
        url = "https://www.emailnator.com/generate-email"
        data = {"email": ["plusGmail", "dotGmail"]}
        response = self.session.post(url, headers=self.headers, json=data)
        self.email = response.json()["email"][0]
        self.update_tokens()
        return self.email

    def load_item(self, message_id):
        url = "https://www.emailnator.com/message-list"
        data = {"email": self.email, "messageID": message_id}
        response = self.session.post(url, headers=self.headers, json=data)
        self.update_tokens()
        return response.text

    def load_list(self):
        self.update_tokens()
        url = "https://www.emailnator.com/message-list"
        data = {"email": self.email}
        response = self.session.post(url, headers=self.headers, json=data)
        self.update_tokens()
        return response.json()

    def check_new_item(self, keyword):
        response_data = self.load_list()

        for message in response_data["messageData"]:
            if keyword.lower() in message["from"].lower():
                return {"messageId": message["messageID"]}

        return {"messageId": None}
