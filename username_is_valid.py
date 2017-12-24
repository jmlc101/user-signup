def username_is_valid(username):
    
    spaces_in_str = 0
    for i in username:
        if i == ' ':
            spaces_in_str += 1

    if (not username) or (username.strip() == ""):
        return False
    elif (len(username) < 3) or (len(username) > 20):
        return False
    elif spaces_in_str > 0:
        return False
    else:
        return True
