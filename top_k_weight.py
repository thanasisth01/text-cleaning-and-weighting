# importing the needed libraries
import datetime
import pandas as pd
import math

# finding the weight of each word in the document it appears in and returning the
# k words who appear the most in the document
def find_weight_of_terms(unique_terms,all_terms,k):

    # sorting all the words the text has
    all_terms.sort()

    # list to store the term and the log frequency it has
    weights_list = []

    # for each term which appears in the text/document
    for term in unique_terms:

        # the index where the term first appears on sorted list all_terms
        my_index = all_terms.index(term)
        # the time the term occurs
        count=1
        # moving to the next term
        my_index = my_index+1
        # if it is the same, add to the count, else move to next term
        while my_index<len(all_terms) and all_terms[my_index]==term:
            count = count+1
            my_index = my_index+1
        # append to the weights_list the term and its log frequency
        weights_list.append([term,round(1+math.log(count,10),3)])     #log(number,base of log)

    # sorting the weights_list in descending order to get the most frequent words
    weights_list.sort(key=lambda weights_list:weights_list[1],reverse=True)

    # final_list: consists of the k terms and their log frequency
    final_list = []
    for i in range(0,k):
        final_list.append(weights_list[i])

    # returning the final_list
    return final_list
    

# 
def procedure(file_ids,file_texts):

    # final_list: consists of the file id and the top k terms with their log frequency
    final_list =[]

    # for printing purposes
    num_of_text=0

    # length of the files_texts list, for printing purposes
    files_length = len(file_texts)
    print("Total number of texts to be reviewed:",files_length,":\n")

    # for each text in the list of text files
    for text in file_texts:
        # for printing purposes, how much have been calculated from the list of texts
        if num_of_text==1000 or num_of_text==5000 or num_of_text==10000:
            print("Just crossed",num_of_text,"of files.")

        # my_list: list with every word in a text file
        my_list = text.split()

        # using sets to get its word 1 time
        my_set = set(my_list)

        # length of the set
        length = len(my_set)

        # choosing the k from the length of the unique words
        k = math.sqrt(length)
        # turning k into an integer
        k = int(k)

        # calling the function which returns a list with terms and their log frequency
        top_k_weight_list = find_weight_of_terms(my_set,my_list,k)

        # appending for its file, its name and its top k terms with their log frequency
        # to the final_list
        file_name = file_ids[num_of_text]
        final_list.append([file_name,top_k_weight_list])

        num_of_text = num_of_text+1

    # returning the final_lsit
    return final_list
        

# WHERE THE PROGRAM STARTS

# when the program starts
now = datetime.datetime.now()
print("Starting date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S\n"))

# reading the csv file
df = pd.read_csv("filtered_texts.csv")
print("Opening file: filtered_texts.csv\n")

# getting the length of the csv file
df_len=len(df)
print("The document file's length is:",df_len,"\n")

# lists with data from the csv file
file_ids = df.iloc[:,0]
file_texts = df.iloc[:,1]
print(file_ids,"\n")
print(file_texts,"\n")

# calling the function procedure to start the calculation of the weighting
data = procedure(file_ids,file_texts)

# new lists to which we enter the final data to easily enter them in the new csv file
files_id = []
top_k_terms_weight = []

for line in data:
    files_id.append(line[0])
    top_k_terms_weight.append(line[1])

# writing out to a csv file the results
dictionary = {'fileID':files_id, 'top_k_terms_weight':top_k_terms_weight }

new_df=pd.DataFrame(dictionary)
new_df.to_csv('top_k_data.csv',index=False)
print("The top k terms weight has been found for every file. There is a new file called: top_k_data.csv")

# when the program finishes
now = datetime.datetime.now()
print ("\nFinishing date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
