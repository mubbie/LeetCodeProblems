# Questions

Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

0 <= strs.length < 100 (maximu number of stirngs is 100 - could be zero)
0 <= strs[i].length < 200 (maximum length of each string is 200 - could be zero)

strs[i] contains only UTF-8 characters.


## Solution

### Ideas

- Append each string to a new string with a delimiter seperating them (decode by splitting on the delimiter)
  - For instance, if we use `,` as the delimiter
  - Encode: `["leet","code","love","you"]` -> `"leet,code,love,you"`
  - Decode: `"leet,code,love,you"` -> `["leet","code","love","you"]`
  - Problem: what if the string contains the delimiter itself? e.g `["leet,code","love","you"]` -> `"leet,code,love,you"` -> `["leet","code","love","you"]` (incorrect)
    - Solution: use a delimiter that is unlikely to appear in the strings (this is not a good solution as it is not robust), or use an escape character before the delimiter in the strings (e.g `\`, this makes more sense, but what if the string contains the escape character itself?)
- Append each string to a new string and use the length of each string as an index to identity where it ends (decode by reading the length and slicing accordingly)
  - Encode: `["leet","code","love","you"]` -> `"4leet4code4love3you"`
  - Decode: `"4leet4code4love3you"` -> `["leet","code","love","you"]`
  - Problem: what if the string contains numbers? e.g `["4leet","code","love","you"]` -> `"54leet4code4love3you"` -> `["leet","code","love","you"]` (incorrect)
    - Solution: use a special character to separate the length from the string (e.g `#`)
      - Encode: `["4leet","code","love","you"]` -> `"5#4leet4#code4#love3#you"`
      - Decode: `"5#4leet4#code4#love3#you"` -> `["4leet","code","love","you"]`
    - What other edge cases are there?
      - Empty string: `[""]` -> `"0#"` -> `[""]` (works fine)
      - Empty list: `[]` -> `""` -> `[]` (works fine)
      - Strings with special characters: `["!@#$%^&*()"]` -> `"10#!@#$%^&*()"` -> `["!@#$%^&*()"]` (works fine)

### Implementation

#### Encode

create a new string

for each string in the list
    append the length of the string followed by a special character (e.g `#`)
    append the string itself

return the new string

#### Decode

create an empty list to store the decoded strings

set an index variable to 0

while the index is less than the length of the encoded string
    find the postion of the special character that immediately follows the length of the string (current index)
        this would be index + 1
    extract the length of the string
    extract the string using the length
    append the extracted string to the list
    move the index to the position after the extracted string

return the list of decoded strings

#### Time/Space Complexity

#### Encoding

Looping and adding strings: O(N) time complexity, where N is the total number of characters in all strings.

Space complexity is O(N) for the encoded string.

#### Decoding

Looping through the encoded string: O(N) time complexity, where N is the length of the encoded string.

Space complexity is O(N) for the list of decoded strings.