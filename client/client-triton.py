import grpc
import numpy as np
# import tensorflow as tf
# from tensorflow.core.framework import types_pb2
# from tensorflow_serving.apis import predict_pb2
# from tensorflow_serving.apis import prediction_service_pb2_grpc

from tritonclient.grpc import service_pb2
from tritonclient.grpc import service_pb2_grpc
import time

channel = grpc.insecure_channel('localhost:8001')
stub = service_pb2_grpc.GRPCInferenceServiceStub(channel)

try:
    request = service_pb2.ServerLiveRequest()
    response = stub.ServerLive(request)
    print("server {}".format(response))
except Exception as ex:
    print(ex)


feature = np.array([[0.67224891,  0.18140817, -0.19491793,  0.21980668,  0.39320188,
        0.15826697,  0.01004872, -0.00318363,  0.04149301, -0.30890288,
       -0.98814881,  0.13053282,  0.96826633, -0.46301329,  1.52249288,
        0.65234284, -0.31088957, -0.42180938, -0.04051697, -0.0452023 ,
       -0.46118658, -1.27676435, -0.03104227, -2.2365872 ,  0.66450114,
        0.43195082, -0.01304192,  0.04507479, -1.11567339]], dtype=np.float32)



request = service_pb2.ModelInferRequest()
request.model_name = "creditfraud"
request.model_version = "1"

input = service_pb2.ModelInferRequest().InferInputTensor()
input.name = "dense_14_input"
input.datatype = "FP32"
input.shape.extend([1, 29])
request.inputs.extend([input])

output = service_pb2.ModelInferRequest().InferRequestedOutputTensor()
output.name = "dense_15"
request.outputs.extend([output])

request.raw_input_contents.extend([feature.tobytes()])

response = stub.ModelInfer(request)
print("model infer:\n{}".format(response))

r = np.frombuffer(response.contents, dtype=np.float32)
print(r)




