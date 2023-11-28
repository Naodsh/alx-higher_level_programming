#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        """
        Prevents the dynamic creation of attributes except for 'first_name'.

        Args:
        - self: The instance of the class.
        - name: The name of the attribute being set.
        - value: The value being assigned to the attribute.
        """

        # Check if the attribute is not 'first_name'
        # and 'first_name' has not been set yet
        if not hasattr(self, 'first_name') and name != 'first_name':
            # If conditions are met, raise an AttributeError
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            # Otherwise, allow setting the attribute
            self.__dict__[name] = value
