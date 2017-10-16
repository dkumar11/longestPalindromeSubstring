
#************************PROBLEM DEFINITION************************
#
""" A subsequence is palindromic if it is the same whether read left to right 
orright to left. For example, “bob” and “racecar” are palindromes, but “cat” 
is not. Devise an algorithm that takes a sequence x[1..n] and returns the length
of the longest palindromic subsequence. Its running time should be O(n2). 
(Recall that a subsequence need not be consecutive, e.g. “aba” is the longest 
palindromic subsequence of “anbma”.) For this problem, you should know how to do 
the proof of correctness, but need not include it in your submission. 
You should submit the main idea, pseudocode, and runtime.
"""


#************************SOLUTION************************
def longestPalindromeLength(input_str):
	""" Returns the length on the largest palindrome
		subsequence in the input string strg.

		>>> longestPalindromeLength("abbabasmbba")
		'The length of the largest Palindrome is 9'
		
		>>> longestPalindromeLength("abba")
		'The length of the largest Palindrome is 4'
		
		>>> longestPalindromeLength("Saippuakivikauppias")
		'The length of the largest Palindrome is 19'
		
		>>> longestPalindromeLength("")
		'The length of the largest Palindrome is 0'
		
		>>> longestPalindromeLength("a")
		'The length of the largest Palindrome is 1'
		
		>>> longestPalindromeLength(65687)
		'Incorrect input. Please input a String'


	"""
	# HELPER FUNCTION
	equal = lambda x, y: x == y

	if isinstance(input_str,str):
		strg = str.lower(input_str)
		n = len(strg)
		if n == 0:
			return "The length of the largest Palindrome" + " is " + str(0)
		M = [[0 for i in range(0,n)] for i in range(0,n)]
		for i in range(0,n):
			M[i][i] = 1

		for i in range(n-1, -1, -1):
			for j in range( i + 1, n):
				if equal(strg[i], strg[j]):
					M[i][j] = 2 + M[i + 1][j - 1]
				else:
					M[i][j] = max(M[i][j - 1], M[i + 1][j])
		return "The length of the largest Palindrome" + " is " + str(M[0][n-1])
	else:
		return "Incorrect input. Please input a String"

if __name__ == "__main__":
    import doctest
    doctest.testmod()