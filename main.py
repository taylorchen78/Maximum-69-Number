"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

def maximum69Number (num):
	numList = [x for x in str(num)]
	print(numList)

	sixLoc = 0;
	if "6" not in numList:
		return num
	else:
		sixLoc = numList.index("6")
		numList[sixLoc] = "9"

		return int(''.join(numList))


print(maximum69Number(9669))
print(maximum69Number(9996))
print(maximum69Number(9999))