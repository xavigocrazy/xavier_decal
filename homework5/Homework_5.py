#1.1 You have been plopped into this directory system. What command will tell you what your working directory is?  
    #pwd will tell you what working directory 

#1.2 The command tells you ∼/python decal/judy decal. What command with list all the files in your current working directory?
    #ls will list all the files in your working directory

#1.3 Brianna just sent out an announcement that there was a typo on homework.py. So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?
    # cd brianna_repo
    # git pull origin main

#1.4 How would you move this new homework.py to your personal repository homework directory?
    # within brianna_repo
    # cp homwork.py
    # mv homework.py ~/python_decal/judy_decal/homework
    # git add homework.py
    # git commit -m "Moved homework.py" 
    # git push origin master

#1.5 You want to see the contents of the homework.py in your terminal from our personal repository. What command(s) will let you do this?
    # cat homework.py

#1.6 You want to edit the contents of the homework.py in your terminal from your personal repository. What command will let you do this?
    # nano homework.py

#1.7 You have finished the homework. What commands will allow you to save the changes and push from your local repository to your remote repository?
    # git add homework.py
    # git commit -m "Moved edited homework.py" 
    # git push origin master

#1.8 git pull origin main, if you run into any conflicts you git add then git commit, then finally push to origin master

#9 cd /~/recent

#2 HW3 Review

#2.1
def CheckDataType(value):
    return type(value).__name__
print(CheckDataType(3.14))

#2.2
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
print(4)
print(5)

#3
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))


#4.1
def duplicateList(lst):
    duplicated = []
    for item in lst:
        duplicated.append(item)
        duplicated.append(item)
    return duplicated
print(duplicateList(['a', 'b', 'c']))

#4.2
def square(num):
    return num * num
print(square(6))