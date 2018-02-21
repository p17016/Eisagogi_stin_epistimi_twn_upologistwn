import datetime

tags = { 1 : 'Deytera' ,2 : 'Trith' ,3 : 'Tetarth' ,4 : 'Pempth' ,5 : 'Paraskeyh' ,6 : 'Savato' ,7 : 'Kyriakh' } #orizw antistixia arithmws epistrofhs ths isoweekday me meres ths evdomadas
count = 0

currentDay = datetime.datetime.now().day		#trexon arithmos ths hmeras 
currentMonth = datetime.datetime.now().month	#trexon mhnas
currentYear = datetime.datetime.now().year		#trexon xronos
	
currentWeekDay = tags[datetime.datetime(currentYear,currentMonth,currentDay).isoweekday()]	#epistrefetai h shmerinh mera(onoma)

for i in range(0,10):							#epanalisph gia ta epomena 10 xronia
	for j in range(currentMonth+1,13):			#epanalipsh gia toys mhnes tou xronou
		if tags[datetime.datetime(currentYear,j,currentDay).isoweekday()]==currentWeekDay :
			count += 1
	
	currentMonth = 1							#to orizw 1 gia thn anazhthsh toy epomenoy xronoy kathe epanalipshs
	currentYear += 1

print "Oi meres stis opoies o mhnas exei", currentDay, "kai h mera einai", currentWeekDay, "sta epomena 10 xronia einai sunolika :", count