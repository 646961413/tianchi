#!usr/bin/env python
# coding=utf-8

f=open('newdata.csv')
context=f.readlines()

##统计一下|set（当天购买的u-brand对）交集set（前n天的交互u-brand对）|除以|set（当天购买的u-brand对）|
n=7
ubrand_byday=[set() for i in range(31)]
ubrand_buy_byday=[set() for i in range(31)]
for line in context:
	line=line.replace('\n','')
	array=line.split(',')
	if array[0] == 'user_id':
		continue
	if array[-1][5:7]=='11':
		day=int(array[-1][8:10])-18
	else:
		day=int(array[-1][8:10])+12
	ubrand=(array[0],array[4])
	ubrand_byday[day].add(ubrand)
	if array[2]=='4':
		ubrand_buy_byday[day].add(ubrand)

for i in range(31):
	count=0.0
	if i<n:
		continue
	for ubrand in ubrand_buy_byday[i]:
		for j in range(n):
			if ubrand in ubrand_byday[i-j-1]:
				count+=1
				break
	print '%d:%f,%f'%(i,count,count/len(ubrand_buy_byday[i]))
