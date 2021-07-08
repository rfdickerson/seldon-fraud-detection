from functools import partial
import argparse
import numpy as np
import time
import sys

import tritonclient.grpc as grpcclient
from tritonclient.utils import InferenceServerException

feature = np.array([0.67224891,  0.18140817, -0.19491793,  0.21980668,  0.39320188,
        0.15826697,  0.01004872, -0.00318363,  0.04149301, -0.30890288,
       -0.98814881,  0.13053282,  0.96826633, -0.46301329,  1.52249288,
        0.65234284, -0.31088957, -0.42180938, -0.04051697, -0.0452023 ,
       -0.46118658, -1.27676435, -0.03104227, -2.2365872 ,  0.66450114,
        0.43195082, -0.01304192,  0.04507479, -1.11567339],
        dtype=np.float32)

features = np.vstack((feature, feature))

print(features)

try:
    triton_client = grpcclient.InferenceServerClient(url="localhost:8001")
except Exception as e:
    print("context creation failed: " + str(e))
    sys.exit()

model_name = 'credit-fraud'

inputs = []
outputs = []
inputs.append(grpcclient.InferInput('dense_14_input', [2, 29], "FP32"))

inputs[0].set_data_from_numpy(features)

outputs.append(grpcclient.InferRequestedOutput('dense_15'))

for _ in range(2000):
    start = time.time()
    result = triton_client.infer(model_name, inputs, "1", outputs)
    end = time.time()

print("latency: ", end - start)
print(result.as_numpy('dense_15'))



