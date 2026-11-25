# Practical 44: Define and display constant tensors in TensorFlow
# Install once (macOS Terminal):  pip3 install tensorflow

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"     # hide TensorFlow information messages
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"    # hide the oneDNN start-up notice

import tensorflow as tf  # noqa: E402

scalar = tf.constant(7)                          # 0-D tensor
vector = tf.constant([1.5, 2.5, 3.5])            # 1-D tensor
matrix = tf.constant([[1, 2, 3], [4, 5, 6]])     # 2-D tensor

print("Scalar :", scalar)
print("Vector :", vector)
print("Matrix :\n", matrix)

print("\nMatrix shape    :", matrix.shape)
print("Matrix data type:", matrix.dtype)
print("Matrix rank     :", tf.rank(matrix).numpy())
print("As NumPy array  :\n", matrix.numpy())
