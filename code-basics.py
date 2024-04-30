import tensorflow as tf

# node1 = tf.constant(3.0, tf.float32)

# node2 = tf.constant(4.0)

# # print(node1, node2)

# # sess = tf.compat.v1.Session()

# tf.print([node1, node2])

# a = tf.constant(5)
# b = tf.constant(2)
# c = tf.constant(3)

# d = tf.multiply(a, b)
# e = tf.add(c, b)
# f = tf.subtract(d, e)

# tf.print(f)

a = tf.compat.v1.placeholder(tf.float32)
b = tf.compat.v1.placeholder(tf.float32)

adder_node = a + b

tf.print(adder_node, {a: [1, 3], b: [2, 4]})
