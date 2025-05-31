def NULL_not_found(object = None) -> int:
    object_type = type(object).__name__

    if object_type != "float" and object not in [None, 0, '', False]:
        print("Type not Found")
        return 1
    elif object_type == "float" and str(object) != "nan":
        print("Type not Found")
        return 1

    match object_type:
        case "str":
            print("Empty:", end="")
        case "int":
            print("Zero: ", end="")
        case "float":
            print(f"Cheese: ", end="")
        case "bool":
            print(f"Fake: ", end="")
        case "NoneType":
            print("Nothing: ", end="")
    print(f"{object} {type(object)}")
    return 0
