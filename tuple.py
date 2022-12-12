#Дано 2 множества, содержащих названия IT-компаний. Найти только те компании, которые содержатся в обоих множествах.
it_group_1 = {'Epam', 'Overeone', 'Google', 'Apple'}
it_group_2 = {'Epam', 'Google', 'Apple'}
print(type(it_group_1))
print(it_group_1 & it_group_2)