
In this challenge, we will try to build a simplified "password checker" 
like those commonly seen on most websites.

*Disclaimer:* This project is for *fun*, and should **not** be used to 
check the complexity of passwords that will protect actual sensitive information. 
(Though if this script says your password is bad, you should be concerned.)

**NOTE:** DO NOT WRITE YOUR ACTUAL PASSWORDS IN THE CYBER-DOJO SESSION. 
THEY WILL BE PUBLICLY STORED AS PLAIN TEXT FOR EVERYONE TO SEE!

# Instructions

This challenge will be hosted on cyber-dojo.org. This will allow you to work 
without needing to install Python on your computer, and you will be able to 
see other members' submissions.

To connect, follow these instructions:
1. Go to https://www.cyber-dojo.org
2. Click "we're in a group"
3. Click "join a session"
4. Enter the ID that will be communicated at the time of the Meetup in 
   the box, then press _Enter_.

Inside the session, you will see:
* On the left of the screen, the controls and list of files
  * To access a file, click on it
  * To save your changes and run the tests, click "test" at the top
* On the right of the screen, the editor for the file that's currently open.

In this challenge, `rate_password.py` is where you are expected to write 
your code. The tests are located in `test_rate_password.py`, and you are 
free to play with them if you wish.

# Description

The expected form of this program is a function that takes a string as 
an argument, and returns an evaluation of its adequateness as a password.

This whole process being somewhat complicated, we will split it in separate 
steps, each built as its own function.

## 1. Length score

Research has shown that the length of a password is generally its most 
significant characteristic. Nowadays, even mid-range consumer-grade graphics 
cards pack up incredible amounts of processing power, enough to crack any 
password up to 8 characters in reasonable time.

Therefore, our first step will be to give a "Length score" to a password 
based on its length. The logic is as follows:
* 0 points for 7 characters or fewer
* 1 point for 8 characters
* +1 point for each additional character

Examples:
* `password` has a score of 1
* `password1234` has a score of 5
* `john` has a score of 0

For this exercise, edit the `length_score` function in the `rate_password.py` file. 
This function takes a password as an argument and returns its length score as a number. 
The `TestLengthScore` class in `test_rate_password.py` contains tests for it, you may 
edit those as well if you wish.

## 2. Commonality check

It is also a terrible idea to choose a password that's common. It is guaranteed 
that attackers will try all the most common password first when trying to crack one.

For this part, write the `is_common` function, which takes a password as an argument
and returns a boolean (`True` or `False`) indicating whether it's common or not. 
For this purpose, a (curated) list of approximately 1,000 common passwords is 
included as `common_password.txt`. You code will need to open that file, read it and 
check if the given password is found or not.

## 3. Complexity score

Finally, a password should be somewhat complex so that the chances of guessing it 
at random are minimal. To measure this, we will give our password a "complexity score", 
which is described below.

Each password starts with a score of 1, then gets points by matching the following rules:
* Has mixed case (uppercase _and_ lowercase): +1 pt
* Has numbers: +2 pts
* Has symbols: +2 pts
* Has any other character: +3 pts

Note: "symbols" are any ASCII non-alphanumeric printable characters, including spaces,
such as:
```.,<>/?{}[]\|()&^%$#@!*```

Additionally, there are rules to penalize lazy passwords:
* Has only one number: -1 pt
* Has only one symbol or other character: -1 pt
* All numbers/symbols are at the end of the password: password complexity worth 2 pts 
  _regardless of all other rules_.

A few examples:
* `password`: 1 pt
* `password123$`: 2 pts (all at the end)
* `H3LLO_WORLD`: 3 pts (1 + 2 for numbers + 2 for symbols - 2 for only one of each)
* `nen9aPhu`: 3 pts (1 + 1 for case + 2 for numbers - 1 for only one number)
* `Ba$th5to`: 4 pts (1 + 1 for case + 2 for numbers + 2 for symbols - 2 for only one of each)
* `Dre1käse`: 5 pts (1 + 1 for case + 2 for numbers + 3 for foreign characters
                     - 2 for only one of each)
* `Oo7,28=r+MU}`: 6 pts (1 + 1 for case + 2 for numbers + 2 for symbols)

For this part, edit the `complexity_score` function in `rate_password.py`. As previously, 
you can find the tests for this in `test_rate_password.py`. This will likely be the most 
complicated part of the problem, do not hesitate to call for help.

## 4. Complete evaluation

Now that we have all the components, we can finally make a function that judges passwords!

The total score of a password is calculated as follows:
* If the password is common, it immediately gets 0 points
* Otherwise, calculate its score as the "Length score" multiplied by the "Complexity score"

The evaluation then returns an evaluation based of that score:
* score < 10 pts: _unacceptable_
* 10 pts ≤ score < 25 pts: _weak_
* 25 pts ≤ score < 50 pts: _ok_
* score ≥ 50 pts: _strong_

For this part, edit the `rate_password` function in `rate_password.py`.

## Bonus work

If the above was relatively easy for you, one last possible improvement is to check for 
proximity to common passwords. This involves modifying the `is_common` rule so that a 
password is also considered common if:
* it has a case-insensitive match in the list,
* removing any single character from the password makes it match a known common password,
* it's one "[l33t speak](https://simple.wikipedia.org/wiki/Leet)" substitution away 
  from any known common password.

There are no tests for this, but you are welcome to write your own!

# Resources

* _Measuring Password Strength: An Empirical Analysis_. 
  Matteo Dell'Amico, Pietro Michiardi, Yves Roudier
  https://arxiv.org/pdf/0907.3402.pdf

* _Password Cracking_. Computerphile
  https://youtu.be/7U-RbOKanYs

* OWASP's SecLists
  https://github.com/danielmiessler/SecLists
  https://www.owasp.org/index.php/OWASP_SecLists_Project

