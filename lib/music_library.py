class MusicLibrary():
    def __init__(self):
        self.music_library = {}

    def add(self, artist, song):
        if artist in self.music_library:
            self.music_library[artist].append(song)
        else:
            self.music_library[artist] = [song]

    def list(self):
        return list(self.music_library.items())
    
    def search_by_artist(self, artist):
        return self.music_library.get(artist,[])
    
    def remove(self, artist, song):
        if artist in self.music_library:
            if song in self.music_library[artist]:
                self.music_library[artist].remove(song)
                if not self.music_library[artist]:
                    del self.music_library[artist]
                return True
            else:
                return False

    
        

