class Crop:
    """A generic food crop"""

    # Constructor
    def __init__(self, growth_rate, light_need, water_need):
        # Set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = 'Seed'
        self._type = 'Generic'

    def needs(self):
        # Return a dictionary containing the light and water needs
        return {'light need': self._light_need, 'water need': self._water_need}

    # Method to provide information about the current state of the crop
    def report(self):
        # Return a dictionary containing the type, status, growth and days
        # growing
        return {'type': self._type, 'status': self._status,
                'growth': self._growth, 'days_growing': self._days_growing}


def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())

    new_crop2 = Crop(2, 5, 7)
    print(new_crop2.needs()['light need'])
    print(new_crop2.report()['type'])


if __name__ == "__main__":
    main()
