def password_is_valid(password):
    spaces_in_str = 0
    for i in password:
        if i == ' ':
            spaces_in_str += 1

    if (not password) or (password.strip() == ""):
        return False
    elif (len(password) < 3) or (len(password) > 20):
        return False
    elif spaces_in_str > 0:
        return False
    else:
        return True