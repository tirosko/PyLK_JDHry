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
a = [1, 2, 3, 4] 
b = a 
c = a.copy() 
d = a
a[0] = [5] 
print(a, b, c, d)