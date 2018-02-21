import random

nums=[i for i in range (-30,31)]				#lista me oloys toys arithmoys poy boroyn na epilexthoyn
rand_nums = random.sample(nums, 30)				#tyxaia lista 30 arithmwn poy anhkoyn sthn panw lista
combinations = 0								#metavlith poy tha dixei an yparxoyn syndiasmoi me athrisma 0
for j in range(0,30):							#elexoyn oles tis pithanes 3ades ths tyxaias listas
	for x in range(j+1,30):
		for z in range(x+1,30):
			if rand_nums[j] + rand_nums[x] + rand_nums[z] == 0 :		#elexei an to athrisma ths kathe triadas einai iso me to 0 kai an einai to typwnei
				print "Prosthetodas tous exis tris arithmoys ths tyxaias listas:", rand_nums[j], rand_nums[x], rand_nums[z], "pairneis athrisma iso me to 0"
				combinations += 1
if combinations == 0 :
	print "Den yparxei kanenas syndiasmos ths tyxaias listas poy to athrisma toy na einai 0"