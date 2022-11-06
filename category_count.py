import string
from os.path import exists

user_filename = "dat_exp2.txt"
file_exists = exists(user_filename)
if file_exists == True:      
    with open(user_filename,"r", encoding = 'utf8') as text_file:
        user_data = text_file.readlines()
else:
    print("The file you typed does not exist in the directory. Please check the file name and try again.")
    exit()

def return_categ (lines_from_file):
    '''Returns a list of categories from a list by cutting out the first four character strings of each element.
Args:
    arg1 (list): A list containing a string for each line.    
Returns:
    list: returns a list that has the first 4 character strings of each element of the argument as its elements.
'''
    cat_from_data = []
    for data_line in lines_from_file:
        cat_from_data.append(data_line[0:4])
    return(cat_from_data)

categ_dka = return_categ(user_data)

categ_set = set(categ_dka)
categ_set_sorted = sorted(categ_set)
categ_count = len(categ_set)
categ_occurrence = []
for categ in categ_set:
    categ_occurrence.append(categ_dka.count(categ))
categ_set_list = []
for categ in categ_set:
    categ_set_list =  categ_set_list + [categ]
categ_dict = {categ_set_list[i]: categ_occurrence[i] for i in range(len(categ_set_list))}
print(categ_dict)

tuples_alphabetically = sorted(categ_dict.items())
file_name = input("The outcome will be saved in a text file. Please input a name for the text file: ")
if file_name == "" :
    print("You typed an empty string")
    exit()
with open(file_name + '.csv',"w") as results_file:
    results_file.write("--- FREQUENCY COUNT SORTED ALPHABETICALLY---" + "\n")
    for categ in tuples_alphabetically:
        results_file.write(str(categ[0]) + " : " + str(categ[1]) + "\n")
    results_file.write("\n")
