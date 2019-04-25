from pair import create_pair, replace_fst, replace_snd
from person import address, naw, person
from person_formatting import fullAddress, fullCity, fullName, fullNaw, fullStreet
from basic_types import T, F

a_person = person('Christine')('Ramirez')
a_address = address(create_pair('Coolidge Street')(1816))(create_pair('MT 59601')('Helena'))
a_naw = naw(a_person)(a_address)

print(a_person(fullName))
print('----------------')
print(a_address(fullAddress))
print('----------------')
print(a_naw(fullNaw))
print('=================')


# update a_person
a_person = replace_fst(a_person)('Stephen')

print(a_person(fullName))
print('----------------')
print(a_naw(fullNaw))
print('----------------')


print(a_person(T))