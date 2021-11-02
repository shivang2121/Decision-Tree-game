# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:39:13 2021

@author: PS
"""
print("Choose your favorite fruit from Grape, Apple , Watermelon, Cherry, Lemon, Grapefuit and Banana ")
val = input("Input Color of your favorite fruit. Choose from Green, yellow, red \n")
color=(val.lower())

if(color=="green"):
    val = input("Input size of your favorite fruit. Choose from small, medium, big \n")
    size=(val.lower())
    if(size=="small"):
        print("Your favorite fruit is Grape")
    if(size=="medium"):
        print("Your favorite fruit is Apple")
    if(size=="big"):
        print("Your favorite fruit is Watermelon")   
    
 
if(color=="red"):
    val = input("Input size of your favorite fruit. Choose from small, medium \n")
    size=(val.lower())
    if(size=="medium"):
        print("Your favorite fruit is Apple")
    if(size=="small"):
        val = input("Input taste of your favorite fruit. Choose from sweet, sour \n")
        taste=(val.lower())   
        if(taste=="sweet"):
            print("Your favorite fruit is Cherry")
        if(taste=="sour"):
            print("Your favorite fruit is Grape")
        
if ((color=="yellow")):
    val = input("Input shape of your favorite fruit. Choose from round,thin \n")
    shape=(val.lower())
    if(shape=="round"):
         val = input("Input size of your favorite fruit. Choose from big,small \n")
         size=(val.lower())
         if(size=="small"):
             print("Your favorite fruit is Lemon")
         if(size=="big"):
             print("Your favorite fruit is Grapefruit")
         
    if(shape=="thin"):
        print("Your favorite fruit is Banana")  
        

else:
    "enter valid fruit name"
print("\nLearning from game: Entropy is how much information is missing. As we asked you more questions, less information was missing and therefore the entropy decreases. This is what is used in Decision Tree Classifier algorithm and is called minimization of entropy. As well, like in this game, the decision tree classifier always asks the correct questions at each step. Here is how the decision tree for this game looks like")
from PIL import Image
myImage = Image.open("fruit.png");
myImage.show();