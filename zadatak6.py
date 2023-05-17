import pandas as pd

dt=pd.read_csv('data.csv')

p=pd.DataFrame({'Ime':['Marko','Miljana','Stefan','Marija','Sofija','Nenad'],
                   'Prezime':['Savic','Milovanovic','Nikolic','Simic','Marijanovic','Lovric'],
                   'Ocena':[4,3,5,5,5,1],
                   'Razred':[7,6,8,7,7,8]})

p.to_csv('file.csv',index=False)

dt=pd.read_csv('file.csv')

print(dt)