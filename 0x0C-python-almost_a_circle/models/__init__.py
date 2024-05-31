class Base:
    '''
    This is a class that gives ID


    '''
    __nb_objects = 0

    def __init__(self, id=None):

        """
        Initialize a new Base instance.

        Args:
            id (int, optional): The ID for the instance. If None,
            a unique ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
