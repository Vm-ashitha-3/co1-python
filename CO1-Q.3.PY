print("LIST COMPREHENSIONS \n")
integers = [5, 10, 6, 8, 3]
positive = [i for i in integers if i > 0]
print(positive)

num = int(input("Enter your number: "))
print("The list of squares:")
new_list = [i**2 for i in range(1, num+1)]
print(new_list)

vowels = ['a','e','i','o','u']
word = input("Enter the word: ")
word_list = list(word)
vowels_list = [char for char in word_list if char in vowels]
print(vowels_list)

new_word = input("Enter the word: ")
new_wordlist = list(new_word)
ord_list = [ord(word) for word in new_wordlist]
print(ord_list)
