import random

rakip_el = str(random.choice(["taş","kağıt","makas"]))

el = input("""
1) Taş
2) Kağıt
3) Makas
""")

if rakip_el == "taş":
	if el == "kağıt" or "2":
		print(f"kaybettin occ, karşındaki {rakip_el} seçti")
	elif el == "makas" or "3":
		print(f"kazandin occ, , karşındaki {rakip_el} seçti")
	elif el == "taş" or "1":
		print("berabere kaldin occ karşındaki de {} seçti".format(rakip_el))

elif rakip_el == "makas":
	if el == "kağıt" or "2":
		print(f"kaybettin occ, karşındaki {rakip_el} seçti")
	elif el == "makas" or "3":
		print(f"berabere kaldin occ, karşındaki de {rakip_el} seçti")
	elif el == "taş" or "1":
		print(f"kazandin occ, karşındaki {rakip_el} seçti")

elif rakip_el == "kağıt":
	if el == "makas" or "3":
		print(f"kaybettin occ, karşındaki {rakip_el} seçti")
	elif el == "taş" or "1":
		print(f"kazandin occ, karşındaki {rakip_el} seçti")
	elif el == "kağıt" or "2":
		print(f"berabere kaldin occ, karşındaki de {rakip_el} seçti")

else:
  print("amnıa koyim")
