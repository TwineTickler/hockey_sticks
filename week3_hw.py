# **What is the bash/terminal command for cloning a repository to your local machine?**

'''
git clone "reponame"

'''

# **What is the bash/terminal command for updating the repository on your local machine from the remote repository?**

'''
git pull

'''

# **What are the bash/terminal commands to commit your local changes and push them to the remote repository?**

'''
git status
git add *
git commit -m "comment"
git push

'''
# 
# **What bash/terminal command will inform you of what files have changed and what files are being tracked by git?**

'''
git status

'''

# **What bash/terminal command creates a new branch within a repository?**

'''
git branch
?

'''

# **What bash/terminal command switches to a different branch within a repo?**

'''
git checkout

'''

# <br><br><br><br><br><br>
# Bash Commands

# **How do you write the full
#   pathname of the current working directory to the terminal?**

'''
pwd

'''

# **How do you list the files in the current working
#   directory**

'''
ls -lh

'''

# **How do you go up one directory?**

'''
cd ..

'''

# **How do you change directories to the home directory in your operating system?**

'''
cd ~

'''

# **How do you list the files in a subdirectory?**

'''
ls subdir

'''

# **How do you create three text files in one command in the terminal?**

'''
touch file1 file2 file3

'''

# **How do you remove a file?**

'''
rm file

'''

# **How do you create a directory?**

'''
mkdir dir

'''

# **How do you remove a directory and recursively delete all of its contents?**

'''
rm -r dir

'''

# **How do you rename a file in bash?**

'''
mv file newfilename

'''

# **How do you copy a file in bash?**

'''
cp file filecopy

'''

# **How do you copy a directory and all its contents in bash?**

'''
cp -r dir dircopy

'''

# <br><br><br><br><br><br>
# # Python Coding
# * intended to be in order of increasing difficulty

# <br><br><br>
# **Create a multi-line comment in Python?**


'''python
'''
'''
muliline comment
here
'''
'''


'''

# <br><br><br>
# **What are the built-in immutable data types in Python?**

'''
Immutable
bool
int
float
tuple (1, 2, 3, 4, 5) - ordered
str

Mutable:
list [1, 2, 3, 4, 5] - ordered
set {1, 2, 3, 4, 5} - unordered
dict {'key':'value','key2':'value2'} - unordered

'''

# <br><br><br>
# **Write a function named `build_type_tuple` that takes an integer or float as an argument and returns a 
# tuple containing the argument converted to `int`, `float`, `bool`, `str`, `complex` and a unicode string (use `chr()`)**


'''python



'''

# def build_type_tuple(x):
#     return (int(x), float(x), bool(x), str(x), complex(x), chr(x))

# print(build_type_tuple(6))


# <br><br><br>
# **Write a function called `do_some_math` that takes 5 numbers as arguments and performs these operations:**<br>
# The sum of num1 and num2, subtracted from the product of num3 and num5, all floor divided by num4


# def do_some_math(n1, n2, n3, n4, n5):
#     return ((n3 * n5) - (n1 + n2)) / n4

# print(do_some_math(1, 5, 3.665453, 2, -6.42))

'''python
'''



# <br><br><br>
# **Write a function named `remainder_after_expansion` that takes three arguments: `x`, `exponent`, and `divisor`. 
# Return the remainder from dividing `x` raised to the `exponent` by the `divisor`.**




'''python
def remainder_after_expansion(x, exponent, divisor):
    return (x ** exponent) % divisor

print(remainder_after_expansion(5, 3, 7))

'''

# <br><br><br>
# **Write a function named `id_of_product` that returns the id of the product of arguments `x` and `y`**


'''python

def id_of_product(x, y):
    return id(x * y)

print(id_of_product(5, 6))
'''

# <br><br><br>
# **Write a function called `divisible_by_low_primes` that takes a number as input from the user, 
# and returns `True` if that number is divisible by 2, 3, 5, or 7, or `False` if it is divisible by none of those.**

