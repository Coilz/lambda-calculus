from formatting import concat

fullName = concat(' ')
fullStreet = concat(' ')
fullCity = concat(', ')
fullAddress = lambda a: lambda b: concat('\n')(a(fullStreet))(b(fullCity))

fullNaw = lambda a: lambda b: concat('\n')(a(fullName))(b(fullAddress))
