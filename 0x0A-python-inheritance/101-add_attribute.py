def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    # Check if the object is a dictionary or supports attribute assignment.
    if hasattr(obj, '__dict__') or isinstance(obj, dict):
        # The object allows adding attributes, so add the new attribute.
        setattr(obj, attr_name, attr_value)
    else:
        # The object can't have new attributes, so raise a TypeError.
        raise TypeError("can't add new attribute")
