#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq

def main():
    Listfac = []

    def NumFactor(n):
        global average
        count_fact = 0
        for i in range(1, n+1):
            if n % i == 0:
                print(i, end = ", ")
                Listfac.append(i)
                count_fact += 1
                heapq.nlargest(3,Listfac)
                average = round(sum(heapq.nlargest(3,Listfac ))/len(heapq.nlargest(3,Listfac )), 2)
        print("\nList = ", Listfac)
        return count_fact

    n = int(input("\nEnter a number: ")) 
    x = NumFactor(n)

    print("The count is:", x)


    if x < 10:
        print("This is too less. Do you want to contiue?")
    if x > 10:
        print("The three highest factors are:", heapq.nlargest(3,Listfac))
        print("Their average =", average)
        print("Do you want to contiue?")

    while True:
        m = input("Enter Y for another number or N to quit: ").upper()
        if m == "Y":
            main()
            break
        if m == "N":
            break        

    
main()


# In[ ]:





# In[ ]:




