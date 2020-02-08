# Numerate the files e.g. example_0, example_1  ...
# str1 is the new name

import os
path = 'C:/Users/Pantelis/Documents/html (my)/Dad Websites/metal_website/images_metal/signs/2-regulation'
files = os.listdir(path)
i = 0
str1 = 'regulation'       #new name     //PARAMETER//

print('job done in dir:',path)
for file in files:
    old_name = str(file)
    # TODO: Specify the file extension
    if '.png' in old_name:
        new_name = str1+'_'+str(i)+'.png'
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        i = i+1
