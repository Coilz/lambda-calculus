from basic_types import T, F

create_pair = lambda x: lambda y: lambda f: f(x)(y)
replace_fst = lambda pair: lambda r: pair(lambda x: lambda y: create_pair(r)(y))
replace_snd = lambda pair: lambda r: pair(lambda x: lambda y: create_pair(x)(r))

fst = lambda pair: pair(T)
snd = lambda pair: pair(F)
