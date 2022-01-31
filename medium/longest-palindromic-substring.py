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


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        # time complexity O(n^2)
        # space complexity O(n^2)
        # store the longest palindrome here
        res = ''
        res_len = 0  # longest length

        for i in range(len(s)):
            # for odd length palindromes e.g "babad" we are starting in the middle and expanding outwards
            # these left and right pointer are equal to i which is our center currently
            l, r = i, i
            # while l and r are in bound and char at l and r are equal we know this is palindrome in these cases
            # so we can potentially update our result
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # we only add if it is longer than our current result
                if r - l + 1 > res_len:
                    # update result
                    res = s[l:r + 1]
                    # update length
                    res_len = r - l + 1
                # expand out our pointers
                l -= 1
                r += 1

            # for even length palindromes e.g "cbbd" we are starting in the middle and expanding outwards
            # for this just set the right pointer to i + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                # expand out our pointers
                l -= 1
                r += 1
        return res


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

s2 = Solution2()
print(s2.longestPalindrome(s="cbbd"))
