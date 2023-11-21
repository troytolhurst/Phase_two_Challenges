from lib.diary_class import Diary
from lib.diary_entry_class import DiaryEntry

def test_diary_intialises_with_empty_list():
    diary = Diary()
    assert diary.diary_entries == []


def test_diary_adds_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("day 1", "Day 1 was great!")
    diary.add(diary_entry_1)
    result = diary.all()
    entry_contents = [(entry.title, entry.contents) for entry in result]
    assert entry_contents == [("day 1", "Day 1 was great!")]

def test_diary_adds_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Day 1 was great")
    diary_entry_2 = DiaryEntry("Day 2", "Day 2 was not so great")
    diary_entry_3 = DiaryEntry("Day 3", "Back to world domination!")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    result = diary.all()
    entry_contents = [(entry.title, entry.contents)for entry in result]
    assert entry_contents == [("Day 1", "Day 1 was great"),("Day 2", "Day 2 was not so great"), ("Day 3", "Back to world domination!")]

def test_add_entries_and_check_word_count():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Day 1 was great")
    diary_entry_2 = DiaryEntry("Day 2", "Day 2 was not so great")
    diary_entry_3 = DiaryEntry("Day 3", "Back to world domination")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.count_words() == 14

def test_add_entry_and_check_read_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Day 1 was great")
    diary.add(diary_entry_1)
    result = diary_entry_1.reading_time(1)
    assert result == 4 
    
def test_add_entries_and_check_diary_read_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Day 1 was great")
    diary_entry_2 = DiaryEntry("Day 2", "Day 2 was not so great")
    diary_entry_3 = DiaryEntry("Day 3", "Back to world domination")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    result = diary.reading_time(1)
    assert result == 14

def test_add_entry_and_test_chunk_read_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Coding is very fun but I think I will play with the xbox game")
    chunk_1 = diary_entry_1.reading_chunk(1, 7)
    chunk_2 = diary_entry_1.reading_chunk(1, 7)
    assert chunk_1 == "Coding is very fun but I think"
    assert chunk_2 == "I will play with the xbox game"

def test_add_entries_and_test_best_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Day 1", "Coding is very fun but I think I will play with the xbox game")
    diary_entry_2 = DiaryEntry("Day 2", "Day 2 was not so great")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    result = diary.find_best_entry_for_reading_time(2, 10)
    assert result == diary_entry_1



