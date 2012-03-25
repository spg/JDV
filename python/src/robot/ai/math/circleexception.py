from exceptions import Exception

class CircleException(Exception):
    def __init__(self, *args, **kwargs):
        super(CircleException, self).__init__(*args, **kwargs)