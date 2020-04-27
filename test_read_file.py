# Temporary file path
filepath = "simple_file.txt"

# Dictionary Containing the frameglasses
my_dict = {}



#################################
# Compare FrameGlasses
def compare_frameglasses(fg1, fg2):
    # Number of tags common to fg1 and fg2
    intOfList = list(set(fg1) & set(fg2))
    len3 = len(intOfList)

    # Number of tags in fg1 but not in fg2
    len1 = len(fg1) - len3

    # Number of tags in fg2 but not in fg1
    len2 = len(fg2) - len3
    
    # Temporary List
    tmpList = []
    tmpList.append(len1)
    tmpList.append(len2)
    tmpList.append(len3)
    tmpList.sort()

    # Return the local satisfaction score
    return(min(tmpList))
    #print(min(tmpList))




# Read the sorted file of FrameGlasses
def read_file(filepath):
    # Open the new sorted text file by (L) and (P)
    with open(filepath) as my_txt:        
        # For each line
        for line in my_txt: 
            # Remove line break
            line = line.replace("\n","") 
            
            # Get the ids from the start of the line
            fg_ids = line.split(" ", 1)[0].replace(","," ")

            # Get the tags as a list
            new_list = line.split(" ")
            fg_tags = new_list[1:]

            # Insert into dictionary the key and values
            my_dict[fg_ids] = fg_tags
    #print(my_dict)
    iterate_frameglasses()



# Iterate over dictionary of frameglasses to calculate scores
def iterate_frameglasses():
    i = 0
    for k1 in my_dict:
        i+=1
        for k2 in list(my_dict)[i:len(my_dict)]:
            fg1 = my_dict[k1]
            fg2 = my_dict[k2]
            scr1 = compare_frameglasses(fg1,fg2)
            print(scr1)




# Read the sorted file of FrameGlasses
read_file(filepath)






