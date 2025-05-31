def all_thing_is_obj(object = None) -> int:
    if object is None:
        return
    obj_type = str(type(object))

    object_type = obj_type[obj_type.find("'") + 1:obj_type.rfind("'")]

    if (object_type == "str"):
        print(f"{object} is in the kitchen : {obj_type}")
    elif (object_type == "int"):
        print("Type not found")
    else:
        print(f"{object_type.capitalize()} : {obj_type}")
    return 42
