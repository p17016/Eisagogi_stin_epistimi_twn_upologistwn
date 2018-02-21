import random

sum=0
for n in range(0,1000): 
	#dimiourgia listas arithmwn
	nums=[i for i in range(1,81)]
	random.shuffle(nums)
	
	#dimiourgia epilogwn pektwn
	paixtes=[]
	for i in range (0,100):
		rand_nums = random.sample(nums, 5)
		paixtes.append(rand_nums)

	#lipsi arithmwn mexri na vrethei bingo
	for g in range (1,81):
		bingo=0										#metavliti gia sunthiki eksodou apo tin for
		rand_num = random.choice(nums)				#travaw enan random arithmo apo tin lista me tous arithmous
		nums.remove(rand_num)						#diagrafi tou stoixeiou gia na mn to ksanatraviksw
		for i in range(0,100):
			if rand_num in paixtes[i]:				#an o tuxaios arithmos pou travixtike uparxei stin lista tou paikti i diegrapse ton
				paixtes[i].remove(rand_num)
				if not paixtes[i]:					#An kapoia lista einai keni tote uparxei bingo ara min psakseis allo paikti
					bingo=1							#bingo = 1 giati vrethike bingo ara stamatame na travame arithmous
					break
		if bingo == 1:
			break
			
	sum = sum + g									#athroisma  arithmwn pou travixtikan gia evresi mesou orou
	
print "O mesos oros twn arithmwn poy prepei na anagelthoyn gia na yparxei bingo einai :", sum / 1000