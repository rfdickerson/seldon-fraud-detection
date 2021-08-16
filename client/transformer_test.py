from seldon_core.seldon_client import SeldonClient

endpoint = "0.0.0.0:9001"

data = [
    [7.0, 8.0, 9.0, 10.0]
]

sc = SeldonClient(microservice_endpoint=endpoint)

response = sc.microservice(
    json_data=data,
    method="transform-output"
)

print(response.request)
print(response.response)

