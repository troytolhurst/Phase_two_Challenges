from lib.diary_entry_class import *
class Diary():
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        self.diary_entries.append(entry)

    def all(self):
        return self.diary_entries
    
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_word_count = 0
        for entry in self.diary_entries:
            total_word_count += entry.count_words()
        return total_word_count
     
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        result = self.count_words()
        return result / wpm
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        best_entry = None
        max_words_to_read = wpm * minutes

        for entry in self.diary_entries:
            words_in_entry = entry.count_words()
            if words_in_entry <= max_words_to_read:
                if best_entry is None or words_in_entry > best_entry.count_words():
                    best_entry = entry

        return best_entry

