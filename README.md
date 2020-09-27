# pythonschool.net Crop Simulation


* crop_class module


* crops module


* potato_class module


* wheat_class module

---

- [pythonschool.net Crop Simulation](#pythonschoolnet-crop-simulation)
- [crop_class.py](#crop-classpy)
    + [class crop_class.Crop(growth_rate, light_need, water_need)](#class-crop-classcrop-growth-rate--light-need--water-need-)
      - [\__init__(growth_rate, light_need, water_need)](#---init---growth-rate--light-need--water-need-)
      - [grow(light, water)](#grow-light--water-)
      - [needs()](#needs--)
      - [report()](#report--)
    + [crop_class.auto_grow(crop, days)](#crop-classauto-grow-crop--days-)
    + [crop_class.display_menu()](#crop-classdisplay-menu--)
    + [crop_class.get_menu_choice()](#crop-classget-menu-choice--)
    + [crop_class.manage_crop(crop)](#crop-classmanage-crop-crop-)
    + [crop_class.manual_grow(crop)](#crop-classmanual-grow-crop-)
- [potato_class.py](#potato-classpy)
    + [class potato_class.Potato()](#class-potato-classpotato--)
      - [\__init__()](#---init----)
      - [grow(light, water)](#grow-light--water--1)
- [wheat_class.py](#wheat-classpy)
    + [class wheat_class.Wheat()](#class-wheat-classwheat--)
      - [\__init__()](#---init-----1)
      - [grow(light, water)](#grow-light--water--2)
- [crops.py](#cropspy)
    + [crops.create_crop()](#cropscreate-crop--)
    + [crops.display_menu()](#cropsdisplay-menu--)
    + [crops.select_option()](#cropsselect-option--)

---

# crop_class.py


### class crop_class.Crop(growth_rate, light_need, water_need)
Bases: `object`

A generic food crop


#### \__init__(growth_rate, light_need, water_need)
Represents the most generic characteristics of a food crop, namely
growth needs of the crop and the _status

Args:

    growth_rate (int): the amount the crop is ‘grown’ by
    
    light_need (int): the required light intensity needed for the crop to grow
    
    water_need (int): the required amount of water needed for the crop  to grow

Attributes:

    _growth (int): the numerical status of the crop’s growth
    
    _days_growing (int): the number of days the crop has spent growing
    
    _status (str): the qualitative status of the crop’s growth
    
    _type (str): the variety of the crop


#### grow(light, water)
Responsible for actually growing the crop


#### needs()
Display the amount of light and water that the crop requires to grow

Returns:

    A dictionary containing the light and water needs


#### report()
Provides an overview of the current state of the crop

Returns:

    A dictionary containing the type, status, growth and days growing


### crop_class.auto_grow(crop, days)
Provides a way to test the crop over a long period of time and to test
the functionality of the class

Args:

    crop (object): the instance of the crop class we want to test the growth of
    
    days (int): the number of days we want to automatically grow the crop for


### crop_class.display_menu()
Shows numerous menu options to the user


### crop_class.get_menu_choice()
Retrives the menu option which the user wants to use

Returns:

    the choice of menu option the user picked


### crop_class.manage_crop(crop)
Iterates over the menu options that the user can pick and also gives
them the functionality to exit the crop management program


### crop_class.manual_grow(crop)
Allows us to provide specific values to grow the crop over a single day

Args:

    crop (object): the instance of the crop class we want to test the growth of

# potato_class.py


### class potato_class.Potato()
Bases: `crop_class.Crop`

A potato crop


#### \__init__()
Represents a potato crop

Args:

    Inherited from parent class Crop (growth_rate, light_need, water_need)

Attributes:

    _type (str): the variety of the crop
    
    Inherited from parent class Crop (_growth, _days_growing, _status)


#### grow(light, water)
A more sophisticated algorithm than the parent class’ method,
responsible for actually growing the crop

# wheat_class.py


### class wheat_class.Wheat()
Bases: `crop_class.Crop`

A wheat crop


#### \__init__()
Represents a wheat crop

Args:

    Inherited from parent class Crop (growth_rate, light_need, water_need)

Attributes:

    _type (str): the variety of the crop

    Inherited from parent class Crop (_growth, _days_growing, _status)


#### grow(light, water)
Responsible for actually growing the crop

# crops.py


### crops.create_crop()
Allows the user to choose which crop type they want to create and
instantiate to then grow

Returns:

    new_crop (object): the instantiated class object


### crops.display_menu()
Shows the crop types that can be generated to the user

### crops.select_option()
Provides the user with the interface to input the crop type they want
to create and instantiate to then grow

Returns:

    choice (int): the crop type the user wants to create
