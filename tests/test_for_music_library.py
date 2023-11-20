from lib.music_library import *

def test_add_music_and_list():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    result = music_library.list()
    assert result == [
        ("Eminem", ["Lose Yourself"]),
        ("The Rolling Stones", ["Paint it Black"]),
        ("The Beatles", ["Here Comes the Sun"])]
    
def test_add_more_songs_to_one_artistand_list():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    music_library.add("Eminem", "Stan")
    result = music_library.list()
    assert result == [
        ("Eminem", ["Lose Yourself", "Stan"]),
        ("The Rolling Stones", ["Paint it Black"]),
        ("The Beatles", ["Here Comes the Sun"])]
    
def test_search_by_artist():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    music_library.add("Eminem", "Stan")
    result = music_library.search_by_artist("Eminem")
    assert result == ["Lose Yourself", "Stan"]

def test_remove_song_by_artist():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    music_library.add("Eminem", "Stan")
    music_library.add("Eminem", "Mockingbird")
    result = music_library.remove("Eminem", "Stan")
    assert result == True
    remaining_songs = music_library.list()
    assert remaining_songs == [("Eminem", ["Lose Yourself", "Mockingbird"]),
        ("The Rolling Stones", ["Paint it Black"]),
        ("The Beatles", ["Here Comes the Sun"])]
    
def test_add_songs_remove_song_and_artist():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    result = music_library.remove("Eminem", "Lose Yourself")
    assert result == True 
    remaining_songs = music_library.list()
    assert remaining_songs == [
        ("The Rolling Stones", ["Paint it Black"]),
        (("The Beatles", ["Here Comes the Sun"]))
        ]
def test_add_songs_remove_song_and_artist():
    music_library = MusicLibrary()
    music_library.add("Eminem", "Lose Yourself")
    music_library.add("The Rolling Stones", "Paint it Black")
    music_library.add("The Beatles", "Here Comes the Sun")
    result = music_library.remove("The Rolling Stones", "Paint it Black")
    assert result == True 
    remaining_songs = music_library.list()
    assert remaining_songs == [
        ("Eminem", ["Lose Yourself"]),
        (("The Beatles", ["Here Comes the Sun"]))]

    

    
    