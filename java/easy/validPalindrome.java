// This program takes a string and determines if it is a palindrome
// Rating: Easy

class Solution {

    public boolean isPalindrome(String s) {

        StringBuilder original = new StringBuilder(s.toLowerCase());

        int i = 0;
        int j = original.length() - 1;

        if ((original.length() < 1 || original.length() > 200000)) {
            System.out.println("Invalid string length");
            return false;
        }  


        while (i <= j) {

            if (!Character.isLetterOrDigit(original.charAt(i))) {
                i++;
            }
            else if (!Character.isLetterOrDigit(original.charAt(j))) {
                j--;
            }

            else {
                if (original.charAt(i) != original.charAt(j)) {
                    return false;
            }

            i++;
            j--;

            }
        }
        
        return true;

        }
    }