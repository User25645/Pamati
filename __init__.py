class skolens:  #definē klasi
  def __init__(self, name, surname, grade, grades):  #obligāti raksta SELF, lai varētu izsaukt vērtības(name, surname, ..), kad tiks izveidoti objekti(Jānis, Annija)
    self.name = name #izcauc vērtības ar SELF. --> Jānis.name = Jānis, Jānis.surname = Ozoliņš, ...
    self.surname = surname
    self.grade = grade
    self.grades = grades
Jānis = skolens("Jānis", "Ozoliņš", 11, [8, 7, 5, 9])   #(name, surname, class, grades) - instances atribūti
Annija = skolens("Annija", "Siliņa", 12, [10, 9, 10, 8])  #[], jo saraksts
