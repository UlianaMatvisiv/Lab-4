"""Creating classes for game."""
class Room:
    """This class helps to describe room and
    get information about it.
    >>> backyard = Room("Backyard")
    >>> backyard.set_description("An old backyard of abondoned house.")
    >>> backyard.get_description()
    'An old backyard of abondoned house.'
    >>> backyard.link_room("Kitchen", "south")"""
    def __init__(self, name):
        """Method lets the class initialize the object's attributes."""
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """Method sets the description of the room."""
        self.description = description

    def get_description(self):
        """Method to get the description of the room."""
        return self.description

    def set_character(self, character):
        """Method to set character."""
        self.character = character

    def get_character(self):
        """Method to get character, who's in the room."""
        return self.character

    def set_item(self, item):
        """Method to set item in the room."""
        self.item = item

    def get_item(self):
        """Method to get item, which is in the room."""
        return self.item

    def link_room(self, room_to_link, direction):
        """Method to link two rooms and set the direction."""
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        """Method to go in the next room."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def get_details(self):
        """Method to get information about direction of
        the next room."""
        print(f"{self.name}\n--------------------\n{self.description}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.name + " is " + direction)


class Character:
    """Class for character information."""
    def __init__(self, name, description):
        """Method lets the class initialize the object's attributes."""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

class Enemy:
    """This class helps to get information
    about enemy.
    >>> bob = Enemy("Bob", "A scary zombie.")
    >>> bob.set_conversation("Meeeh")
    >>> bob.set_weakness("knife")
    >>> bob.get_weakness()
    'knife'
    >>> bob.talk()
    [Bob says]: Meeeh
    """
    defeated_count = 0
    def __init__(self, name, description):
        """Method lets the class initialize the object's attributes."""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """Method to set line of the enemy."""
        self.conversation = conversation

    def set_weakness(self, weakness):
        """Method to set enemy's weakness."""
        self.weakness = weakness

    def get_weakness(self):
        """Method to get enemy's weakness."""
        return self.weakness

    def describe(self):
        """Method to describe who is in the room."""
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """Method to display enemy`s line."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)

    def fight(self, item_used):
        """Method to check if player had chosen
        the right item to fight."""
        if item_used == self.weakness:
            print("You fend " + self.name + " off with the " + item_used)
            Enemy.defeated_count += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

    def get_defeated(self):
        """Method to display how many times player won."""
        return Enemy.defeated_count

class Friend:
    """Class for friend's information."""
    def __init__(self, name, description):
        """Method lets the class initialize the object's attributes."""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

class Item:
    """This class helps to describe item
    and get information about it.
    >>> knife = Item("knife")
    >>> knife.set_description("Silver knife with wooden handle.")
    >>> knife.get_description()
    'Silver knife with wooden handle.'
    >>> knife.get_name()
    'knife'
    >>> knife.describe()
    The [knife] is here - Silver knife with wooden handle.
    """
    def __init__(self, name):
        """Method lets the class initialize the object's attributes."""
        self.name = name
        self.description = None

    def set_description(self, description):
        """Method to set description of the item."""
        self.description = description

    def get_description(self):
        """Method to get description of an item."""
        return self.description

    def get_name(self):
        """Method to get name of an item."""
        return self.name

    def describe(self):
        """Method to describe item in the room."""
        print(f"The [{self.name}] is here - {self.description}")
if __name__ == '__main__':
    import doctest
    doctest.testmod()
