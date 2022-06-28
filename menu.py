#creat a menu which do the following operations
 #add new item
 #insert new item
 #remove
 #search
 #print
lists=[]
#creat a menu
while True:
   print(""" MENU
            1.New item
            2.insert item
            3.remove item
            4.search
            5.print
            6.pop the item
            7.sort
            8.reverse sort
            9.exit
        """
          )
   #add new item
   a=int(input("enter your choice:"))
   if a==1:
         c=input("enter an item to be added:")
         lists.append(c)

                
   elif a==2:                                             #insert new item 
         b=input("enter an item to be inserted:")
         i=int(input("on which index to be inserted:"))
         lists.insert(i,b)
      
   elif a==3:                                              #remove item
         d=input("enter item to be removed:")
         lists.remove(d)
   
   elif a==4:                                              #search an item
        e=input("enter item to be serached:")
        try:
            r=lists.index(e)
            print(f' {e} is found at index {r}')
        except:
            print(f' {e} not found in the list')

 
   elif a==5:                                               #print an item

         print("lists:",lists)
   
   elif a==6:                                               #pop an item
        index=int(input("enter index to be poppod:"))
        try:
            lists.pop(index)
            print(f' {index} item is popped')
        except:
            print(f' {index} not found in the list')
  
   elif a==7:                                               #sort the list
         lists.sort()
  
   elif a==8:                                               #reverse the list
        lists.sort(reverse=True)
   elif a==9:                                                #exit 
        print("thank you")
        break
   else:
       print("invalid choice")
       break
            
          
