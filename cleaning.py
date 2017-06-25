import re


def update_phone(phone_num):
    # Remove multiple numbers and extensions
    stripped = re.split('[xo,;]', phone_num)[0]
    # Strip of all non-numeric characters
    stripped = re.sub('[^0-9]','', stripped)
    # Unusual cases
    if len(stripped) != 10 and len(stripped) != 11:
        if phone_num == "1+1-215-626-7668":
            return "(215) 626-7668"
        elif phone_num == "215-22x-2728":
            return "(215) 22x-2728"
        # Invalid phone number reported
        else:
            return False
    if len(stripped) == 11:
        if stripped[0] == '1':
            stripped = stripped[1:]
        else:
            return False
    return "(" + stripped[:3] + ") " + stripped[3:6] + "-" + stripped[6:]

def update_postcode(postal_code):
    possible_codes = []
    # Immediately return suitable codes
    if len(postal_code) == 5 and len(re.sub('[^0-9]','', postal_code)) == 5:
        return postal_code
    stripped = re.split('[^0-9]', postal_code)
    for segment in stripped:
        if len(segment) == 5: # 5-digit code
            possible_codes.append(segment)
    # No 5-digit codes present
    if len(possible_codes) == 0:
        return False
    # Multiple 5-digit codes present
    elif len(possible_codes) > 1:
        return_code = ""
        for code in possible_codes:
            return_code += ";"
            return_code += code
        return return_code[1:]
    else:
        return possible_codes[0]

def update_streetname(street_name):
    #street_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
        "Trail", "Parkway", "Commons", "Way", "Broadway", "Highway", "Terrace", "Pike", "Circle", 
        "Park", "Bypass", "Run", "Alley", "Way", "Plaza", "Turnpike", "Crossing", "Walk", "Expressway",
         "North", "South", "East", "West"]
    mapping = { "St": "Street",
                "St.": "Street",
                "Rd": "Road",
                "Rd.": "Road",
                "Ave": "Avenue",
                "Ave.": "Avenue",
                "Dr": "Drive",
                "Blvd": "Boulevard",
                "Blvd.": "Boulevard",
                "Ct": "Court",
                "Cir": "Circle",
                "Ln": "Lane",
                "Hwy": "Highway"
    }
    directions = {  "N": "North",
                    "N.": "North",
                    "S": "South",
                    "S.": "South",
                    "E": "East",
                    "E.": "East",
                    "W": "West",
                    "W.": "West"
    }

    # Fix capitalization
    segments = street_name.split(" ")
    fixed_name = ""
    for segment in segments:
        fixed_name += " "
        seg_cap = segment.capitalize()
        if seg_cap in directions.keys():
            seg_cap = directions[seg_cap]
        fixed_name += seg_cap
    fixed_name = fixed_name[1:]

    # Check ending
    match = re.search(r'\b\S+\.?$', fixed_name)
    if match:
        ending = match.group()
        if ending not in expected:
            if ending in mapping.keys():
                new_ending = mapping[ending]
                return fixed_name[:-len(ending)] + new_ending

    return fixed_name