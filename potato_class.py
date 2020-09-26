from crop_class import *


# Potato is a subclass of Crop
class Potato(Crop):
    """A potato crop"""

    # Constructor
    def __init__(self):
        """Represents a potato crop

        Args:
            Inherited from parent class Crop (growth_rate, light_need,
            water_need)

        Attributes:
            _type (str): the variety of the crop
            Inherited from parent class Crop (_growth, _days_growing, _status)
        """
        # Call the parent class constructor with default values for potato
        # growth rate = 1; light_need = 3; water_need = 6

        super().__init__(1, 3, 6)
        self._type = 'Potato'

    # Override the grow method for subclass
    def grow(self, light, water):
        """A more sophisticated algorithm than the parent class' method,
        responsible for actually growing the crop"""
        if light >= self._light_need and water >= self._water_need:
            if self._status == 'Seedling' and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == 'Young' and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        # Increment days growing
        self._days_growing += 1
        # Update the status
        self._update_status()


def main():
    # Create a new potato crop
    potato_crop = Potato()
    print(potato_crop.report())

    # Manually grow the crop
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())


if __name__ == "__main__":
    main()
