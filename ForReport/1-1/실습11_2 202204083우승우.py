list_fruit = ['apple', 'banana', 'tomato']
list_animal = ['bear', 'elephant', 'monkey']
list_instrument = ['guitar', 'piano', 'harmonica']

def total_length_of_words(word_list):
    sum = 0
    for word in word_list:
        sum += len(word)
    return sum
    

print(total_length_of_words(list_fruit))
print(total_length_of_words(list_animal))
print(total_length_of_words(list_instrument))