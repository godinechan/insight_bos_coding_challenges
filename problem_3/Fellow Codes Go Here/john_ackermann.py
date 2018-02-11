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

def is_substring_helper (s):
    # get number of unique elements in string 's'
    uni_s = len(list(set(s)))
    # get length of 's'
    len_s = len(s)
    # check whether length s is divisible by uni_s
    if not len_s % uni_s:
       # if so, construct a new string using copies
       # of the unique elements of s
       ele_s = s[:uni_s]
       new_s = ele_s
       while len(new_s) < len(s):
           new_s = new_s + ele_s
       # check whether new_s = s
       if new_s == s:
           return True
       else:
           return False
    else:
        return False

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