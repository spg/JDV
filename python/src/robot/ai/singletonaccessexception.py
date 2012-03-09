class SingletonAccessException(Exception):
    def __init__(self, *args, **kwargs):
        super(SingletonAccessException, self).__init__(*args, **kwargs)