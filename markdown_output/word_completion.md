# WordCollection Class

Word lookup based on a Patricia tree (a.k.a. Radix Tree, a.k.a. Trie
data structure). This data structure is efficiently searchable by the
prefix of words. Such a prefix search takes a string prefix, and returns
all dictionary words that begin with that prefix.

This class ingests rank/word pair files in a given directory. The ranks
are intended to be relative usage frequencies. The class manages these
frequency ranks.

Public methods:

-   `add(word)`
-   `contains(word)`
-   `prefix_search(prefix)`
-   `rank(word)`

`WordCollection` can be subclassed.

# TelPadEncodedWordCollection Subclass

Instances behave as the superclass `WordCollection`. However, all added
words are encoded as if entered via a telephone pad. Each letter group
of the telephone pad is represented by its first letter. Example:
\"and\" \--\> \"amd\" (phone buttons 1,5,2).

The class can thus be used to search words by entering for each real
word\'s letters \'c\' the first letter of the telephone pad that
contains \'c\'. For word input, clients need not concern themselves with
this encoding. That transformation occurs automatically.

However, calls to `search_prefix()` or `contains()` must encode the real
words with the encoded version. Thus, instead of calling
`myColl.contains("and")`, the client would call
`myColl.contains("amd")`. Method `encodeWord()` takes a real word and
returns the encoded version.

Method `search_prefix()` will usually contain a larger number of
\'remaining possible words\' than a regular
[#WordCollection](#WordCollection). This is because the mapping from
encoded to real words is one-to-many.
