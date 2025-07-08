# for punctuation purposes
import string
import os

# for stemming purposes
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# for time purposes
import datetime

import pandas as pd

# removes frequent words, punctuation symbols and turns capital letters to small
def remove_punct_and_freq_words(data):

    # the most frequent words based on wikipedia
    frequent_words = ["the","be","to","of","and","a","in","that","have","I",
                      "it","for","not","on","with","he","as","you","do","at",
                      "this","but","his","by","from","they","we","say","her",
                      "she","or","an","will","my","one","would","all","there",
                      "their","what","so","up","out","if","about","who","get",
                      "which","go","me","when","make","can","like","time","then",
                      "no","just","him","know","take","people","into","year",
                      "your","good","some","could","them","see","other","than",
                      "now","look","only","come","its","over","think","also","back",
                      "after","use","two","how","our","first","well","way","even"
                      "new","want","because","any","these","give","day","most","us",
                      "subject","keywords","re","i"]

    # removing the punctuations from the string with the data
    punct_data = data.translate(str.maketrans('','',string.punctuation))

    # transforming every word into lowercase from the string with the data
    lowercase_data = punct_data.lower()
    
    # stemming the words
    ps = PorterStemmer()
    words = word_tokenize(lowercase_data)

    # contains the words which are not frequent
    final_list = []
    
    # words: list with all the words in the lowercase_data string
    words = lowercase_data.split()

    # if a word exists in the frequent_words list, then don't add it in the final_list
    for word in words:
        if word not in frequent_words:
            final_list.append(word)

    # joining all the words who remained after removal
    final_product = " ".join(final_list)

    # returning the final product
    return final_product

# removes header trash, empty lines
def remove_header_trash(data):

    # the punctuation symbols which must be removed
    punct_symbols = string.punctuation

    # from the header we don't keep the receiver etc, expect from this info
    header_keep = ["Subject:","Keywords:"]

    # we split the text file line by line to edit it
    data_line_by_line = data.splitlines()

    # lines that must be removed from the text
    remove_list = []

    # to keep track of the line we edit
    count=0
    for aLine in data_line_by_line:

        # splitting the lines in a list of words
        words = aLine.split()

        # if our line has words
        if len(words)!=0:
            
            # if the first word is not in the needed header info and has ":" next to it
            if words[0] not in header_keep and words[0][-1]==":":
                 # remove it from the text
                 remove_list.append(count)
            # if the line starts with a punctuation symbol
            elif punct_symbols.find(words[0][0])>=0:
                remove_list.append(count)
        # the empty line is being removed
        else:
           remove_list.append(count)
        count = count+1

    # the lines we want to keep from the text file
    final_data=[]

    # length of lines
    my_length = len(data_line_by_line)

    # for every line
    for i in range(0,my_length):

        # if the line is not in the remove list
        if i not in remove_list:
            # add the line to the final lines 
            final_data.append(data_line_by_line[i])

    # joining all the needed lines together
    final_product = " ".join(final_data)

    # returning the final product (filtered text file)
    return final_product


# WHERE THE PROGRAM STARTS

# time the program starts
now = datetime.datetime.now()
print("Starting date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S\n"))

# the path where the folder exists
main_path = "./Destination_FolderName/20news-bydate-train"

# getting the names of the sub folders of the main folder
filelist=os.listdir(main_path)

# finding the paths of the subfolders
sub_paths = []
for x in filelist:
    sub_paths.append(main_path+"/"+x)

# printing the nu,ber of subpaths
print("Number of sub paths:",len(sub_paths),"\n")

# the final files after header trash, punctuation and frequent words removal 
final_filtered_files = []

# printing the number of subpath we are on
line=1

# for each subfolder
for aSubPath in sub_paths:

    # getting the names of the files, in each sub folder
    files_list = os.listdir(aSubPath)

    # printing the sub folder the program is now
    print("Now in sub path",line,":",aSubPath)

    # for each file in the current subfolder
    for aFile in files_list:

        # getting the path of the file, to open it
        file = open(aSubPath+"/"+aFile,"r",errors="ignore")

        # reading the file
        data = file.read()

        # calling the function to remove irrelevant lines from the header
        new_data = remove_header_trash(data)
        
        # calling the function to remove punctuations and frequent words
        final = remove_punct_and_freq_words(new_data)

        # appending the file name and the filtered text file
        final_filtered_files.append([aFile,final])
        
        # closing the file
        file.close()

    line = line+1

# for comfort to enter the data to csv file
files_name = []
filtered_files = []

# appending to files_name and filtered_files, each file name and file text respectivelly
for data in final_filtered_files:
    files_name.append(data[0])
    filtered_files.append(data[1])

# entering the filtered files and names to a new csv
dictionary = {'fileID':files_name, 'filteredTexts':filtered_files}

new_df=pd.DataFrame(dictionary)
new_df.to_csv('filtered_texts.csv',index=False)
print("\nPrefiltering has ended. There is a new file called: filtered_texts.csv")

# time the program finishes
now = datetime.datetime.now()
print ("\nFinishing date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
