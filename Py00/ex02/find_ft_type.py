def all_thing_is_obj(object: any) -> int:

    if (isinstance(object, (str, list, tuple, set, dict))):
        if (isinstance(object, str)):
            print(object, "is in the kitchen :", end=" ")
        elif (isinstance(object, list)):
            print("List :", end=" ")
        elif (isinstance(object, tuple)):
            print("Tuple :", end=" ")
        elif (isinstance(object, set)):
            print("Set :", end=" ")
        elif (isinstance(object, dict)):
            print("Dict :", end=" ")
        print(type(object))
    else:
        print("Type not found")
    return 42