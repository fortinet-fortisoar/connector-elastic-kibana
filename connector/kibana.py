# %%
import json
import requests
from typing import Literal


class Kibana:
    def __init__(
        self,
        server_url: str,
        protocol: str,
        api_key: str = None,
        username: str = None,
        password: str = None,
        port: int = 9200,
        verify_ssl: bool = True,
    ):
        self.server_url = server_url
        self.protocol = protocol
        self.api_key = (api_key,)
        self.username = username
        self.password = password
        self.port = str(port)
        self.verify_ssl = verify_ssl

        self.url = self.protocol + "://" + self.server_url + ":" + str(self.port)

    def get_status(self) -> requests.Response:
        return self.make_api_request("GET", "/api/data_views")

    def get_osquery_saved_queries(self) -> requests.Response:
        return self.make_api_request("GET", "/api/osquery/saved_queries")

    def create_osquery_live_queries(self) -> requests.Response:
        return self.make_api_request("POST", "/api/osquery/live_queries")

    def get_osquery_live_queries(self, id: str, action_id: str) -> requests.Response:
        return self.make_api_request("GET", f"/api/osquery/live_queries/{id}/results/{action_id}")

    def find_cases(self) -> requests.Response:
        return self.make_api_request("GET", f"/api/cases/_find")

    def get_cases(self, case_id: str) -> requests.Response:
        return self.make_api_request("GET", f"/api/cases/{case_id}")

    def apply_detection_engine_tags(self) -> requests.Response:
        return self.make_api_request("POST", f"/api/detection_engine/signals/tags")

    def make_api_request(
        self,
        method: Literal["GET", "POST", "PATCH", "DELETE", "PUT"],
        api_endpoint: str,
        params: dict = None,
        data: str = None,
    ):
        if not api_endpoint.startswith("/"):
            api_endpoint = "/" + api_endpoint

        resp = None

        headers = {"Accept": "application/json", "Content-type": "application/json", "kbn-xsrf": "true"}
        if isinstance(self.api_key, str):
            headers["Authorization"] = f"ApiKey {self.api_key}"
            resp = requests.request(
                method, self.url + api_endpoint, headers=headers, data=data, params=params, verify=self.verify_ssl
            )

        elif isinstance(self.username, str) and isinstance(self.password, str):
            resp = requests.request(
                method,
                self.url + api_endpoint,
                auth=(self.username, self.password),
                headers=headers,
                data=data,
                params=params,
                verify=self.verify_ssl,
            )

        return resp
