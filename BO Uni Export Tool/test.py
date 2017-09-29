from collections import OrderedDict


objectList = []
i = 0

with open('HRInfoUni.txt') as file:

	inObjLay = 0
	skipNextLine = 0

	prevTabCount = 0

	for line in file:
#		print(len(line) - len(line.lstrip()))

		if(skipNextLine == 1):
			print('skip this ' + line)

			# once 'Object layout' is found, skip the next (useless) line
			if(inObjLay == 1):
				skipNextLine = 0





		elif(skipNextLine != 1):
			if('Object layout' in line):
				inObjLay = 1
				skipNextLine = 1
			elif(inObjLay == 1 and skipNextLine != 1):
				tabs = (len(line) - len(line.lstrip())) / 4
				line = line.lstrip().rstrip('\n')

				if(tabs < 1):
					inObjLay = 0
					break

				elif(tabs == 1):
#					print('true '+str(line))
					diction = OrderedDict({line: []})
					objectList.append(diction)
					prevTabCount = tabs



				elif(tabs == 2):
					nextLine = next(file)
					nextTabs = (len(nextLine) - len(nextLine.lstrip())) / 4
					if(nextTabs > 2):
						diction = OrderedDict({line: []})
					else:
						diction = line

					if(prevTabCount == 2):
						objectList.append(diction)

					if(prevTabCount == 1):
						length1 = len(objectList) - 1
						lastKey = next(reversed(objectList[length1]))
						objectList[length1][lastKey].append(diction)
						print(objectList[length1][lastKey])

					prevTabCount = tabs



				elif(tabs == 3):
					nextLine = next(file)
					(len(nextLine) - len(nextLine.lstrip())) / 4
					if(nextTabs > 3):
						diction = {line: []}
					else:
						diction = line

					if(prevTabCount == 3):
						objectList.append(diction)

					if(prevTabCount == 2):
						print('start')
						print(objectList)
						length1 = len(objectList) - 1
						print('length '+ str(length1))
						lastKey = next(reversed(objectList[length1]))
						length2 = len(objectList[length1][lastKey]) - 1
						lastKey2 = next(reversed(objectList[length1][lastKey][ length2 ]))

						print(objectList[length1][lastKey][length2][lastKey2])
						objectList[length1][lastKey][length2][lastKey2].append(diction)
						#print(objectList[0][lastKey])
					#objectList.append(diction)

					prevTabCount = tabs





#				print('hey ' + line)
#print(objectList)










#
