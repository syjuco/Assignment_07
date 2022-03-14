#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SSyjuco, 2022-Mar-05, Modified File to complete Assignment06 Requirements. You can follow the # comments from top to bottom to track my changes. 
# SSyjuco, 2022-Mar-13, Modifying file for Assignment07 requirements. Follow along the in line TO DONE comments for the changes. 
#------------------------------------------#

import pickle

# -- DATA -- # TO DONE added strFileOutput variable to create the binary file CDInventory.dat
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage input file
strFileOutput = 'CDInventory.dat'
objFile = None  # file object


# -- PROCESSING -- # From Assignment 6 I added 4 new functions: add_cd():, delete_cdfr_memory():, write_file(file_name, table):, input_cd():
class DataProcessor:
    """Processing the data to and from memory"""

    @staticmethod
    def add_cd():
        """ Function to add CD details to memory
        
        Args: 
            None.
        
        Returns:
            newlst = [] # need to define a list receive the results of the input_cd() 
            newlst = IO.input_cd() # this captures the user CD input from another function (will discuss in the IO class below) and converts to a list
            dicRow = {'ID': newlst[0], 'Title': newlst[1], 'Artist': newlst[2]} # the dictionary keys can now receive the inputs from the newlst indices
            lstTbl.append(dicRow) # dicRow can now be appended to lstTbl as usual
            IO.show_invenotry(lstTbl) # this calls the IO function show_inventory(lstTbl) to confirm to the user what was added to the table 
        
        
        """
        newlst = []
        newlst = IO.input_cd()
        dicRow = {'ID': newlst[0], 'Title': newlst[1], 'Artist': newlst[2]}
        return lstTbl.append(dicRow)
        
    @staticmethod
    def delete_cdfr_memory():
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        
        
class FileProcessor: # I added the third out of four functions in this class, write_file(file_name, table):
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table): 
        """Function to save the CDs currently in memory to the text file CDInventory.txt
        
        Args:
            file_name (string): name of the file the data will be written to
            table (list): list that will be written to the file 
        
        Returns: 
            None. 
        
        
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        
        
    @staticmethod #TO DONE added new function to save file to binary format
    def write_fileb(fileName, data):
        """Function to save the CDs in memory to a binary file 
        
        Args:
            fileName (string): name of the file the data will be written to
            data: data to be written to the file 
        
        Returns: 
            None.
        
        """
        
        with open(fileName, 'wb') as file: 
            pickle.dump(data, file)
            
    
    @staticmethod #TO DONE added new function to read the contents of the binary file and load to memory
    def read_filep(fileName):
        """ Function to read the contents of the binary file and load to memory
        
        Args:
            fileName: name of the file to read from
            
        Returns:
            data: the data that will be loaded to memory from the file. 
        """
        
        with open(fileName, 'rb') as file: 
            data = pickle.load(file)
        return data        
    
    
# -- PRESENTATION (Input/Output) -- #

class IO:  
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod    
    def input_cd():
        """Function to ask the user for CD details to add to memory: CD's ID, CD title, Artist
            UPDATES AS OF 03/13/2022: added try - except method to ensure users inputs a numerical CD ID. 
            
        Args:
            None. 
        
        Returns: 
            strID = input('Enter ID: ').strip() # asks the user for their desired ID to assign to the CD
            strTitle = input('What is the CD\'s title? ').strip() # asks the user to input the CDs title
            stArtist = input('What is the Artist\'s name? ').strip() #asks the user to input the Artist of the CD
            return [strID, strTitle, stArtist] #returns the result of the three inputs as a list. this is important for the add_cd(): function to get a list result to process. 
        
        """
        strInput = ''
        while True: #TO DONE this sets up the try - except block. Objective is to catch the user from initial input of the CD ID.
            strInput = input('Enter CD numerical ID: ').strip()
            try: 
                strID = int(strInput)
                strTitle = input('What is the CD\'s title? ').strip()
                stArtist = input('What is the Artist\'s name? ').strip()
                return [strID, strTitle, stArtist]
            except:
                print('Please input a number to proceed.')
    

# 1. When program starts, read in the currently saved Inventory TO DONE added functions to start the program with the user creating a new CDInventory file in binary form. 
print('To get started, we need to create the file CDInventory.dat by pickling your first CD.')
DataProcessor.add_cd() # captures input from the user to create one CD to be stored
FileProcessor.write_fileb(strFileOutput, lstTbl) # write the CD in the form lstTbl to the file CDInventory.dat. CD is also now in memory. 
IO.show_inventory(lstTbl) #confirms to the user what's now in memory. 

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes': #TO DONE added the following lines of code to load the data from the CDInventory.dat file
            print('reloading...')
            f = open(strFileOutput, 'rb') # this reads the CDinventory.dat file
            lstTbl = pickle.load(f) # assigns the contents of the file to the variable lstTbl
            IO.show_inventory(lstTbl) # we are able to run show_inventory because data will be loaded as a table, same way it was pickled. 
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # 3.3.2 Add item to the table
        DataProcessor.add_cd() #This function combines steps 3.3.1 and 3.3.2
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i': #TO DONE added try - except block to let the programmer know what to specify for the table. 
        try:
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        except: 
            print('Could not load inventory. specify a table () for the funcion IO.show_inventory.\nCheck your code.')
    # 3.5 process delete a CD
    elif strChoice == 'd': #TO DONE added try- except block to let programmer know delete function will not work without a table in show_inventory() function
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        try:
            IO.show_inventory(lstTbl)
        except: 
            print('Could not load delete function due to show_inventory function missing a table ().\nCheck your code.')
            continue
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_cdfr_memory() #This is the new function that was defined 
        IO.show_inventory(lstTbl) # this displays the updated CDs in memory
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_fileb(strFileOutput, lstTbl) #TO DONE will now use the function to write to CDInventory.dat
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




