




import random

a1 = {"sual": "Babaş Necə İnsandı?", "cvb": "mükəmməl"}
a2 = {"sual": "Nurlan Kimdi", "cvb": "alverçi"}

suallar = a1, a2
# suallar = open("sozler.txt", "r")
random.choice(suallar)


a = input((suallar["sual"]))

if a == suallar["cvb"]:
  print("doğru")



















