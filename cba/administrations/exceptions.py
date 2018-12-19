class InvalidProvinceData(Exception):

    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
        self.data = kwargs['data']


class InvalidDistrictData(Exception):

    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
        self.data = kwargs['data']
