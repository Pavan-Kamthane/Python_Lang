class TrieNode :
    def __init__ ( self ) :
        self.children = {}
        self.isEnd = False
        self.index = -1


class Trie :
    def __init__ ( self ) :
        self.root = TrieNode ()

    def insert ( self , word , index ) :
        node = self.root
        for char in word :
            if char not in node.children :
                node.children [ char ] = TrieNode ()
            node = node.children [ char ]
        node.isEnd = True
        node.index = index

    def search ( self , word ) :
        node = self.root
        for char in word :
            if char not in node.children :
                return (False , -1)
            node = node.children [ char ]
        return (node.isEnd , node.index)


class Solution :
    def pairPalindrome ( self , words ) :
        def is_palindrome ( check ) :
            return check == check [ : :-1 ]

        trie = Trie ()
        for i , word in enumerate ( words ) :
            trie.insert ( word , i )
        valid_pals = [ ]
        for i , word in enumerate ( words ) :
            m = len ( word )
            for k in range ( m + 1 ) :
                prefix = word [ :k ]
                suffix = word [ k : ]
                if is_palindrome ( prefix ) :
                    search , index = trie.search ( suffix [ : :-1 ] )
                    if search and index != i :
                        valid_pals.append ( [ index , i ] )
                if k != m and is_palindrome ( suffix ) :
                    search , index = trie.search ( prefix [ : :-1 ] )
                    if search and index != i :
                        valid_pals.append ( [ i , index ] )
        return valid_pals


if __name__ == '__main__':
   words = ["pa","a","tot","","anagram","cpp","p"]
   print(Solution().pairPalindrome(words))
