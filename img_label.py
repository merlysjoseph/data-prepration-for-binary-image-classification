import os
import cv2
import numpy as np
def preprocessing_and_labelling(severity_folder):
    height=width=256
    x_train = []
    y_train=[]
    label_convert=[]

    for dirs in os.listdir(severity_folder):
        #print(dirs)
        if dirs.startswith('.'):
            continue
        print('*******************', os.path.join(severity_folder, dirs))
        for f in os.listdir(os.path.join(severity_folder, dirs)):
            file_p = os.path.join(severity_folder, dirs, f)
            label=file_p.split('/')[-2]
            label_final=''
            if label in label_convert:
                label_final=label_convert.index(label)
            else:
                label_convert.append(label)
                label_final = label_convert.index(label)

            img = cv2.imread(file_p)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret,thresh_img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)

            data=cv2.resize(thresh_img,(height,width))
            print(data.shape)
            
            img=data.reshape(-1,1) #reshape((data.shape[0],data.shape[1], 1))
            print(img.shape)
           
            #img_modified = img / 255.0
            #print(img_modified)
            # print (os.path.join(severity_folder,dirs,f))

            x_train.append(img)
            y_train.append(label_final)
            # print('moderate')
    
    print('Done...')
    
    return np.asarray(x_train),np.asarray(y_train)