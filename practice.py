numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_num = [num for num in numbers if num<=0]
print(neg_num)
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [nums for sub in list_of_lists for nums in sub]
print(flat_list)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_cunt = [nums for sub in countries for nums in sub]
print(flat_cunt)
lst = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
list_into_tuples = [tuple(row) for row in lst]
print(type(list_into_tuples[0]))
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_into_dict = [dict(sub) for sub in countries]
print(type(list_into_dict[0]), list_into_dict)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
pri = [f"{first} {last}" for first, last in [sub[0] for sub in names]]
print(pri)