from boDimension import boDim
from boObject import boObject
from BusinessObject import *

A = A("Stevens")
print(A.getName())


def countTabs(value):
	return (len(value) - len(value.lstrip())) / 4






busObj = None
#count = 0

with open('universe.txt') as file:

	inObjLayGroup = 0 # indicates whether current parsed line is within the Object Layout Section
	inDimAttrGroup = 0 # indicates whether current parsed line is within the Dimensions and Attributes Section
	inIndiDimGroup = 0 # indicates whether current parsed line is within an individual dimension grouping
	isBlankLine = 0 # indicates whether the parsed line is blank to be used in the next iteration
	prevLine = None
	skipNextLine = 0
	dimensionList = []

	errorCount = 0
	count = 0
	for line in file:
		count=count+1

		if(skipNextLine == 1):
			# once 'Object layout' is found, skip the next (useless) line
			if(inObjLayGroup == 1):
				skipNextLine = 0
			elif(inDimAttrGroup == 1):
				skipNextLine = 0


		elif(skipNextLine != 1):

			if('Object layout' in line):
				inObjLayGroup = 1
				skipNextLine = 1

			elif(inObjLayGroup == 1 and skipNextLine != 1):
				tabs = countTabs(line)
				line = line.lstrip().rstrip('\n')

				# If there are no tabs, the Object Layout section is over
				if(tabs < 1 or not line):
					inObjLayGroup = 0

				# If tabs is 1, the current line is the Universe name, and should be the main object folder
				elif(tabs == 1):
					busObj = boObject(line, tabs)

				if(tabs > 1):
					busObj.addObject(line, tabs)


			elif('Dimensions and Attributes' in line):
				print('here')
				inDimAttrGroup = 1
				skipNextLine = 1

			elif(inDimAttrGroup == 1 and skipNextLine != 1):
				tabs = countTabs(line)
				line = line.lstrip().rstrip('\n')

				count=count+1
				if(inIndiDimGroup == 0 and 'Dimension' in line and '-------------------------------------------------' in next(file)):
					inIndiDimGroup = 1
					line = line.replace('Dimension: ', '')
					newDim = boDim(line)
					prevLine = next(file).lstrip().rstrip('\n')
					count = count+1

				elif(inIndiDimGroup == 1):

					if('coreItemIdentifier' in line):
						newDim.setAttr('coreItemIdentifier', line)
					elif('overridableProperties' in line):
						newDim.setAttr('overridableProperties', line)
					elif('businessName' in line):
						newDim.setAttr('businessName', line)
					elif('description' in line):
						newDim.setAttr('description', line)
					elif('state' in line):
						newDim.setAttr('state', line)
					elif('dataType' in line):
						newDim.setAttr('dataType', line)
					elif('access' in line):
						newDim.setAttr('access', line)
					elif('forResult' in line):
						newDim.setAttr('forResult', line)
					elif('SQL Definition' in line):
						newDim.setAttr('SQL Definition', line)
					elif('List of Values' in line):
						newDim.setAttr('List of Values', line)
					elif('Can be used in' in line):
						newDim.setAttr('Can be used in', line)

					elif(line and not tabs):
						#print('RIGHT HERE MOTHERFUCKER')
						newDim.appendAttribute(newDim.getPrevAttr(), line)

					elif not line:
						inIndiDimGroup = 0
						dimensionList.append(newDim)
					else:
						print(line)




#busObj.printAll()
print(len(dimensionList))








#
