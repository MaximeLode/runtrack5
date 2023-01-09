liste_notes = [42, 40, 45, 80, 82, 83, 84, 85, 87, 90, 100]

def arrondir_notes(notes):
  def arrondir(note):
    if note < 40:
      return note
    elif note % 5 >= 3:
      return note + (5 - note % 5)
    else:
      return note
  return [arrondir(n) for n in notes]
print(arrondir_notes(liste_notes))