def fileToList(filename):
	lst = []
	try:
		file_obj = open(filename)
		lines = file_obj.readlines()
		for i in lines:
			lst.append(i.strip())
		return lst
		file_obj.close()
	except:
		return lst

def returnFirstString(lst):
	try:
		return lst[0]
	except:
		return ''

def strandsAreNotEmpty(strand1, strand2):
	if len(strand1) > 0 and len(strand2) > 0:
		return True
	else:
		return False

def strandsAreEqualLengths(strand1, strand2):
	return (len(strand1) == len(strand2))

def candidateOverlapsTarget(target, candidate, overlap):
	a = target[len(target) - overlap:]
	b = candidate[0:overlap]
	return a == b

def findLargestOverlap(target, candidate):
	if target == "" or candidate == "":
		return -1
	elif len(target) != len(candidate):
		return -1
	else:
		overlap = len(target)
		while True:
			a = target[len(target) - overlap:]
			b = candidate[0:overlap]
			overlap -= 1
			if a == b:
				break
		return overlap + 1

def findBestCandidate(target, candidates):
	best = ""
	largest = 0
	for i in candidates:
		ov = findLargestOverlap(target, i)
		if ov > largest:
			largest = ov
			best = i
		elif ov == largest:
			pass
	return (best, largest)

def joinTwoStrands(target, candidate, overlap):
	b = candidate[0:overlap]
	c = candidate.replace(b, "")
	return str(target) + str(c)

def main():
	target_file = input("What's the name of the file with the target string? ")
	candidate_file = input("What's the name of the file with the candidate strings? ")

	target = fileToList(target_file)
	candidate_list = fileToList(candidate_file)

	best = findBestCandidate(target, candidate_list)
	combined = joinTwoStrands(target, best[0], best[1])

	print(combined)

if __name__ == '__main__':
	main()