class InvalidProvinceData(Exception):

    def __init__(self, message, data):
        super().__init__(message)
        self.data = data


class InvalidDistrictData(Exception):

    def __init__(self, message, data):
        super().__init__(message)
        self.data = data
