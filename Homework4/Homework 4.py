#2.1
donuts = list(range(21))
print(donuts)
# At first i typed in list[0,21] however this did not work and so i added the range to define my list

#2.2
def square_list(numbers):
    return [num **2 for num in numbers]
donuts = list(range(21))
donuts_squared = square_list(donuts)
print(donuts_squared)

#2.3
def first_15_elements(numbers):
    return numbers[:15]
first_15 = first_15_elements(donuts_squared)
print(first_15)
#The error I ran into was that first_15_elements was not defined and so I defined it to return the first 15 numbers

#2.4
def every_fifth_element(numbers):
    return numbers[4::5]
every_5th_donut = every_fifth_element(donuts_squared)
print(every_5th_donut)
#I worte [::5] and this was starting at 0 but we want to start at 16 which would be [4::5]

#2.5
def every_third_element(numbers):
    return numbers[3:][::-3]
donuts_every_three = every_third_element(donuts_squared)
print(donuts_every_three)
# At first I wrote [-3:][::-3] but this was only printing 400 so i changed it to [3:] and that solved it

#3.1
def create_2d_list():
    return [[col + row * 5 + 1 for col in range(5)] for row in range(5)]
matrix = create_2d_list()
for row in matrix:
    print(row)

#3.2
def replace_multiples_of_3(matrix):
    return [["?" if num % 3 == 0 else num for num in row] for row in matrix]
modified_matrix = replace_multiples_of_3(matrix)
for row in modified_matrix:
    print(row)
#The error I got was that I forgot to defined the modified_matrix so I defined it to = the replace_multiples_of_3 

#3.3
def sum_non_question_mark(matrix):
    return sum(num for row in matrix for num in row if num != "?")
total_sum = sum_non_question_mark(modified_matrix)
print(total_sum)