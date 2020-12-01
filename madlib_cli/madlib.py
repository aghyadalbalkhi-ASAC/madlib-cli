import re

def welc_msg(msg):
    print(msg)



def read_File(file_path):
    reader = open(file_path,'r')
    content = reader.read()
    reader.close()
    # rawContent = re.sub('\{(.*?)\}', '{}', content)
    # print(rawContent)
    # print(reader.closed)
    return content



def user_input(content):

    listOfQuestion =re.findall("\{(.*?)\}", content)
    answers=[]

    for question in listOfQuestion:
        answer=input('Please Enter a  '+ question +' :')
        answers.append(answer)
    return answers

    
def merge_content(content,answers):
    rawContent = raw_Content(content)
    gamerText=rawContent.format(answers[0],answers[1],answers[2],answers[3],answers[4],answers[5],answers[6],answers[7],answers[8],answers[9],answers[10],answers[11],answers[12],answers[13],answers[14],answers[15],answers[16],answers[17],answers[18],answers[19],answers[20])
    return gamerText

def create_file(content):
    with open('assets/GameResult.txt','w') as writer:
        writer.write(content)

def raw_Content(content):
    return re.sub('\{(.*?)\}', '{}', content)


"""
The Main Method where its control the whole function in this lab 
"""

if __name__ == "__main__":

    # Welcome msg appear to the user and this msg can be changed 
    msg = 'Welcome to Madlib Game ^-8'
    welc_msg(msg)

    # Read a specific file through funcation by passing the path to it

    file_path="assets/Game.txt"
    content = read_File(file_path)
    print(content)

    #Take The Input from the user 
    answers=user_input(content)
    gamerText=merge_content(content,answers)
    create_file(gamerText)

