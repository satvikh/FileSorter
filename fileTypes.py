#import the config file
import config


#create a class type for each thing
class File:
    def __init__(self,fileName):  
        
        self.name=fileName
        self.location=config.preSortPath + "\\" + self.name
        print(self.location)
        #self.type----identifies the file every character starting from the last for a period (file extension)
        self.type=''
        
        for i in reversed(fileName):#identifies file type if identifiable 
            self.type=i+self.type
            if i=='.':
                break
         

        else: #If file type cannot be identified, then the type is set to a blank value
            self.type=''

        #File.destination----identifies the destination of the file using the config file
        self.destination=config.fileDestinations[self.type]+self.name
        


    



   