from crop_class import *


class Wheat(Crop):
    """A wheat crop"""

    # Constructor
    def __init__(self):
        """Represents a wheat crop

        Args:
            Inherited from parent class Crop (growth_rate, light_need,
            water_need)

        Attributes:
            _type (str): the variety of the crop
            Inherited from parent class Crop (_growth, _days_growing, _status)
        """
        # Call the parent class constructor with default values for potato
        # growth rate = 2; light_need = 5; water_need = 4
        super().__init__(2,5,4)
        self._type = "Wheat" # Override the parent class attribute with new
                             # value

    # Override the grow method for subclass
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling":
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young":
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        # Increment days growing
        self._days_growing += 1
        # Update the status
        self._update_status()
