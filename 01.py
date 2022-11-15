#Funkcijas-print(izvada datus), input(reģistrē lietotāja datus), int(pārvērš norādīto vērtību veselā skaitlī), str() 

#1.MAINĪGO IZVEIDE
x=5 #integer(vesels sk.), float(decimāld.)
y='abc' #string

z=False #bool - True/False
print(3>5) #--> izvadīs False

print(5+5)

#2.
age = input("How old are you?")  #izvadīs jaut. un uz to cilvēks varēs atbildēt

#3. SARAKSTI- LIST (saraksta nosauk. = [])
punkti = [2, 13, 5, 4, 20, 8]
#index    0    1  2  3  4   5

#print(saraksta nosauk[el.nr./index])
print(punkti[1])  #izvadīsies 13

#4.VĀRDNĪCAS - DICTIONARY
tulkojumi = {
  'sun': 'saule', # 'key(atslēga)' : 'value(vērtība)'     
  'dog': 'suns',     
  'car': 'auto'
  }
  
#print(vardnicas nosauk.['key']) 
print(tulkojumi['dog'])

#5 IF, ELIF, ELSE
#UZD. Ja lietotāja vecums ir mazāks par 20, tad viņš iet skolā. Ja viņam ir jaunāks par 24, tad iet universitātē. Parējos gadījumos visticamāk strādā. 

age = 30

If age < 20:  
  print('Tu ej skolā')
  
Elif age < 24:  #sasaistīts ar iepriekšējo --> lai nebūtu jāraksta -  If age > 20 and age < 24
  print('Tu ej uni')
  
Else:           #visi pārējie gadījumi --> lai nebūtu jāraksta age > 24
  print('Tu strādā!')
