
def fileopen(data, target):
 
    with open(data,'r',encoding='cp949') as file:
    
        text = file.read()
        
        if target in text   :
        
            flag = True
            
            splitdata = text.split()
            
        else :
        
            flag = False
            
            splitdata = None
 
    return flag, splitdata

def count_word(data,TargetText):
 
    count = 0
    
    for i in data :
    
        if TargetText in i :
        
            count += 1
            
    return  count
def rep(data,key,new):
    with open(data,'r',encoding='cp949') as file:
        my=file.read()
        N=my.replace(key,new)
        return N
        # print(f'my{my}')
        # for i in my:
        #     print(f'i: {i}')
        #     if key in i:
        #         i.replace(key,new)
        # print('이후my:',my)  
def remov(path,what):
    f=open(path,'w')
    f.write("")
    f.write(what)
    f.close()


text_file_path = 'C:\\Users\\Owner\\Documents\\CODE\\Git1\\firgit.hwp'
from hanword import *
new_text_content = ''
target_word = '이'
new_word = '@@@@@@'
#with open(text_file_path,'r') as f:
    #lines = f.readline() ## 기존 텍스트파일에 대한 내용을 모두 읽는다.
lines =get_text(text_file_path)
print(type(lines))
lines.replace(target_word,new_word)
print(lines)
# for i, l in enumerate(lines):

#     new_string = l.replace(target_word,new_word)
#     if new_string:
#         new_text_content += new_string + '\n'
        # else:
        #     new_text_content += '\n'f
#print(new_text_content,"#########")               
# with open(text_file_path,'w') as f:
#     print(f"new_text_content{new_text_content}")
#     f.write(new_text_content)