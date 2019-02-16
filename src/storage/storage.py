# Returns user from backend storage
def get_user(user_id):
    return {
            "id": 0,
            "name": "John"
            }

# Stores a new group in the backend storage and returns group id
def create_group(group_name):
    return {
            "id": 0,
            "name": "tomato"
            }

# Stores a new message in the backend storage
def store_message(group_id, user_id, message):
    print("Storing message")

# Returns group history
def get_group_messages(group_id):
    pass
