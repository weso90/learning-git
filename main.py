#ZADANIE 1

shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
    "cukiernia": ["sernik", "jabłecznik"]
}

for i, j in shopping_list.items():
    print(f"Idę do {i.capitalize()} i kupuję tam: {[j.capitalize() for j in j]}")

print(f"W sumie kupuję {[sum(len(i) for i in shopping_list.values())]} towarów")

print("trzeci branch, sprawdzam czy merge będzie działał")