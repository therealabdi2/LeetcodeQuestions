'''
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        # these 2 pointers are pointing at the first pos at the string
        left = right = 0

        palindrome = [[0] * n for _ in range(n)]

        # Outer loop starting from 2nd index
        for j in range(1, n):
            # inner loop starts from first index and runs upto j
            # we are comparing here
            for i in range(0, j):
                # remember if len is < 2 then there is nothing in b/w i and j str
                # e.g whatever is b/w aa is empty
                inner_is_palindrome = palindrome[i + 1][j - 1] or j - i <= 2

                # if true then that means string with starting pos of i and ending pos of j
                # is palindrome
                if s[i] == s[j] and inner_is_palindrome:
                    palindrome[i][j] = True
                    # after we confirm it is Palindrome we need to check if new length is longer
                    # than the previous one, we update left and right pointers if they are
                    if j - i > right - left:
                        left = i
                        right = j
        return s[left:right + 1]


s = Solution()
print(s.longestPalindrome("rgszobovkyonbtps"
                          "jnygxkugokdascyhw"
                          "vqiawupiesrqewwyxwzqfalcg"
                          "tnyppflgghrkwvwtaugkllyqoonz"
                          "obflqjkcmhlstbmqungfzvb"
                          "kucdrvciifri"
                          "aebpicmuavesdnu"
                          "cgmhdmzkpwocerostwzipukprmpcltrkvafgqavfhh"
                          "mojwypttnymjgluohwzhjlmxluvosyfcnajuvphlrmzd"
                          "mmmyarpnhmypgygshuegfnnlktotiqpmjtuaig"
                          "xechjtwwvceqrfmtzwevryyhivbcsgnldfiaedbumm"
                          "zzqfasmpveyzasgleiuqltwauvdaheesaaroytlhfdy"
                          "jsjwgfpgllmwajkujooahsspfirjeyimoacfzcojqgpiq"
                          "tplkondgfiqqxwakkwvsrumkalvdtokrityxwxmsmprraotxheqgthpucu"
                          "gjlhrllakkbfmmfbkkallrhljgucuphtgqehxtoarrpmsmxwxytirkotdvlak"
                          "mursvwkkawxqqifgdnoklptqipgqjoczfcaomiyejrifpsshaoojukjawmllg"
                          "pfgwjsjydfhltyoraaseehadvuawtlq"
                          "uielgsazyevpmsafqzzmmubdeaifdl"
                          "ngscbvihyyrvewztmfrqecvwwtjhcexgiautjmpq"
                          "itotklnnfgeuhsgygpymhnpraymmmdzmrlhpvujancf"
                          "ysovulxmljhzwhoulgjmynttpywjomhhfvaqgfavkrtl"
                          "cpmrpkupizwtsorecowpkzmdhmgcundsevaumcipbeairf"
                          "iicvrdcukbvzfgnuqmbtslhmckjqlfboznooqyllkguatwvwk"
                          "rhgglfppyntgclafqzwxywweqrseipuwaiqvwhycsadkogukxgynjsptbnoykvobozsgr"))
