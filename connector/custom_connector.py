import requests
from typing import Literal, Optional, Union, Any


class CustomConnector:
    def __init__(self, url: str, api_key: str, verify_ssl: bool):
        self.url: str = url
        self.api_key: str = api_key
        self.verify_ssl: bool = verify_ssl
        self._check_url(url)

    def _check_url(self, url: str):
        if not (self.url.startswith("https://") or self.url.startswith("http://")):
            raise Exception("config url must start with 'https://' or 'http://'")

        if self.url.endswith("/"):
            raise Exception("config url must not end with '/'")

    def _check_api_endpoint(self, api_endpoint: str):
        if not api_endpoint.startswith("/"):
            raise Exception("param api_endpoint must startswith '/'")

    def _delete_none_dict(self, _d: Union[dict, list, None]) -> Union[dict, list, None]:
        if _d == None:
            return None
        elif isinstance(_d, list):
            return _d
        return {k: v for k, v in _d.items() if v is not None}

    def _check_health(self):
        return self.health_check()

    def generic_api_call(
        self,
        method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
        api_endpoint: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        json_data: Optional[dict] = None,
    ) -> dict:
        self._check_api_endpoint(api_endpoint)
        url = self.url + api_endpoint

        headers = headers if headers else {}
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["kbn-xsrf"] = "true"
        headers["Authorization"] = f"ApiKey {self.api_key}"

        params_new = self._delete_none_dict(params)
        json_data_new = self._delete_none_dict(json_data)

        resp = requests.request(method, url, headers=headers, params=params_new, json=json_data_new, verify=self.verify_ssl)
        return resp.json()

    def health_check(self) -> dict:
        endpoint = f"/admin/health"
        return self.generic_api_call("GET", endpoint)

    def get_all_data_views(self) -> dict:
        """Get all data views
        - API Doc: <https://www.elastic.co/docs/api/doc/kibana/operation/operation-getalldataviewsdefault>"""
        endpoint = f"/api/data_views"
        return self.generic_api_call("GET", endpoint)

    def get_saved_queries(self) -> dict:
        """Get saved queries
        - API Doc: <https://www.elastic.co/docs/api/doc/kibana/operation/operation-osqueryfindsavedqueries>"""
        endpoint = f"/api/osquery/saved_queries"
        return self.generic_api_call("GET", endpoint)

    def create_a_live_query(
        self,
        agent_ids: Optional[list[str]] = None,
        agent_platforms: Optional[list[str]] = None,
        agent_policy_ids: Optional[list[str]] = None,
        alert_ids: Optional[list[str]] = None,
        case_ids: Optional[list[str]] = None,
        ecs_mapping: Optional[dict] = None,
        event_ids: Optional[list[str]] = None,
        metadata: Optional[dict] = None,
        pack_id: Optional[str] = None,
        query: Optional[dict] = None,
    ) -> dict:
        """Create a live query
        - API Doc: https://www.elastic.co/docs/api/doc/kibana/operation/operation-osquerycreatelivequery
        """
        endpoint = f"/api/osquery/live_queries"
        json_data = {
            "agent_ids": agent_ids,
            "agent_platforms": agent_platforms,
            "agent_policy_ids": agent_policy_ids,
            "alert_ids": alert_ids,
            "case_ids": case_ids,
            "ecs_mapping": ecs_mapping,
            "event_ids": event_ids,
            "metadata": metadata,
            "pack_id": pack_id,
            "query": query,
        }
        return self.generic_api_call("POST", endpoint, json_data=json_data)

    def get_live_query_results(self, id: str, actionId: str) -> dict:
        """Get live query results
        - API Doc: https://www.elastic.co/docs/api/doc/kibana/operation/operation-osquerygetlivequeryresults
        """
        endpoint = f"/api/osquery/live_queries/{id}/results/{actionId}"
        return self.generic_api_call("GET", endpoint)

    def search_cases(
        self,
        assignees: Optional[Union[str, list[str]]] = None,
        category: Optional[Union[str, list[str]]] = None,
        defaultSearchOperator: str = "OR",
        from_: Optional[str] = None,
        owner: Optional[Union[str, list[str]]] = None,
        page: int = 1,
        perPage: int = 20,
        reporters: Optional[Union[str, list[str]]] = None,
        search: Optional[str] = None,
        searchFields: Optional[Union[str, list[str]]] = None,
        severity: Optional[str] = None,
        sortField: str = "createdAt",
        sortOrder: str = "desc",
        status: Optional[str] = None,
        tags: Optional[Union[str, list[str]]] = None,
        to: Optional[str] = None,
    ) -> dict:
        """Search cases
        - API Doc: <https://www.elastic.co/docs/api/doc/kibana/operation/operation-findcasesdefaultspace>"""
        endpoint = f"/api/cases/_find"
        params = {
            "assignees": assignees,
            "category": category,
            "defaultSearchOperator": defaultSearchOperator,
            "from": from_,
            "owner": owner,
            "page": page,
            "perPage": perPage,
            "reporters": reporters,
            "search": search,
            "searchFields": searchFields,
            "severity": severity,
            "sortField": sortField,
            "sortOrder": sortOrder,
            "status": status,
            "tags": tags,
            "to": to,
        }
        return self.generic_api_call("POST", endpoint, params=params)

    def get_case_information(self, caseId: str) -> dict:
        """Get case information
        - API Doc: <https://www.elastic.co/docs/api/doc/kibana/operation/operation-getcasedefaultspace>
        """
        endpoint = f"/api/cases/{caseId}"
        return self.generic_api_call("GET", endpoint)

    def add_and_remove_detection_alert_tags(self, ids: list[str], tags: dict) -> dict:
        """Add and remove detection alert tags.
        - API Doc: <https://www.elastic.co/docs/api/doc/kibana/operation/operation-setalerttags>
        """
        endpoint = f"/api/detection_engine/signals/tags"
        json_data = {"ids": ids, "tags": tags}
        return self.generic_api_call("POST", endpoint, json_data=json_data)

    # ---------------- Below Codes will be deprecaed after version 1.0.1 ------------------
    # TODO Below function will be deprecated at version 1.0.1
    def generic_action(
        self,
        method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
        apiendpoint: str,
        params: dict,
        data: dict,
    ) -> dict:
        return self.generic_api_call(method, apiendpoint, params=params, json_data=data)
