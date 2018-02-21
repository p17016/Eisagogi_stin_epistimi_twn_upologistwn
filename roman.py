while True:
		try:
			arithmos = int(raw_input('Dwse enan arithmo apo to 1 mexri to 1000000: '))			#o xrisths dinei enan arithmo
			if arithmos<1 or arithmos> 1000000:													#elegxei an einai metaxy toy 1 kai toy 1000000
				print "Lathos, o arithos poy edwses einai poly megalos!Diavase tis odigies."	
				continue																		#o xrisths borei na xanadwsei enan arithmo
			break
		except ValueError:																		#elegxei an o xrisths den exei valei arithmo
			print "To programa dexetai mono arithmoys!"

conv = [[1000000, 'M-'],																		#pinakas me ta aparaithta stoixia gia thn metatroph arithmwn se latinika
		[900000, 'CM-'], [500000, 'D-'], [400000, 'CD-'], [100000, 'C-'],
		[90000, 'XC-'], [50000, 'L-'], [40000, 'XL-'], [10000, 'X-'], 
		[9000, 'IX-'], [8000, 'VIII-'], [7000, 'VII-'], [6000, 'VI-'], [5000, 'V-'],[4000, 'IV-'], [1000, 'M'],
		[900, 'CM'], [500, 'D'], [400, 'CD'], [ 100, 'C'],
        [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'], [  10, 'X'],
        [  9, 'IX'], [  5, 'V'], [  4, 'IV'], [   1, 'I']]
       
num = arithmos
roman = ''
i = 0 
while num > 0:
    while conv[i][0] > num:															#metaferetai sthn adistixh thesh toy pinaka poy yparxoyn ta latinika symbola
		i+=1 
    roman += conv[i][1] 															#prosthetei to adisthxo latiniko symbolo sto string poy tha ektiposoyme
    num -= conv[i][0] 																#meiwnei apo ton arithmo poy dwthike ton arithmo poy prosthethike sto string me ta latinika symbola

print roman

