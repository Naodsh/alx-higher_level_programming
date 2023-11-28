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

        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute \
                    '{}'".format(name))

    def __delattr__(self, name):
        """
        Prevents the dynamic creation of attributes except for 'first_name'.

        Args:
        - self: The instance of the class.
        - name: The name of the attribute being set.
        """

        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute \
                    '{}'".format(name))
