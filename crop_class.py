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


def main():
    # Instantiate the class
    new_crop = Crop(1,4,3)
    print(new_crop._light_need)
    print(new_crop._status)
    print(new_crop._type)

    new_crop2 = Crop(2, 5, 7)
    print(new_crop2._light_need)
    print(new_crop2._status)
    print(new_crop2._type)


if __name__ == "__main__":
    main()
