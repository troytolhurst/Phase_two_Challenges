"""
when we add 2 diary entries 
we get all diary entries back in a list
"""
diary = Diary()
diary_entry_1 = DiaryEntry("day 1", "Day 1 was great!")
diary_entry_2 = DiaryEntry("day 2", "Day 2 was also great!")
diary.add(diary_entry_1) diary.all => [diary_entry_1,diary_entry_2]