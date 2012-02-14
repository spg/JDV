class Marshaller():

    def serialize(self, obj):
        dump = cPickle.dumps(obj)

        return dump

    def deserialize(self, dump):
        obj = cPickle.loads(dump)

        return obj

