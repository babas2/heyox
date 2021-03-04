




import random

a1 = {"sual": "Babaş Necə İnsandı?", "cvb": "Mükəmməl", "cvb2": "mükəmməl"}
a2 = {"sual": "Nurlan Kimdi", "cvb": "alverçi", "cvb2": "Alverçi"}

suallar = a1, a2
# suallar = open("sozler.txt", "r")
ss = random.choice(suallar)

cc = input((ss["sual"]))

if cc == ss["cvb"]:
  print("doğru brat")



















