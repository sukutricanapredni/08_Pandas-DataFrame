# #1.Zadatak
# ##Iz fajla data.csv ucitati podatke i izracunati prosecan puls
import pandas as pd

# dt=pd.read_csv('data.csv')
# print(dt)
# print(dt.loc[0:,'Pulse'].mean())

# #2.Zadatak
# #Ucitati podatke iz file.csv fajla i ispisati najvecu i najmanju ocenu

# dt=pd.read_csv('file.csv')
# print(dt.loc[0:,'Ocena'].agg(['min','max']))

# ##3.Zadatak
# #uctati podatke iz eksel.xlsx fajla i eksportovati ih u file.csv fajl 
# dt=pd.read_excel('eksel.xlsx',sheet_name='Sheet1')

# dt.to_csv('file.csv',index=False)

##4.Zadatak
##Ucitati podatke iz eksel1.xlsx fajla i dodati novu kolonu odeljenje
##i eksportovati nazad u eksel1.xlsx fajl
dt=pd.read_excel('eksel1.xlsx',sheet_name='Sheet1')
print(len(dt))
l=[1,2,3,4,5,6]
dt['Odeljenja']=l
print(dt)
dt.to_excel('eksel1.xlsx',index=False)

##5.Zadatak
##Ucitati podatke iz eksel.xlsx fajla i naci ime osobe sa najvecom
#platom
dt=pd.read_excel('eksel.xlsx',sheet_name='Sheet1')
print(dt.loc[0:,('Ime','Plata')].max())
print()
