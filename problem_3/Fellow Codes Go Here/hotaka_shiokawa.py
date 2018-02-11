"""
Given a string check if it can be constructed by taking a substring of it and appending multiple copies of the substring 
together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

# O(n * number of divisor) version
def is_substring_helper (data):
    # YOUR CODE HERE
    n = len(data)
    for i in range(1,n/2+1): # no need to go beyond n/2
        if n%i==0 and data[:i]*(n//i)==data:
            return True
    return False

"""
# Pure O(n) version, but somewhat more complicated.
def is_substring_helper (data):
    # YOUR CODE HERE
    n = len(data)
    i1 = 0 
    i2 = 1
    candidate = False
    while i2 < n:
        if (data[i1] != data[i2]) and candidate:
                i1 = 0
                candidate = False
        if (data[i1] == data[i2]):
            if candidate == False and n%i2==0:
                    len_substr = i2
                    candidate = True
            i1 += 1
        i2 += 1

    if candidate: return True
    else: return False
"""



#DON NOT CHANGE THIS FUNCTION
def is_substring (string_input):
	return is_substring_helper(string_input)


#test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

if __name__ == "__main__":
    main()
