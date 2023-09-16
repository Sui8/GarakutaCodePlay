S = input()

db = [["tourist", 3858], ["ksun48", 3679], ["Benq", 3658], ["Um_nik", 3648], ["apiad", 3638], ["Stonefeang", 3630], ["ecnerwala", 3613]
, ["mnbvmar", 3555], ["newbiedmy", 3516], ["semiexp", 3481]]

for i in range(len(db)):
  if S == db[i][0]:
    print(db[i][1])
    exit(0)