# Credit Card Fraud Detection
> Seldon toy project

## Setup

- `kind create cluster`
- `istioctl manifest apply --set profile=demo`

- Install the seldon core protobufs `pip install seldon-core[tensorflow]`

## Deploy model

- `kubectl create namespace seldon`
- `kubectl apply -f credit-card-model.yaml`

## Client call

- `python client/credit-client.py`




