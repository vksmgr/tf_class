import tensorflow as tf


def callMe():
    # hello()
    # arithmetic()
    uniqueName()
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


# each tensor should have unique name if it does not have it will make the versions
def uniqueName():
    a = tf.constant(value=3, name='j', dtype=tf.float32)
    b = tf.constant(value=3, name='j', dtype=tf.float32)
    print(a)
    print(b)
    # if no name given tensor flow will automatically provide the name to the tesor
    c = tf.add(a,b)
    print(c)