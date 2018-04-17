import label_image as label
import os

class test:
    """A simple example class"""
    i = 12345

    def f(self):

        fileDir = os.path.dirname(os.path.realpath('__file__'))
        print (fileDir)
        return 'hello world'
t = test()
print(t.f())
print (label.runInit('tf_files/photos/144603918_b9de002f60_m.jpg'))
