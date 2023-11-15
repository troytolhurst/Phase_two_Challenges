def grammar(string):
    if string == " ":
        raise ValueError("No string")
    if string[0].isupper() and string[-1] in ".!?":
        return 'Grammar is correct!'
    elif string[0].isupper() and not string[-1] in ".!?":
        return 'String does not end with suitable punctuation.'
    elif string[0].islower() and string[-1] in ".!?":
        return 'String does not start with capital letter'
    else:
        return 'String does not start with capital letter or end with suitable punctuation.'

