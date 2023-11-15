def make_snippet(string):
    words = string.split(" ")
    if len(words) > 5:
        first_five = words [:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return string

