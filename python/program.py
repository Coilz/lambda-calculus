from pair import create_pair, replace_fst, replace_snd
from person import address, naw, person
from person_formatting import fullAddress, fullCity, fullName, fullNaw, fullStreet
from basic_types import T, F

a_person = person('Erwin')('Konink')
a_address = address(create_pair('Anijsstraat')(74))(create_pair('7322 PS')('Apeldoorn'))
a_naw = naw(a_person)(a_address)

print(a_person(fullName))
print('----------------')
print(a_address(fullAddress))
print('----------------')
print(a_naw(fullNaw))
print('=================')


# update a_person
a_person = replace_fst(a_person)('Roos')

print(a_person(fullName))
print('----------------')
print(a_naw(fullNaw))
print('----------------')


print(a_person(T))