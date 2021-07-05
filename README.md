# Credit Card Fraud Detection
> Seldon toy project

## Setup

- `kind create cluster`
- `istioctl manifest apply --set profile=demo`
- `helm install seldon-core ../../seldon-core/helm-charts/seldon-core-operator/ --namespace seldon-system --set istio.enabled=true`

### Setup Jaeger

```
kubectl create namespace observability
ubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/crds/jaegertracing.io_jaegers_crd.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/service_account.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role_binding.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/operator.yaml
```

```
kubectl apply -f system/simplest.yaml
```

Port forward:

```
kubectl port-forward $(kubectl get pods -l app.kubernetes.io/name=simplest -n seldon -o jsonpath='{.items[0].metadata.name}') 16686:16686 -n seldon
```

## Deploy model

- `kubectl create namespace seldon`
- `kubectl apply -f credit-card-model.yaml`

Port forward:

```
kubectl port-forward $(kubectl get pods -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}') -n istio-system 8004:8080
```

## Client call

- `python client/credit-client.py`




