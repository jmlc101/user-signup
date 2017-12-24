def email_is_valid(entry):
    at_count = 0
    period_count = 0
    space_count = 0
    if (len(entry) >= 3) and (len(entry) <= 20):
        for i in entry:
            if i == " ":
                space_count += 1
            elif i == "@":
                at_count += 1
            elif i == ".":
                period_count += 1
    if (at_count == 1) and (period_count == 1) and (space_count == 0):
        return True
    else:
        return False
        
        