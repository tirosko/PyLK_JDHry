# https://www.geeksforgeeks.org/quizzes/python-list-quiz/


# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# # Indexing a list using index() method
# # pos = nameList.index("GeeksforGeeks")
# pos1 = nameList.index("Pratik")
# print (pos1)

# Kviz 4
# li = [1, 3, 5, 7, 9]
# # print(li.pop(-3), end = ' ')
# # Pop remove a specific element from the list using index
# print(li.pop(-3))
# print(li)

# Vysvetliť kód a jeho výstup. Copy zoznamu `a` obsahuje pôvodný zoznam `[1, 2, 3, 4]`.
# Keď priradíme `b = a`, `b` sa stáva referenciou na ten istý zoznam, takže zmeny v `a` sa prejavia aj v `b`.
# Naopak, `c = a.copy()` vytvára nový zoznam, ktorý je kópiou pôvodného zoznamu `a`, takže zmeny v `a` neovplyvnia `c`.
# Keď zmeníme `a[0]` na `[5]`, zmení sa prvý prvok zoznamu `a` na nový zoznam `[5]`.
# Pretože `b` odkazuje na ten istý zoznam, zmeny sa prejavia aj v `b`, zatiaľ čo `c` zostane nezmenený.
# Zoznam `d` je tiež referenciou na ten istý zoznam, takže zmeny v `a` sa prejavia aj v `d`.
# a = [1, 2, 3, 4]
# b = a
# c = a.copy()
# d = a
# a[0] = [5]
# print(a, b, c, d)

# Kvíz 6
# li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# val1, val2 = 0,''
# for x in li:
# 	if(type(x) == int or type(x) == float):
# 		val1 += x
# 	elif(type(x) == str):
# 		val2 += x
# 	else:
# 		break
# print(val1, val2)


# li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# # val2 je prázdný řetězec, takže když se k němu přidá 'GFG', stane se z něj 'GFG'.
# val1, val2 = 0,''
# for x in li:
# 	if isinstance(x, (int, float)):
# 		val1 += x
# 	elif isinstance(x, str):
# 		val2 += x
# 	else:
# 		break
# print(val1, val2)

# Kvíz 7
# a = []
# print(a)
# a.append([1, [2, 3], 4])
# print(a)
# a.extend([7, 8, 9])
# print(a)
# print(a[0][1][1])
# print(a[2])
# print(a[0][1][1] + a[2])

# Kvíz 8
# a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if (x in ([x for x in range(20)]))]
# print(a)

# Pokračovanie kvízu 8
