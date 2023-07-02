/* This program takes a string s and finds the length of the longest
substring within it that does not have repeating characters
Rating: Medium
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {

        String longest = "";

        if (s.length() > 50000) {
            System.out.println("Invalid string length");
            return 0;
        }

        for (int i = 0; i < s.length(); i++) {
            String temp = "";
            temp += s.charAt(i);
            int j = i+1;
            while ((j <= (s.length() - 1)) && (!temp.contains(String.valueOf(s.charAt(j))))) {
                temp += s.charAt(j);
                j++;
            }
                if (temp.length() > longest.length()) {
                    longest = temp;
                }
            }
            
        return longest.length();

        }

    }