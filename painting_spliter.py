
# coding: utf-8

# ### Students: Anh Tu NGUYEN - Joseph MERHEB - Sita SHRESTHA

# In[26]:


class Reader:
    def __init__(self, input_file):
        self.input_file = input_file
        self.portrait_list = ''
        self.landscape_list = ''
        self.new_text = ''
        self.my_dict = {}
        self.sorted_dict = {}
        file = open(input_file, "r")
        lines = file.readlines()[1:]
        i = 0
        for line in lines:
            self.new_text += str(i) + ' ' + line
            i += 1
        file.close()
        
    def paint_split(self):
        for line in self.new_text.splitlines():
            pType = line.split(' ')[1]
            if (pType == 'P'):
                self.portrait_list += line + '\n'
            elif (pType == 'L'):
                self.landscape_list += line + '\n'
        result = self.landscape_list + self.portrait_list
        return result
    
    def portrait_combiner(self):
        p_list = self.portrait_list.splitlines()
        result = ''
        for line in self.landscape_list.splitlines():
            l_id = line.split(' ')[0]
            result += str(l_id) + ' '
            tags = line.split(' ')[3:]
            for tag in tags:
                if (tag == tags[-1]):
                    result += tag + '\n'
                else: result += tag + ' '
        for i in range(0, int(len(p_list)/2)):
            p1_id = p_list[i].split(' ')[0]
            p2_id = p_list[len(p_list)-1-i].split(' ')[0]
            p1_tags = p_list[i].split(' ')[3:]
            p2_tags = p_list[len(p_list)-1-i].split(' ')[3:]
            tag_list = list(set(p1_tags) | set(p2_tags))
            result += str(p1_id) + ',' + str(p2_id) + ' '
            for tag in tag_list:
                if (tag == tag_list[-1]):
                    result += tag + '\n'
                else: result += tag + ' '
        file = open("simple_file.txt", "w")
        file.write(result)
        file.close()
        
        self.read_file(result)
    
    #####################################
    # Compare FrameGlasses
    def compare_frameglasses(self, fg1, fg2):
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
    #####################################
    
    # Read the sorted file of FrameGlasses
    def read_file(self, my_txt):
        # For each line
        for line in my_txt.splitlines(): 
            # Remove line break
            line = line.replace("\n","") 
            
            # Get the ids from the start of the line
            fg_ids = line.split(" ", 1)[0].replace(","," ")

            # Get the tags as a list
            new_list = line.split(" ")
            fg_tags = new_list[1:]

            # Insert into dictionary the key and values
            self.my_dict[fg_ids] = fg_tags
        #print(self.my_dict)
        self.iterate_frameglasses()

    # Iterate over dictionary of frameglasses to calculate scores
    def iterate_frameglasses(self):
        while len(self.my_dict) > 0:
            i = 0

            # First key in the dictionary    
            k1 = list(self.my_dict)[0]

            # Values/List related to the first key
            fg1 = self.my_dict[k1]

            # Add the first key/value into a new dictionary, as starting point
            self.sorted_dict[k1] = fg1

            # Itirate over the dictionary starting from the third element
            i = 1
            score0 = 0
        
            for k in list(self.my_dict)[i:len(self.my_dict)]:
                i+=1

                # list/value related to each key in dictionary
                fg_new = self.my_dict[k]

                # score between list 1 and each new list
                score_new = self.compare_frameglasses(fg1,fg_new)
                # print("Score between 1 and: " + str(i) + ": " + str(score_new))        

                # if this new score is less than the one we got at first, then we keep
                if score_new > score0:
                    score0 = score_new
                    # Memorize the new lists and keys
                    k2 = k
                    fg2 = fg_new
            
            
            # print(" ")
            # print("----------------------")
            # print("Best Score is: " + str(score0))
            # print("Between: ")
            # print(fg1,fg2)
        
            if len(self.my_dict) == 1:
                self.sorted_dict[k1] = fg1
                if k1 in self.my_dict:
                    del self.my_dict[k1]
            else:
                self.sorted_dict[k2] = fg2            
                del self.my_dict[k1]
                if k2 in self.my_dict:     
                    del self.my_dict[k2]

            # print(" ")
            # print("----------------------")
            # print("Old List:")
            # print(my_dict)

            # print(" ")
            # print("----------------------")
            # print("New List:")
            # print(self.sorted_dict)


        # Write the new sorted dictionary into a text file
        # Remove the tags, keep the IDs, and 
        # Put the total number of lines at the begining of the text
        self.write_frameglasses()
    
    #####################################
    # Write frameglasses into a text file
    def write_frameglasses(self):
        # Number of frameglasses
        frameglasses_count = str(len(self.sorted_dict))
        f = open("output_" + self.input_file, "w")
        f.write(frameglasses_count)
        f.write('\n')
    
        for key in self.sorted_dict:        
            f.write(key)
            f.write('\n')
        f.close()

    #####################################


# In[29]:


import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    args = parser.parse_args()

    reader = Reader(args.input)
    reader.paint_split()
    reader.portrait_combiner()
    
if __name__ == "__main__":
    main()
    
# reader = Reader("10_computable_moments.txt")
# reader.paint_split()
# reader.portrait_combiner()

