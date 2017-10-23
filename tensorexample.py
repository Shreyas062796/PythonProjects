import tensorflow as tf



a = tf.Variable([2], dtype=tf.float64)
b = tf.Variable([1], dtype=tf.float64)

x = tf.placeholder(tf.float64)

linear = x ** (a) + 2 * x + b


sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear, {x: [1, 2, 3, 4]}))
