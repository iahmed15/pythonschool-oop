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

    def _update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._sattus = 'Young'
        elif self._growth > 0:
            self._growth = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'

    def grow(
        self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
            
        # Increment days growing
        self._days_growing += 1

        # Update the status
        self._update_status()


def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    new_crop.grow(4, 4)
    print(new_crop.report())


if __name__ == "__main__":
    main()
