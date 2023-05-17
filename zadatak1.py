import pandas as panda

p=panda.DataFrame({'Ime':['Marko','Miljana','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Milovanovic','Nikolic','Simic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,5,5,1],
                   'Razred':[7,6,8,7,7,8]})

print(p)

print(p.iloc[0:2,0:1])
print(p.loc[0:2,('Ime','Prezime','Razred')])

print(p.head(2))
print(p.tail(2))
print(p.shape)
print(p.describe())

print(p.size)
print(p.sum())
print('Ocena suma',p.loc[0:,('Ocena',)].sum())
print('Poslednja ocena',p.loc[-1:,('Ocena',)])
print('Prva ocena',p.loc[:1,('Ocena',)])
print('Srednja ocena',p.loc[0:,('Ocena',)].mean())
print('Najveca ocena',p.loc[0:,('Ocena',)].min())
print('Najmanja ocena',p.loc[0:,('Ocena',)].max())


