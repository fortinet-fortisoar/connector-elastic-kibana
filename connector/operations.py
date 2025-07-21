"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""

import json

from .kibana import Kibana


def parse_configs(config):
    info_keys = ["server_url", "protocol", "username", "password", "port", "verify_ssl"]
    return {_key: config[_key] for _key in info_keys}


def generic_action(config, params):
    kibana = Kibana(**parse_configs(config))
    resp = kibana.make_api_request(
        params.get("method"), params.get("apiendpoint"), params=params.get("params"), data=json.dumps(params.get("data"))
    )
    return resp.json()


def get_status(config, params):
    es = Kibana(**parse_configs(config))
    resp = es.get_status()
    return resp.json()


operations = {
    "generic_action": generic_action,
    "get_status": get_status,
    # "os_query_get_saved_query": os_query_get_saved_query,
    # "os_query_create_live_query": os_query_create_live_query,
    # "os_query_get_live_query_results": os_query_get_live_query_results,
}
