import requests
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def ping_graphql():
    try:
        # Raw requests ping
        query = {"query": "{ hello }"}
        response = requests.post("http://localhost:8000/graphql", json=query)
        response.raise_for_status()
        result = response.json()
        print("Raw GraphQL response:", result)

        # Optional gql client ping
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        gql_query = gql("{ hello }")
        gql_result = client.execute(gql_query)
        print("gql client response:", gql_result)

    except Exception as e:
        print("GraphQL ping failed:", e)

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"Heartbeat: {datetime.datetime.now()}")


# Call the function
ping_graphql()
