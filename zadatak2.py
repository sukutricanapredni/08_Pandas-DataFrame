import pandas as panda

p=panda.DataFrame({'Ime':['Nikola'],'Prezime':['Savic']})
print(p)

p.loc[len(p)]=['Marta','Kacarevic']
p.loc[4]=['Nikola','Nikolic']
print(p)
p.drop(1,axis=0,inplace=True)
print(p)
p.drop('Prezime',axis=1,inplace=True)
print(p)

