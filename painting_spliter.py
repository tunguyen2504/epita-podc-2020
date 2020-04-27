
# coding: utf-8

# In[121]:


class Reader:
    def __init__(self, input_file):
        file = open(input_file, "r");
        lines = file.readlines()[1:];
        i = 0;
        new_text = '';
        for line in lines:
            new_text += str(i) + ' ' + line;
            i += 1;
        file.close()
        portrait_list = '';
        landscape_list = '';
        for line in new_text.splitlines():
            pType = line.split(' ')[1];
            if (pType == 'P'):
                portrait_list += line + '\n';
            elif (pType == 'L'):
                landscape_list += line + '\n';
        full_list = landscape_list + portrait_list;
        print(full_list);
        output_file = input_file + "_reorder.txt";
        new_file = open(output_file, "w");
        new_file.write(full_list);
        new_file.close();
#         print(landscape)
#         print(outtext)
# outfile = open("3_2000.txt","w")
# outfile.writelines(outtext)
# outfile.close()


# In[122]:


import argparse
def main():
    parser = argparse.ArgumentParser(description="Script to check the score")
    parser.add_argument("input", type=str, help="The path to the input file")

    args = parser.parse_args()

    read = Reader(args.input)
    
if __name__ == "__main__":
    main()	
	
# read = Reader("../10_computable_moments.txt")

