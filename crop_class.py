import random


class Crop:

    # Constructor
    def __init__(self, growth_rate, light_need, water_need):
        """Represents the most generic characteristics of a food crop, namely
        growth needs of the crop and the _status

        Args:
            growth_rate (int): the amount the crop is 'grown' by
            light_need (int): the required light intensity needed for the crop
                              to grow
            water_need (int): the required amount of water needed for the crop 
                              to grow

        Attributes:
            _growth (int): the numerical status of the crop's growth
            _days_growing (int): the number of days the crop has spent growing
            _status (str): the qualitative status of the crop's growth
            _type (str): the variety of crop
        """

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = 'Seed'
        self._type = 'Generic'

    def needs(self):
        """Display the amount of light and water that the crop requires to grow

        Returns:
            A dictionary containing the light and water needs
        """
        return {'light need': self._light_need, 'water need': self._water_need}

    # Method to provide information about the current state of the crop
    def report(self):
        """Provides an overview of the current state of the crop

        Returns:
            A dictionary containing the type, status, growth and days growing
        """
        return {'type': self._type, 'status': self._status,
                'growth': self._growth, 'days_growing': self._days_growing}

    def _update_status(self):
        """Provides a way to change the status attribute to an appropriate value
        depending on the current amount of growth"""
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'

    def grow(self, light, water):
        """Responsible for actually growing the crop"""
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate

        # Increment days growing
        self._days_growing += 1

        # Update the status
        self._update_status()


def auto_grow(crop, days):
    """Provides a way to test the crop over a long period of time and to test
    the functionality of the class

    Args:
        crop (class): the instance of the crop class we want to test the
                      growth of
        days (int): the number of days we want to automatically grow the crop
                    for
    """
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1, 10)
        crop.grow(light, water)


def manual_grow(crop):
    """Allows us to provide specific values to grow the crop over a single day

    Args:
        crop (class): the instance of the crop class we want to test the
                      growth of
    """
    valid = False
    while not valid:
        try:
            light = int(input('Please enter a light value (1-10):\n> '))
            if 1 <= light <= 10:
                valid = True
            else:
                print('Value entered not valid - pleas enter a value between 1'
                      + ' and 10')
        except ValueError:
            print("Value entered not valid - please enter a value between 1" +
                  " and 10")

    valid = False
    while not valid:
        try:
            water = int(input('Please enter a water value (1-10):\n> '))
            if 1 <= water <= 10:
                valid = True
            else:
                print('Value entered not valid - pleas enter a value between 1'
                      + ' and 10')
        except ValueError:
            print("Value entered not valid - please enter a value between 1" +
                  " and 10")

    # Grow the crop
    crop.grow(light, water)

def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    manual_grow(new_crop)
    print(new_crop.report())


if __name__ == "__main__":
    main()
