#import files and modules
import config
from fileTypes import *
import os
import shutil


# FORWARD ACTION
def fileSort():
    #Define variables and functions
    fileNames = os.listdir(config.preSortPath) #Provides a list of the file names

    # change the directory of each name in filenames after making them classes
    classedFiles=[]
    
    for files in fileNames:
        classedFiles.append(File(files))
        

    
    #clear the records file
    
            
    open('fileRecords.txt', 'w').close()
    #Traverse through the list and update fileRecords with respective class attributes and final Destination
    with open('fileRecords.txt', 'r+') as fileRecords:


        for file in classedFiles:


            #Moves the file
            shutil.move(file.location, file.destination)


            #Changes the fileRecords file accordingly
            fileRecords.write(file.name)

            for i in range(config.columnWidth-len(file.name)):
                fileRecords.write(' ')

            fileRecords.write(f'|{file.location}') #first separator

            for i in range(config.columnWidth-len(file.name)):
                fileRecords.write(' ')

            fileRecords.write(f'|{file.destination} \n') #Second separator





        

def fileUndo():

    #access the fileRecords and use the columns to move all of the files back
    with open('fileRecords.txt', 'r') as fileRecords:
  
        for lines in fileRecords:
            formLines=lines.split('|')

            ultraFormLine=(formLines[0].strip(),formLines[1].strip(),formLines[2].strip())
            location=ultraFormLine[2]
            destination=ultraFormLine[1]

            print(location,destination)
            shutil.move(location, destination)

#determining the action

chosen=False

while chosen==False:
    forwardOrUndo=input('Do you want to undo a past file sort? [y/n]: ')

    if forwardOrUndo=='y':
        fileUndo()
        chosen=True
    elif forwardOrUndo=='n':
        fileSort()
        chosen=True
