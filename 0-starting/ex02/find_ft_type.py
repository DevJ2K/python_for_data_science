def all_thing_is_obj(object = None) -> int:
    if object is None:
        return 42
    obj_type = type(object).__name__.capitalize()
    if (obj_type == "Str"):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (obj_type == "Int"):
        print("Type not found")
    else:
        print(f"{obj_type} : {type(object)}")
    return 42
