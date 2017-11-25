import tensorflow as tf



a = tf.Variable([2], dtype=tf.float64)
b = tf.Variable([1], dtype=tf.float64)

x = tf.placeholder(tf.float64)

linear = x ** (a) + 2 * x + b

sess = tf.Session()
x = [[-2.25 + 4.75j], [-3.25 + 5.75j]]
absolute = tf.abs(x)
print(sess.run(absolute))

a = tf.constant(5.0)
b = tf.constant(4.0)

z = tf.Session()
c = a*b
print(z.run(c))
