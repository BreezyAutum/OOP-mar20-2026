ui_char_name = input("Enter a name for your character:\n")
ui_char_age = input("Enter your character's age:\n")
ui_char_race = input("Select a race:\n\nHuman\nOrc\nElf\nTroll")
ui_char_job = input("Select a class:\n\nFighter\nWizard\nCleric\nRogue\n")
class player:
  def __innit__(self, charName, charAge, charRace, charJob):
    charName = ui_char_name
    self.charName = charName
    charAge = ui_char_age
    self.charAge = charAge
    charRace = ui_char_race
    self.charRace = charRace
    charJob = ui_char_job
    self.charJob = charJob