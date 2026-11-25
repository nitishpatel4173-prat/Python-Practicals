# Practical 45: Reshape a tensor using tf.reshape()

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf  # noqa: E402

tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original tensor, shape", tensor.shape, ":\n", tensor.numpy())

reshaped_3x4 = tf.reshape(tensor, (3, 4))
print("\nReshaped to (3, 4):\n", reshaped_3x4.numpy())

reshaped_2x2x3 = tf.reshape(tensor, (2, 2, 3))
print("\nReshaped to (2, 2, 3):\n", reshaped_2x2x3.numpy())

auto = tf.reshape(tensor, (4, -1))          # -1 means "work out this size"
print("\nReshaped to (4, -1) -> shape", auto.shape, ":\n", auto.numpy())

flat = tf.reshape(reshaped_3x4, [-1])       # back to a 1-D tensor
print("\nFlattened again:", flat.numpy())
