import numpy as np
import tensorflow as tf
from seldon_core.proto import prediction_pb2, prediction_pb2_grpc
import grpc

channel = grpc.insecure_channel("localhost:8004")

stub = prediction_pb2_grpc.SeldonStub(channel)

feature = np.array([[0.67224891,  0.18140817, -0.19491793,  0.21980668,  0.39320188,
        0.15826697,  0.01004872, -0.00318363,  0.04149301, -0.30890288,
       -0.98814881,  0.13053282,  0.96826633, -0.46301329,  1.52249288,
        0.65234284, -0.31088957, -0.42180938, -0.04051697, -0.0452023 ,
       -0.46118658, -1.27676435, -0.03104227, -2.2365872 ,  0.66450114,
        0.43195082, -0.01304192,  0.04507479, -1.11567339]])

ft = tf.convert_to_tensor(feature)

datadef = prediction_pb2.DefaultData(
    tftensor=tf.make_tensor_proto(ft)
)

request = prediction_pb2.SeldonMessage(data=datadef)

metadata = [("seldon", "credit-fraud"), ("namespace", "seldon")]
stub.Predict(request=request, metadata=metadata)