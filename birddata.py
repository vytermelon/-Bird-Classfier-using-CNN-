import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
datadir="D:\Birds150\\150\\train"
categories=["BROWN THRASHER","CACTUS WREN","CALIFORNIA CONDOR","CALIFORNIA GULL","CALIFORNIA QUAIL","DARK EYED JUNCO","DOWNY WOODPECKER","EASTERN BLUEBIRD","EASTERN ROSELLA","EASTERN TOWEE"]#['OSPREY', 'OSTRICH', 'PAINTED BUNTIG', 'PARADISE TANAGER', 'PARUS MAJOR', 'PEACOCK', 'PELICAN', 'PEREGRINE FALCON', 'PINK ROBIN', 'PUFFIN', 'PURPLE FINCH', 'PURPLE GALLINULE', 'PURPLE MARTIN', 'PURPLE SWAMPHEN', 'QUETZAL', 'RAINBOW LORIKEET', 'RED FACED CORMORANT', 'RED HEADED WOODPECKER', 'RED THROATED BEE EATER', 'RED WINGED BLACKBIRD', 'RED WISKERED BULBUL', 'RING-NECKED PHEASANT', 'ROADRUNNER', 'ROBIN', 'ROSY FACED LOVEBIRD', 'ROUGH LEG BUZZARD', 'RUBY THROATED HUMMINGBIRD', 'SAND MARTIN', 'SCARLET IBIS', 'SCARLET MACAW', 'SNOWY EGRET', 'SPLENDID WREN', 'SPOONBILL', 'STORK BILLED KINGFISHER', 'STRAWBERRY FINCH', 'TEAL DUCK', 'TIT MOUSE', 'TOUCHAN', 'TRUMPTER SWAN', 'TURKEY VULTURE', 'TURQUOISE MOTMOT', 'VARIED THRUSH', 'VENEZUELIAN TROUPIAL', 'VERMILION FLYCATHER', 'VIOLET GREEN SWALLOW', 'WESTERN MEADOWLARK', 'WILD TURKEY', 'WILSONS BIRD OF PARADISE', 'WOOD DUCK', 'YELLOW HEADED BLACKBIRD']
#["ALBATROSS","ALEXANDRINE PARAKEET","AMERICAN AVOCET","AMERICAN BITTERN","AMERICAN COOT","BALD EAGLE","BARN OWL","BARN SWALLOW","BAR-TAILED GODWIT","BAY-BREASTED WARBLER"]
#,"FLAME TANAGER","FLAMINGO","FRIGATE","GLOSSY IBIS","GOLD WING WARBLER"]
#,"HAWAIIAN GOOSE","HOODED MERGANSER","HOOPOES","HORNBILL","HOUSE FINCH","INDIGO BUNTING","JABIRU","LARK BUNTING","LILAC ROLLER","LONG-EARED OWL","MALLARD DUCK","MANDRIN DUCK","MARABOU STORK","MIKADO  PHEASANT","MOURNING DOVE","PEREGRINE FALCON","PARADISE TANAGER","PARUS MAJOR","PEACOCK","PELICAN"]


training_data=[]
class_num=[]


IMG_SIZE=64
def create_training_data():
    test=[1,0,0,0,0,0,0,0,0,0]
    #,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for category in categories:
        path=os.path.join(datadir,category)
       # class_num=categories.index(category)
        class_num=test
        test= test[-1:] + test[:-1]
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img))
                img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)
                new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()
random.shuffle(training_data)
x_train=[]
y_train=[]

for features,label in training_data:
    x_train.append(features)
    y_train.append(label)
x_train=np.array(x_train)
y_train=np.array(y_train)
#print(x_train.shape)


testing_data=[]
IMG_SIZE=64
datadir="D:\Birds150\\150\\valid"
def create_testing_data():
    test=[1,0,0,0,0,0,0,0,0,0]
    #,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for category in categories:
        path=os.path.join(datadir,category)
        class_num1=test
        test= test[-1:] + test[:-1]
        for img in os.listdir(path):
            try:
                img_array1=cv2.imread(os.path.join(path,img))
                img_array1=cv2.cvtColor(img_array1,cv2.COLOR_BGR2RGB)
                new_array1=cv2.resize(img_array1,(IMG_SIZE,IMG_SIZE))
                testing_data.append([new_array1,class_num1])
            except Exception as e:
                pass
create_testing_data()
random.shuffle(testing_data)
x_test=[]
y_test=[]
for features,label in testing_data:
    x_test.append(features)
    y_test.append(label)
x_test=np.array(x_test)
y_test=np.array(y_test)
