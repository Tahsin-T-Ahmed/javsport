def get_date_ordinal_suffix(number: int) -> str:    
    ordinal_suffix = None
    day_of_month = number

    match(number):
        case 1 | 21: 
            ordinal_suffix = "st"
        case 2 | 22:
            ordinal_suffix = "nd"
        case 3 | 23:
            ordinal_suffix = "rd"
        case _:
            ordinal_suffix = "th"

    return ordinal_suffix