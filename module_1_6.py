my_dict = {"Alex" : 1982, "Denis" : 2000, "Nikolai" : 1975}
print(my_dict)
print(my_dict ["Denis"])

print(my_dict.get("Anton"))
my_dict.update ({"Vera" : 2005,
                "Lehca" : 1986})
print(my_dict)
c = my_dict.pop ("Alex")
print(c)
print(my_dict)

my_set = {1,2,3,4,3,4,2,1,"Mahca", "Kola", "Mahca"}
print(my_set)
print(my_set.add(5))
print(my_set.add("Alex"))
print(my_set.discard(3))
print(my_set)