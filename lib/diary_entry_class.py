class DiaryEntry():
    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.current_word_index = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        for contents in self.contents:
            content_split = self.contents.split()
            return len(content_split)
    
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        result = self.count_words()
        return result / wpm
    
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        content_split = self.contents.split()
        words_to_read = int(wpm * minutes)
        chunk = " ".join(content_split[self.current_word_index:self.current_word_index + words_to_read])
        self.current_word_index += words_to_read
        if self.current_word_index >= len(content_split):
            self.current_word_index = 0 
        return chunk