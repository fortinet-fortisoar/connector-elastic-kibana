## About the connector
Elastic Kibana provides a powerful UI for interacting with the Elastic Stack. It enables users to search, visualize, and manage data from Elasticsearch, build dashboards, monitor systems, and secure their environment.
<p>This document provides information about the Elastic Kibana Connector, which facilitates automated interactions, with a Elastic Kibana server using FortiSOAR&trade; playbooks. Add the Elastic Kibana Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Elastic Kibana.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet CSE

Contributor: Daehyeob Kim

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-elastic-kibana`

## Prerequisites to configuring the connector
- You must have the URL of Elastic Kibana server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Elastic Kibana server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Elastic Kibana</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Elastic server to connect and perform automated operations.<br>
<tr><td>API Key<br></td><td>Specify the API Key to connect to the endpoint and perform automated operations<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get All Data Views<br></td><td>Retrieve a list of all data views from Elastic Kibana.<br></td><td>get_all_data_views <br/>Investigation<br></td></tr>
<tr><td>Get Saved Queries<br></td><td>Retrieve a list of all saved queries from Elastic Kibana.<br></td><td>get_saved_queries <br/>Investigation<br></td></tr>
<tr><td>Create Live Query<br></td><td>Create and run a live query in Elastic Kibana based on the input parameters that ypu have specified.<br></td><td>create_a_live_query <br/>Investigation<br></td></tr>
<tr><td>Get Live Query Results<br></td><td>Retrieve the results of a live query using the query action ID from Elastic Kibana.<br></td><td>get_live_query_results <br/>Investigation<br></td></tr>
<tr><td>Search cases<br></td><td>Search cases in Elastic Kibana server based on the input parameters that you have specified.<br></td><td>search_cases <br/>Investigation<br></td></tr>
<tr><td>Get Case Information<br></td><td>Retrieve a specific case information from Elastic Kibana based on the case ID you have specified.<br></td><td>get_case_information <br/>Investigation<br></td></tr>
<tr><td>Add and Remove Detection Alert Tags<br></td><td>Add and remove detection alert tags based on the alert IDs and tags which you have specified.<br></td><td>add_and_remove_detection_alert_tags <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>generic_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get All Data Views
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "data_view": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "typeMeta": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "namespaces": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>
### operation: Get Saved Queries
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Create Live Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify the SQL query to execute in Elastic Kibana. For e.g select * from uptime;<br>
</td></tr><tr><td>Agent IDs<br></td><td>Specify a comma-separated list of agent IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>Agent Platforms<br></td><td>Specify a comma-separated list of platforms IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>Agent Policy IDs<br></td><td>Specify a comma-separated list of policy IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>Alert IDs<br></td><td>Specify a comma-separated list of alert IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>Case IDs<br></td><td>Specify a comma-separated list of alert IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>ECS Mapping<br></td><td>Map osquery results columns or static values to Elastic Common Schema (ECS) fields.<br>
</td></tr><tr><td>Event IDs<br></td><td>Specify a comma-separated list of event IDs to create and execute a live query in Elastic Kibana.<br>
</td></tr><tr><td>Metadata<br></td><td>Specify the custom metadata object associated with the live query.<br>
</td></tr><tr><td>Pack ID<br></td><td>Specify the ID of the pack you want to run in Elastic Kibana.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Live Query Results
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query ID<br></td><td>Specify the ID of the live query result you want to retrieve.<br>
</td></tr><tr><td>Query Action ID<br></td><td>Specify the ID of the query action that generated the live query results.<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search cases
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Assignees<br></td><td>Filters the returned cases by assignees. Valid values are None or unique identifiers for the user profiles.<br>
</td></tr><tr><td>Category<br></td><td>Filters the returned cases by category.<br>
</td></tr><tr><td>Default Search Operator<br></td><td>Specify the default operator to use for the simple query string. By default, it set as "OR"<br>
</td></tr><tr><td>From DateTime<br></td><td>Specify the from datetime to retrieve only cases that were created after a specific date. The date must be specified as a KQL data range or date match expression.<br>
</td></tr><tr><td>To DateTime<br></td><td>Specify the to datetime, to only cases that were created before a specific date. The date must be specified as a KQL data range or date match expression.<br>
</td></tr><tr><td>Owner<br></td><td>A filter to limit the response to a specific set of applications. If this parameter is omitted, the response contains information about all the cases that the user has access to read. You can choose from the following options: Cases, Observability, or Security Solution<br>
</td></tr><tr><td>Reporters<br></td><td>Filters the returned cases by the user name of the reporter.<br>
</td></tr><tr><td>Search Query<br></td><td>An Elasticsearch simple query string query that filters the objects in the response.<br>
</td></tr><tr><td>Search Fields<br></td><td>Select the fields to perform the simple_query_string parsed query against. You can choose either Title or Description<br>
</td></tr><tr><td>Severity<br></td><td>Select the severity by which to filters the returned cases. You can choose from the following options: Low, Medium, high, or Critical.<br>
</td></tr><tr><td>Status<br></td><td>Select the status by which to filters the returned cases by state. You can choose from the following options: Open, In Progress, or Closed<br>
</td></tr><tr><td>Tags<br></td><td>Filters the returned cases by tags.<br>
</td></tr><tr><td>Sort Field<br></td><td>Select the fields by which to sort the cases retrieved. You can choose from the following options: CreatedAt, UpdatedAt, ClosedAt, Title, category, Status, or Severity. By default, this option is set to "CreatedAt".<br>
</td></tr><tr><td>Sort Order<br></td><td>Select the sort order for the retrieved cases. You can choose from the following options: Ascending or Descending. By default, this option is set to "Descending".<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number from which to retrieve cases when pagination is applied. This parameter is used to fetch a specific subset of results based on the page number, helping to break large datasets into manageable chunks. By default, this value is set to 1.<br>
</td></tr><tr><td>Page Size<br></td><td>Specify the maximum number of results this operation should return, per page, in the response. By default, this value is set to 20 and maximum value is 100.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "cases": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "tags": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "owner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "comments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "settings": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "syncAlerts": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "assignees": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "closed_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "closed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "connector": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "fields": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_by": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "full_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "profile_uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "updated_by": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "full_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "profile_uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "totalAlerts": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "customFields": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "key": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "key": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "totalComment": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "external_service": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "count_open_cases": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "count_closed_cases": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "count_in_progress_cases": ""
</code><code><br>}</code>
### operation: Get Case Information
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Case ID<br></td><td>Specify the ID of the case based on which you want to retrieve details.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "tags": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "owner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "title": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "comments": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "owner": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "comment": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "pushed_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "pushed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_by": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "full_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "profile_uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "updated_by": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "settings": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "syncAlerts": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "assignees": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closed_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "closed_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "connector": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fields": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_by": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "full_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "profile_uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "updated_by": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "username": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "full_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "profile_uid": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "totalAlerts": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "customFields": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "key": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "value": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "totalComment": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "external_service": ""
</code><code><br>}</code>
### operation: Add and Remove Detection Alert Tags
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Alert IDs<br></td><td>Specify a comma-separated list of alert IDs to add and remove detection alert tags in Elastic Kibana.<br>
</td></tr><tr><td>Tags<br></td><td>Specify a comma-separated list of alert tags to add and remove from alerts in Elastic Kibana.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "took": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "noops": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "batches": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "deleted": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "retries": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "bulk": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "search": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "updated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "failures": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timed_out": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "throttled_millis": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "version_conflicts": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "requests_per_second": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "throttled_until_millis": ""
</code><code><br>}</code>
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options: 

GET 

PUT 

POST 

DELETE 

PATCH 

HEAD 

OPTIONS 

TRACE<br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

## Included playbooks
The `Sample - Elastic Kibana - 1.0.0` playbook collection comes bundled with the Elastic Kibana connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Elastic Kibana connector.

- Add and Remove Detection Alert Tags
- Create Live Query
- Execute an API Request
- Get All Data Views
- Get Case Information
- Get Live Query Results
- Get Saved Queries
- Search cases

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
