from lib.music_libary import *

def add_music_to_libary():
    music_libary = MusicLibary()
    music_libary.add("The Beatles", "Here comes the sun")
    music_libary.add("The Rolling Stones", "Paint It Black")
    music_libary.add("Eminem", "The Real Slim Shady")
    result = music_libary.list()
    assert result == {"The Beatles": "Here comes the sun",
"The Rolling Stones": "Paint It Black",
"Eminem":"The Real Slim Shady"}
    