print("welcome you will have fun time in this game :)")

def read_template(path):
    
    with open(path,'r') as file:
     content = file.read().strip()
     #strip return acopy of string
     print(content)
     return content
     
import re
#re module, we can start using regular expressions and search
def parse_template(txt, isTrue=True):
    pattern = r"{(.*?)}"
    #  r means the string will be treated as raw string. 
    part_of_output=re.findall(pattern,txt)
    # findall() module is used to search for “all” occurrences that match a given pattern.
    print(f'answer these {len(part_of_output)} questions ')
    #get the inputs from the user
    
    i=1
    user_input=[]
    if(isTrue == True):
        for item in part_of_output:
            input_user=input(f" question number {i} plaese suggest {item} '\n' your answer is:")
            user_input.append(input_user)
            # append like push in js 
            i=i+1
        output=[user_input,part_of_output]
        return output
    else:
        return part_of_output

def merge(input, placeholders, txt):
    i=0
    for item in input:
        txt=txt.replace(placeholders[i],item,1)
        #replace(oldvalue, newvalue, count)
        #count is optional to add
        i=1+i

    txt=txt.replace("{","")
    massage_content=txt.replace("}" ,"")
    file="(/assets/ms.txt)".strip()
    with open(file,'w') as message:
        message.write(massage_content)

    print(f"""
    ********
     your paraghraph
     ********
     {massage_content}
     """)
    return massage_content

if __name__ == "__main__":
    content = read_template('assets/madlib.txt')
    items = parse_template(content)
    to_be_replaced_with = items[0]
    to_be_replaced = items[1] 
    merge(to_be_replaced_with, to_be_replaced, content)
