# Author: Michael Taylor
# GitHub username: Michael-T321
# Date: 5/20/25
# Description: Library system with classes for LibraryItems, Patrons, and Library management, including check out, return, 
# requesting items, fines, and date incrementing.

class LibraryItem:
    """
    Represents an item in the library, such as a book, album, or movie.
    Stores information like the item ID, title, location, who checked it out, who requested it, and the date it was checked out.
    """
    def __init__(self, library_item_id, title, date_checked_out=None, checked_out_by=None, requested_by=None):
        """
        initialize a LibraryItem.
        
        args:
            library_item_id (str): identifier for the library item
            title (str): title of the item
            date_checked_out (int): date the item was checked out
            checked_out_by (Patron): Patron who checked out the item
            requested_by (Patron): Patron who requested the item
        """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = date_checked_out

    def get_library_item_id(self):
        return self._library_item_id

    def get_title(self):
        return self._title

    def get_location(self):
        return self._location

    def set_location(self, new_location):
        """
        Set the current location status of the library item
        """
        self._location = new_location

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_checked_out_by(self, new_checked_out_by):
        """
        Set the Patron who has checked out the item.
        """
        self._checked_out_by = new_checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def set_requested_by(self, new_requested_by):
        """
        patron who requested the item
        """
        self._requested_by = new_requested_by

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_date_checked_out(self, new_date):
        """
        date the item was checked out
        """
        self._date_checked_out = new_date


class Book(LibraryItem):
    """
    Represents a Book item in the library, inheriting from LibraryItem. Adds an author attribute and specifies the checkout length.
    """
    def __init__(self, library_item_id, title, author, date_checked_out=None, checked_out_by=None, requested_by=None):
        """
        Initialize a Book item.
        
        Args:
            Same as LibraryItem with the added author
            author (str): author of the book.
        """
        super().__init__(library_item_id, title, date_checked_out, checked_out_by, requested_by)
        self._author = author

    def get_author(self):
        return self._author

    def get_checked_out_length(self):
        return 21


class Album(LibraryItem):
    """
    Represents an Album item in the library, inheriting from LibraryItem. Adds an artist attribute and specifies the checkout length.
    """
    def __init__(self, library_item_id, title, artist, date_checked_out=None, checked_out_by=None, requested_by=None):
        """
        Initialize an Album item
        
        Args:
            Same as LibraryItem with the added album
            artist (str): Artist of the album.

        """
        super().__init__(library_item_id, title, date_checked_out, checked_out_by, requested_by)
        self._artist = artist

    def get_artist(self):
        return self._artist

    def get_checked_out_length(self):
        return 14


class Movie(LibraryItem):
    """
    Represents a Movie item in the library, inheriting from LibraryItem. Adds a director attribute and specifies the checkout length.
    """
    def __init__(self, library_item_id, title, director, date_checked_out=None, checked_out_by=None, requested_by=None):
        """
        Initialize a Movie item.
        
        Args:
            Same as LibraryItem with the added director
            director (str): Director of the movie.
        """
        super().__init__(library_item_id, title, date_checked_out, checked_out_by, requested_by)
        self._director = director

    def get_director(self):
        return self._director

    def get_checked_out_length(self):
        return 7


