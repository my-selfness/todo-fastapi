
def indivisual_serial(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "name":todo["title"],
        "description":todo["description"],
        "complete":todo["completed"]
    }


def list_serial(todos)->list:
    return[indivisual_serial(todo) for todo in todos]