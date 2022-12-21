############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    # MelonType(self, code, first_harvest, color, is_seedless, is_bestseller, name):

    # Fill in the rest
    muskmelon = MelonType(
        "musk", 
        1998, 
        "green", 
        True, 
        True,
        "Muskmelon")
        
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType(
        "cas",
        2003,
        "orange",
        False,
        False,
        "Casaba"
    )
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    all_melon_types.append(casaba)

    crenshaw = MelonType(
        "cren",
        1996,
        "green",
        False,
        False,
        "Crenshaw"
    )
    
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "yw",
        2013,
        "yellow",
        False,
        True,
        "Yellow Watermelon"
    )
    
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types
    
    
melons_list = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        name = melon.name
        pairings = melon.pairings
        print(f"{name} pairs with:")
        for pair in pairings:
            print(f"- {pair}")

# print_pairing_info(melons_list)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

    melon_dict = {}

    for melon in melon_types:
        name = melon.name
        code = melon.code
        melon_dict[code] = name
    
    print(melon_dict)
    return melon_dict

melon_types = make_melon_type_lookup(melons_list)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Returns True or False based on whether the melon is able to be sold.
        
        Shape and color ratings > 5
        Not from field 3"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    harvested_melons = []
    
    # melons_by_id = make_melon_type_lookup(melon_types) # A dictionary of melons and their codes
    melons_by_id = melon_types

    # Melon(melons_by_id['yw'], shape_rating, color_rating, from_field, harvested_by)

    melon_1 = Melon(
        melons_by_id["yw"],
        8,
        7,
        2,
        "Sheila"
    )

    melon_2 = Melon(
        melons_by_id["yw"],
        3,
        4,
        2,
        "Sheila"
    )
    
    melon_3 = Melon(
        melons_by_id["yw"],
        9,
        8,
        3,
        "Sheila"
    )

    melon_4 = Melon(
        melons_by_id["cas"],
        10,
        6,
        35,
        "Sheila"
    )

    
    melon_5 = Melon(
        melons_by_id["cren"],
        8,
        9,
        35,
        "Michael"
    )
    
    melon_6 = Melon(
        melons_by_id["cren"],
        8,
        2,
        35,
        "Michael"
    )
    
    melon_7 = Melon(
        melons_by_id["cren"],
        2,
        3,
        4,
        "Michael"
    )

    melon_8 = Melon(
        melons_by_id["musk"],
        6,
        7,
        4,
        "Michael"
    )

    melon_9 = Melon(
        melons_by_id["yw"],
        7,
        10,
        3,
        "Sheila"
    )

    harvested_melons.append(melon_1)
    harvested_melons.append(melon_2)
    harvested_melons.append(melon_3)
    harvested_melons.append(melon_4)
    harvested_melons.append(melon_5)
    harvested_melons.append(melon_6)
    harvested_melons.append(melon_7)
    harvested_melons.append(melon_8)
    harvested_melons.append(melon_9)

    # print(harvested_melons)
    return harvested_melons

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        harvested_by = melon.harvested_by
        from_field = melon.from_field
        if melon.is_sellable() == True:
            print(f"Harvested by {harvested_by} from Field {from_field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {harvested_by} from Field {from_field} (NOT SELLABLE)")
    
get_sellability_report(melons)