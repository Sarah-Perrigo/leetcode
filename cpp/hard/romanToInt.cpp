// This program takes a roman numeral and converts it to an integer

# include <iostream>

class Solution {
public:
    int romanToInt(string s) {


            int result = 0;

            // make sure the roman numeral is between 1 and 15 characters
            if (not (1 <= s.length() && s.length() <= 15))
                cout << "Your roman numeral must be between 1 and 15 characters";
            

            /*parses through every value in the roman numeral and adds the
                correct amount to the result*/
            for (int i = 0; i < s.length(); i++) {
                switch (s[i]) {
                    case 'I':
                        if (s[i+1] == 'V' || s[i+1] == 'X')
                            result -= 1;
                        else
                            result += 1;
                        break;
                    case 'V':
                        result += 5;
                        break;
                    case 'X':
                        if (s[i+1] == 'L' || s[i+1] == 'C')
                            result -= 10;
                        else
                            result += 10;
                        break;
                    case 'L':
                        result += 50;
                        break;
                    case 'C':
                        if (s[i+1] == 'D' || s[i+1] == 'M')
                            result -= 100;
                        else
                            result += 100;
                        break;
                    case 'D':
                        result += 500;
                        break;
                    case 'M':
                        result += 1000;
                        break;
                }
            }
            return result;

        }

        int main() {

            cout << "Enter roman numeral: ";
            string roman;
            cin >> roman;

            cout << romanToInt(roman);

            return 0;
        }

    
};