def divisible_by_low_primes(x):
    if x == 0:
        return False
    elif (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or (x % 7 == 0):
        return True
    else:
        return False

def func2(x):
    arr = [2, 3, 5, 7]
    if x == 0:
        return False
    for n in arr:
        if x % n == 0:
            return True
    return False

# print(divisible_by_low_primes(int(input("Enter a number: "))))
# print(func2(int(input("Enter a number: "))))

'''python
'''

# <br><br><br>
# **Write a function called `sum_of_divisible_by_n` that takes three arguments, `low`, `high` and `n`. 
# Sum the numbers in the range from `low` to `high` inclusive that are divisible by `n`**

def sum_of_divisible_by_n(low, high, n):
    result = 0
    for x in range(low, high+1):
        if x % n == 0:
            result += x
    return result



# print(sum_of_divisible_by_n(4, 20, 6))

'''python
'''

# <br><br><br>
# **Write a function called `get_mode` that takes a list of numbers as an argument and returns the most frequently occurring number in that list. Assume that there will be a definitive most frequently occurring number.**


'''python




'''

# <br><br><br>
# **Write a function called `verify_string_length` that takes two arguments, a `string` and a `min_length`. Return `True` if `string` meets the `min_length` requirement, otherwise `False`**


'''python




'''

# <br><br><br>
# **Write a function called `repeating_num_series` that takes a list of numbers `series_of_numbers` and an integer called `num_times` as an argument. The function should return  a single list containing that series repeated `num_times`**


'''python




'''

# <br><br><br>
# **Write a function called `get_first_and_last` that takes a list as an argument and returns a tuple containing the first and last elements of that list. In the case of an argument of `length==1`, return a tuple with a single value. If the argument is an empty list, return an empty tuple.**


'''python




'''

# <br><br><br>
# **Write a function called `nth_element` that takes a list and `nth` as arguments. Return a list containing every `nth` element of the input list, starting with the first element.**


'''python




'''

# <br><br><br>
# **Write a function `central_tendencies` that returns the mean, median and mode of a list of numbers**
# * Print the output from the function:
#     * expected result: `(5.933333333333334, 6.0, 1.0)`


'''python
def central_tendencies(num_list):
    '''
    # Returns the mean, median and mode
    # of a list of numbers
    
    # PARAMETERS
    # ----------
    # num_list: list of ints
        
    # RETURNS
    # -------
    # central_vals: tuple of len=3
    #     mean: float
    #         the arithmetic mean of the num_list

    #     median: float
    #         the median value in the num_list

    #     mode: float
    #         the most common value in the num_list
    #         assume only one mode in the distribution
        
    # EXAMPLE
    # -------
'''
    nums = [2, 2, 3, 4, 5]
    '''
    # >>> central_tendencies(nums)
    # (3.2, 3.0, 2.0)
'''
    
    
    



######## Test your Code Below ###########
nums = [1,1,1,2,3,4,5,6,7,8,9,9,10,11,12]
print(central_tendencies(nums))
'''

# <br><br><br>
# **Write a function `distr_spread()` that returns the range, variance, and standard deviation of a list of numbers**
# * Hints: 
#     * You can call your previous function 
#     * You may want to import the [`math` module](https://docs.python.org/3/library/math.html)
# * Print the output from the function:
#     * expected result: `(11, 14.638095238095238, 3.8259763770958175)`


'''python
import math

def distr_spread(num_list):
    '''
    # Returns the range, sample variance, and 
    # sample standard deviation
    
    # PARAMETERS
    # ----------
    # num_list: list of ints
        
    # RETURNS
    # -------
    # spread_vals: tuple of len=3
    #     samp_range: float
    #         the span of values in the data

    #     samp_variance: float
    #         the median value in the num_list

    #     samp_std: float
    #         the most common value in the num_list
    #         assume only one mode in the distribution
        
    # EXAMPLE
    # -------
'''
    nums = [2, 2, 3, 4, 5]
    '''
    # >>> distr_spread(nums)
    # (3, 1.7, 1.3038404810405297)
'''
    
    
    
    

######## Test your Code Below ###########
nums = [1,1,1,2,3,4,5,6,7,8,9,9,10,11,12]
print(distr_spread(nums))
'''

# <br><br><br>
# **Write the `greatest_common_divisor` function, which takes two integerst and returns the largest number that divides both numbers.**


'''python




'''

# <br><br><br>
# **Write the `get_primes_dig_sum_to_n` function, that takes `list_of_ints` and `dig_sum` as arguments. The function should return all numbers in the input list that are primes with recursive digit sums equal to `dig_sum`**


'''python





'''

# <br><br><br>
# **Write the classic "Fizz Buzz" coding challenge. Define a function `fizz_buzz` that takes `low` and `high` as arguments. The function should run through all the numbers in the range from `low` to `high`, `print()` 'Fizz Buzz' when the number is evenly divisible by both 5 and 3, "Fizz" when the number is only divisible by 3, and "Buzz" when the number is only divisible by 5.**


'''python




'''

# <br><br><br>
# **Write a function `lower_first_rest_upper()` that takes a string as input and returns a string where the first letter of each word is lowercase, and the rest of the word is uppercase**
# * You will likely to use `string` methods:
#     * `string.lower()`
#     * `string.upper()`
# * Print the result of your function call
# * expected result: `fAVARTIA pERITA iS a sPECIES oF sEA sNAIL`


'''python
string_to_mod = 'Favartia perita is a species of sea snail'

#########  Complete the Code Below ###########






######## Test your Code Below ###########
print(lower_first_rest_upper(string_to_mod))
'''

# <br><br><br>
# **Write a function called `add_and_repeat_strings` that takes two strings and an integer `repeats` as arguments. The function should return those two strings, concatenated and separated by a space, and repeated `repeats` times.**


'''python



'''

# <br><br><br>
# **Write a function called `make_good_filename` that takes a string as input. Remove all non-alphanumeric characters. Separate all words in the string with an underscore `_`. If the first character in the string is a number, remove it. Make sure your filename is all lowercase.**


'''python




'''

# <br><br><br>
# **Write a function called `make_capital_camelcase` that takes a string as an argument, and returns that string in "capital camelcase" form. Remove punctuation and any non-alphanumeric characters. Don't allow the first character of the returned string to be a number.**
# * ex. "I am a string" -> "IAmAString"


'''python





'''

# <br><br><br>
# **Complete the `poisson_pmf` function:**
# * For reference, the Probability Mass Function (PMF) for the Poisson Distribution can be represented as:
# * $P(X=k) = e^{-\lambda} \cdot \frac{\lambda^k}{k!}$
# * note that the Python `math` module contains the `exp()` function to compute $e^x$


'''python




'''

# <br><br><br>
# **Write the `poisson_dict` function in order to gain more insight into the Poisson distribution. Return a dictionary, where the keys represent the values of k for a given parameter `lmbda`. Include a `low` and `high` parameter as well, for the range of poisson values in which we are interested.**


'''python




'''

# <br><br><br>
# **Write a function `sigmoid_logistic()` that returns $f(x)$ for the sigmoid/logistic function $f(x)=\frac{1}{1+e^{-x}}$,  as well as 0 or 1 based on the setting of a threshold**
# * The Logistic Function will come up a lot in terms of Logistic Regression and neural nets.
# * You can get Euler's number $e$ from the `math` module.
# * Print the output from the function:
#     * expected result: `(0.7310585786300049, 1)`


'''python
def sigmoid_logistic(x, threshold):
    '''
    # Returns the output of the sigmoid logistic
    # function and 0 or 1 based on a given threshold.
    
    # PARAMETERS
    # ----------
    # x: number
    #     Input to the sigmoid/logistic function
    
    # threshold: float
    #     value between 0 and 1 that dictates
    #     threshold
        
    # RETURNS
    # -------
    # tuple:
    #     f_of_x: float
    #         Representing the output of the 
    #         sigmoid function
            
    #     threshed: int
    #         0 or 1, based on the given
    #         result of f_of_x being above
    #         or below the threshold
        
    # EXAMPLE
    # -------
'''
    x = -9
    threshold = 0.4
    '''
    # >>> sigmoid_logistic(x, threshold)
    # (0.00012339457598623172, 0)
'''
   



######## Test your Code Below ###########
x = 1
threshold = 0.73
print(sigmoid_logistic(x, threshold))
'''

# <br><br><br>
# **Write a function called `sigmoid_values_in_range` that  utilizes the `sigmoid_logistic` function. `sigmoid_values_in_range` takes three float arguments, `low`, `high`, and `step`, representing the values of `x` in the sigmoid function above. Return a dictionary where the keys are the values of x, and the values are the calculations returned from the sigmoid function.**


'''python




'''

# <br><br><br>
# **Write a function called `sigmoid_distr_by_thresh` that utilizes the `sigmoid_logistic` function. `sigmoid_distr_by_thresh` takes three float arguments, `low`, `high`, and `step`, representing the values of `x` in the sigmoid function, as well as `threshold`, to be passed into the call to `sigmoid_logistic`. This function should return a dictionary with two keys, `>{threshold}` and `<={threshold}`, where the values are the results in those respective ranges**


'''python




'''

# <br><br><br>
# **Write a function called `show_nice_distro` that takes a dictionary as an argument. Assume that the keys in this dictionary represent the value of a random draw, and the values are the counts of occurrences of that value. The printed display should look something like:**

'''
0: *
1: ****
2: ******
3: ****
4: **
5: *
'''

# **Try to use this function to display the results of the distributions you write from here on. You will want to reduce the number of asterisks when they exceed a length. Play around with it to make it look nice.**


'''python




'''

# <br><br><br>
# **Write a function titled `remove_stopwords` that takes a string as an argument. Return a dictionary, where the keys are words, and the value is the count of those words in the document. Lowercase your keys and do not include numbers or punctuation. Do not include stopwords in your distribution.  A stopword can be considered a very common word in a language. These words are often unhelpful when comparing similarity between two documents. Use the defined stopwords below.**

# * use these stopwords: 
'''
['the', 'and', 'of', 'it', 'he','she',
 'it','was', 'i', 'me', 'my', 'myself', 
 'we', 'our', 'us', 'your', 'him', 
 'what', 'which', 'to', 'from', 'where',
 'a', 'in', 'on', 'be', 'its']
 '''


'''python
paragraph = '''
# From Safety To Where was a post-punk 
# trio from Columbia, South Carolina, USA, known for 
# its jarring guitar/bass interplay and frantic, 
# screaming vocals. The Joy Division reference in 
# the band's name was only slightly evident in its 
# music, which evolved from terse, minimalist, 
# post-hardcore into dark, melodic post-punk. 
# In 2002, the band signed to Radical Records in 
# New York City, which released their most notable 
# album, Irreversible Trend. The album ranked in 
# the Top 75 of the College Music Journal Top 200 
# albums chart that July, spawning the college radio 
# hit, "Only Now". Propelled by the appearance of 
# its ethereal instrumental, "Monument" 
# (from Irreversible Trend) on MTV's The Real 
# World and several tours of the East Coast and 
# Midwest in 2002, the band recorded its final 
# album, Interference, over the course of the next 
# two years. However, the band succumbed to a souring 
# internal relationship before it could be released.'''

stopwords = ['the', 'and', 'of', 'it', 'he','she',
             'it','was', 'i', 'me', 'my', 'myself', 
             'we', 'our', 'us', 'your', 'him', 
             'what', 'which', 'to', 'from', 'where',
             'a', 'in', 'on', 'be', 'its']





# <br><br><br>
# **Write a function called `trinary_sums_distribution` that takes no arguments. The length of the trinary should be 4 "trits". Your function should return a dictionary where the keys represent sums of the the "trits", and the values represent the counts of occurrences of those sums**


'''python





'''

# <br><br><br>
# **Write a function called `binary_trial` that generates a list of random binary of length `n`. Write another function called `binary_trial_sampler` that calls `binary_trial` `num_samples` times and returns a dictionary where the keys are the sums of 1's in the sampled binary lists, and the values are counts of the occurrences of those sums. Parameters to `binary_trial_sampler` should be `num_samples` and `n`, the length of the binary lists.**


'''python




'''

# <br><br><br>
# **Write a function `word_permutations_dict()` that takes a string as input and returns a dictionary where the keys are every word in the input string, and the values are lists containing strings of every permutation of letters of that word**
# * **DO NOT use an import of a permutations method here, implement an algorithm!**
#     * You will likely want to use [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm) to generate your permutations, although there are multiple other algorithms to accomplish this task.
# * You may want to use a helper function
# * When you test your function, it will be more helpful to print the lengths of the lists for each key in the dictionary instead of printing the lists themselves.
#     * expected result:
#            moths : 120 permutations
#            are : 6 permutations
#            insect : 720 permutations
#            teddy : 60 permutations
#            bears : 120 permutations
#     * Hint:
#         * What happens if you have repeated letters in a word?


'''python
test_string = 'moths are insect teddy bears'

#########  Complete your Function Code Below ###########







######## Test your Code Below ###########
perms_dict = word_permutations_dict(test_string)
for k,v in perms_dict.items():
    print('{} : {} permutations'.format(k, len(v)))
'''


'''python

'''
