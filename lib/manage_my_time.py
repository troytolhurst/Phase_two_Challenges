#def manage_my_time(speed, string):
   # word_list = string.split()
   # word_count = len(word_list)
    #result = word_count / speed
    #hours = int(result // 60)
    #minutes = int(result % 60)
    #seconds = int(result * 60) % 60
    #return f"It will take {hours} hours, {minutes} minutes and {seconds} seconds to read this string."

def manage_my_time(speed, string):
    word_count = len(string.split())
    result = divmod(word_count / speed, 60)
    return f"It will take {int(result[0])} hours, {int(result[1])} minutes and {int(result[1] * 60) % 60} seconds to read this string."
