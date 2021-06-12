print("welcome you will have fun time in this game :)")

def read_template(path):
    
    """
    this function that takes in a path to text file and
    returns a stripped string of the file contents.

    """

    with open(path,'r') as file:
     content = file.read().strip()
     #strip return acopy of string
     print(content)
    #  return content
    try:
        file=open(path)
        content=file.read().strip()
        file.close()
    except FileNotFoundError:
        if content == 'no such file':
            print('File Not Found Error please try again')
    return content

     
import re
#re module, we can start using regular expressions and search a pattern
#boolean value should start with is to make it true
def parse_template(txt, isTrue=True):

    """
     this function that takes in a template string and boolean value
     it will ask the user the num of question and to input value
     and returns a string with language parts 
     removed and a separate list of those language parts.

    """
    pattern = r"{(.*?)}"
    #  r means the string will be treated as raw string. 
    part_of_output=re.findall(pattern,txt)
    # findall() module is used to search for “all” occurrences that match a given pattern.
    #the lenght of list equal to num of Q.
    print(f'answer these {len(part_of_output)} questions ')
    #get the inputs from the user
    
    i=1
    user_input=[]
    if(isTrue == True):
        for item in part_of_output:
            input_user=input(f" question number {i} plaese suggest {item} '\n' your answer is :) ")
            user_input.append(input_user)
            # append like push in js 
            i=i+1
        output=[user_input,part_of_output]
        return output
    else:
        return part_of_output

def merge(input, placeholders, txt):

    """

    function that takes in a “bare” template and a list of user entered language parts
    and returns a string with the language parts inserted into the template.

    """
    i=0
    for item in input:
        txt=txt.replace(placeholders[i],item,1)
        #replace(oldvalue, newvalue, count)
        #count is optional to add
        i=1+i

    txt=txt.replace("{","")
    massage_content=txt.replace("}" ,"")
    file="assets/ms.txt"
    content=file.strip()
    with open(content,'w') as message:
        message.write(massage_content)

    print(f"""
    *******
     your paraghraph
    *******
     {massage_content}
     """)
    return massage_content

##dunder what inside it will not imort it work just when i run this page in commad line
if __name__ == "__main__":
    txt = read_template('assets/madlib.txt')
    item = parse_template(txt)
    first_parameter = item[0]
    second_parameter = item[1] 
    merge(first_parameter, second_parameter, txt)
