
name = 'Abdullah'  #str use "/'
age = 10        #int
fruits = ['Orange', 'Apple', 'Banana'] #list aka arrays in other languages

print(name + " " + "is" + " " + str(age) + " and likes" + " " + fruits[2] + "s")






food = "pear"
foods = ['pie', 'fish', 'pizza', 'pasta']
number = 100
numbers = [10, 11, 12]

for number in numbers: #iteration
    print(number)

for char in food:      #iteration
    print(char)

'''
for i in 3:
    print (i)

PR#oduces error as int are not iteratble

instead use range function
'''    
for i in range(3):
    print(i)

if len(food) > 3:
    print(food + " " +"is nice")
else:
    print(food + " " + "is a very short spelt food")
    
