import tensorflow as tf


def callMe():
    # hello()
    arithmetic()
    pass


# hello world in tensorflow
def hello():
    h = tf.constant("Hello World")
    with tf.Session() as sess:  ## Session will have the parenthessis
        out = sess.run(h)
    print(out)
    pass


# simple arithmetic
def arithmetic():
    a = tf.constant(10)
    b = tf.constant(20)
    add = a + b
    sub = a - b
    mul = a * b

    with tf.Session() as sess:
        add = sess.run(add)
        sub = sess.run(sub)
        mul = sess.run(mul)
    print("The Add: {}".format(add))
    print("The mul: {}".format(mul))
    print("The sub: {}".format(sub))
