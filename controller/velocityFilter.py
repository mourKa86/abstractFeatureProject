from abstractFeature import Feature

class VelocityFilter(Feature):
    def __init__(self, data):
        self._apply = False
        self.data = data

    @Feature.apply.setter
    def apply(self, value):
        self._apply = value

    def filterData(self, data):
        # data filtering
        return data
