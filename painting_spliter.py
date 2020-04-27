
# coding: utf-8

# In[102]:


class Reader:
    def __init__(self, input_file):
        self.portrait_list = '';
        self.landscape_list = '';
        self.new_text = '';
        file = open(input_file, "r");
        lines = file.readlines()[1:];
        i = 0;
        for line in lines:
            self.new_text += str(i) + ' ' + line;
            i += 1;
        file.close()
        
    def paint_split(self):
        for line in self.new_text.splitlines():
            pType = line.split(' ')[1];
            if (pType == 'P'):
                self.portrait_list += line + '\n';
            elif (pType == 'L'):
                self.landscape_list += line + '\n';
        result = self.landscape_list + self.portrait_list;
        return result;
    
    def portrait_combiner(self):
        p_list = self.portrait_list.splitlines();
        print(int(len(p_list)/2));
        result = '';
        for i in range(0, int(len(p_list)/2)):
            p1_id = p_list[i].split(' ')[0];
            p2_id = p_list[len(p_list)-1-i].split(' ')[0];
            p1_tags = p_list[i].split(' ')[3:];
            p2_tags = p_list[len(p_list)-1-i].split(' ')[3:];
            tag_list = list(set(p1_tags) | set(p2_tags));
            result += str(p1_id) + ',' + str(p2_id) + ' ';
            for tag in tag_list:
                if (tag == tag_list[-1]):
                    result += tag + '\n'
                else: result += tag + ' ';
        print(result);


# In[103]:


import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    args = parser.parse_args()

    reader = Reader(args.input)
    reader.paint_split();
    reader.portrait_combiner();
    
if __name__ == "__main__":
    main()
    
# reader = Reader("../10_computable_moments.txt");
# reader.paint_split();
# print(reader.portrait_list);
# reader.portrait_combiner();

