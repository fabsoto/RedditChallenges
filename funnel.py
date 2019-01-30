def funnel(word1, word2):
	for i in range(len(word1)):
		copy = word1
		if (copy[:i] + copy[i+1:]) == word2:
			return True
	return False