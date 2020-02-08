#Goal: Replace str1 with str2 from every filename which contains str1 in CURRENT directory

import os
path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(path)
i = 1
str1 = '.zip'   #string to be replaced  //PARAMETER//
str2 = ''       #string replacement     //PARAMETER//

for file in files:
    old_name = str(file)
    if str1 in old_name:
        new_name = old_name.replace(str1,str2)
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        i = i+1
