def calculate_occurrences(string):
    result={}
    for letter in string:
        if letter in result:
            result[letter]+=1
            
        else:
            result[letter]=1

    return result    
def find_multiples(start,end):
    for i in range(start,end):
        if i % 3==0 and i % 5==0:
            print ("fizz buzz")
        
        elif i % 5==0:
            print ("buzz")
        elif i % 3==0:
            print ("fizz")
        else:
            print(i)

        
def check_vowels(word):
    vowels=['a','e','i','o','u']
    for i in word:
        if i in vowels:
            print(f"{i} is vowel")
        else:
            print(f"{i} is a consonant")

def reverse_sentence(sentence):
    return " ".join(sentence.split(" ")[::-1])

print(reverse_sentence("hello how are you")) 

def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

print(reverse_each_word("hello how are you")) 

def reverse_all(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)[::-1]

print(reverse_all("hello how are you"))


def check_numbers(numbers):
    squares={i:i*i for i in numbers}
    print(squares)
check_numbers([1,2,3,4])  

def map_dict(a):
    
    for key, values in a.items():
        print(f"{key}:{values}")
map_dict(a={1: 1, 2: 4, 3: 9, 4: 16})

def reverse(word):
    reversed=word[::-1]
    print(reversed)
reverse("hello")   


def reversed_sentence(words):
    words2=words.split(" ")
    
    return " ".join(words2)[::-1]
print(reversed_sentence("I can code"))


        

        
            