class Patron:
    """
    Represents a library patron, with an ID, name, checked out items, and fines owed.
    """
    def __init__(self, patron_id, name):
        """
        Initialize a Patron.
        
        Args:
            patron_id (str): identifier for the patron
            name (str): name of the patron
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_patron_id(self):
        return self._patron_id

    def get_name(self):
        return self._name

    def get_checked_out_items(self):
        return self._checked_out_items

    def add_library_item(self, item):
        """
        Add a library item to the patron's checked out items
        
        Args:
            item (LibraryItem): item to add
        """
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """
        Remove a library item from the patron's checked out items if present.
        
        Args:
            item (LibraryItem): item to remove.
        """
        if item in self._checked_out_items:
            self._checked_out_items.remove(item)

    def get_fine_amount(self):
        return self._fine_amount

    def amend_fine(self, fine):
        """
        change the patron's fine amount
        
        Args:
            fine (float): Amount to add or subtract from fines
        """
        self._fine_amount += fine


class Library:
    """
    Represents a library, holdings (items), members (patrons), current date, and operations such as checkout, returns,
    requests, fine payments, and date increments.
    """
    def __init__(self):
        """
        Initialize the library with empty holdings and members, and set current date to 0
        """
        self._holdings = {}  # dict with library_item_id as key and LibraryItem as value
        self._members = {}   # dict with patron_id as key and Patron as value
        self._current_date = 0

    def get_holdings(self):
        return self._holdings

    def get_members(self):
        return self._members

    def get_current_date(self):
        return self._current_date

    def add_library_item(self, item):
        """
        Add a LibraryItem to holdings
        
        args:
            item (LibraryItem): item to add
        """
        self._holdings[item.get_library_item_id()] = item

    def add_patron(self, patron):
        """
        add a Patron to members
        
        Args:
            patron (Patron): ppatron to add
        """
        self._members[patron.get_patron_id()] = patron

    def lookup_library_item_from_id(self, library_item_id):
        """
        Find a LibraryItem by its ID
        
        Args:
            library_item_id (str): ID to lookup
        
        Returns:
            LibraryItem or None if not found.
        """
        return self._holdings.get(library_item_id, None)

    def lookup_patron_from_id(self, patron_id):
        """
        find a Patron by their ID
        
        args:
            patron_id (str): ID to lookup
        
        returns:
            Patron or None if not found
        """
        return self._members.get(patron_id, None)

    def check_out_library_item(self, patron_id, library_item_id):
        """
        Check out a library item to a patron if possible
        
        args:
            patron_id (str): Patrons ID
            library_item_id (str): Items ID
        
        returns:
            message
        """
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"

        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if item.get_requested_by() is not None and item.get_requested_by() != patron:
            return "item on hold by other patron"

        item.set_checked_out_by(patron)
        item.set_date_checked_out(self._current_date)
        item.set_location("CHECKED_OUT")
        patron.add_library_item(item)

        if item.get_requested_by() == patron:
            item.set_requested_by(None)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """
        Return a library item to the library
        
        args:
            library_item_id (str): Items ID
        
        returns:
            str: message
        """
        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_location() == "ON_SHELF":
            return "item already in library"

        patron = item.get_checked_out_by()
        if patron is not None:
            patron.remove_library_item(item)

        if item.get_requested_by() is None:
            item.set_location("ON_SHELF")
        else:
            item.set_location("ON_HOLD_SHELF")

        item.set_checked_out_by(None)
        item.set_date_checked_out(None)

        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        Place a hold request on a library item by a patron
        
        args:
            patron_id (str): patrons ID
            library_item_id (str): items ID
        
        Returns:
            str: message
        """
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"

        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_requested_by() is not None:
            return "item already on hold"

        item.set_requested_by(patron)
        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self, patron_id, paid_amount):
        """
        Pay part or all of a patron's fine
        
        args:
            patron_id (str): Patrons ID
            paid_amount (float): Amount paid
        
        returns:
            str: message
        """
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"

        patron.amend_fine(-paid_amount)
        return "payment successful"

    def increment_current_date(self):
        """
        Increment the current date by one day and updates fines for all patrons with overdue items
        """
        self._current_date += 1

        for patron in self._members.values():
            for item in patron.get_checked_out_items():
                days_checked_out = self._current_date - item.get_date_checked_out()
                if isinstance(item, Book) and days_checked_out > 21:
                    patron.amend_fine(0.10)
                elif isinstance(item, Album) and days_checked_out > 14:
                    patron.amend_fine(0.10)
                elif isinstance(item, Movie) and days_checked_out > 7:
                    patron.amend_fine(0.10)



                

        
        

        


        
        

        

        
        


        

