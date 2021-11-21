class AerospaceEngineer:
    """Aerospace Engineer (Director) - Controls creation of final product """

    def __init__(self, builder):
        self._builder = builder

    def create_aeroplane(self):
        self._builder.create_new_aeroplane()
        self._builder.add_wings()
        self._builder.add_avionics()
        self._builder.add_engines()

    def get_aeroplane(self):
        return self._builder.aeroplane


class AeroplaneBuilder:
    """ AeroplaneBuilder as the Abstract Builder"""

    def __init__(self):
        self.aeroplane = None

    def create_new_aeroplane(self):
        self.aeroplane = Aeroplane()


class Airliner(AeroplaneBuilder):
    """Concrete Builder that provide parts for putting the aircraft together. """

    def add_wings(self):
        self.aeroplane.wings = '197ft'

    def add_avionics(self):
        self.aeroplane.avionics = 'commercial'

    def add_engines(self):
        self.aeroplane.engines = 2


class Aeroplane:
    """ Aeroplane as the Product """

    def __init__(self):
        self.wings = None
        self.avionics = None
        self.engines = None

    def __str__(self):
        return 'Building a {} Boeing 787 Dreamliner with a wingspan of {} that runs on {} engines.'.format(self.avionics, self.wings, self.engines)


builder = Airliner()
director = AerospaceEngineer(builder)
director.create_aeroplane()
aeroplane = director.get_aeroplane()
print(aeroplane)
