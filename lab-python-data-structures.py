#!/usr/bin/env python
# coding: utf-8

# # Lab | Data Structures 

# ## Exercise: Managing Customer Orders
# 
# As part of a business venture, you are starting an online store that sells various products. To ensure smooth operations, you need to develop a program that manages customer orders and inventory.
# 
# Follow the steps below to complete the exercise:
# 
# 1. Define a list called `products` that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".
# 
# 2. Create an empty dictionary called `inventory`.
# 
# 3. Ask the user to input the quantity of each product available in the inventory. Use the product names from the `products` list as keys in the `inventory` dictionary and assign the respective quantities as values.
# 
# 4. Create an empty set called `customer_orders`.
# 
# 5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the `customer_orders` set.
# 
# 6. Print the products in the `customer_orders` set.
# 
# 7. Calculate the following order statistics:
#    - Total Products Ordered: The total number of products in the `customer_orders` set.
#    - Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
#    
#    Store these statistics in a tuple called `order_status`.
# 
# 8. Print the order statistics using the following format:
#    ```
#    Order Statistics:
#    Total Products Ordered: <total_products_ordered>
#    Percentage of Products Ordered: <percentage_ordered>% 
#    ```
# 
# 9. Update the inventory by subtracting 1 from the quantity of each product. Modify the `inventory` dictionary accordingly.
# 
# 10. Print the updated inventory, displaying the quantity of each product on separate lines.
# 
# Solve the exercise by implementing the steps using the Python concepts of lists, dictionaries, sets, and basic input/output operations. 

# In[1]:


# Define the list of products
products = ["tshirt", "mug", "hat", "book", "keychain"]


# In[2]:


inventory = {}


# In[4]:


inventory["tshirt"]=int(input("Please enter the amount of t-shirts:"))
inventory["mug"]=int(input("Please enter the amount of mugs:"))
inventory["hat"]=int(input("Please enter the amount of hats:"))
inventory["book"]=int(input("Please enter the amount of books:"))
inventory["keychain"]=int(input("Please enter the amount of keychains:"))


# In[5]:


tshirt = inventory["tshirt"] 
mug = inventory["mug"] 
hat = inventory["hat"]
book = inventory["book"] 
keychain = inventory["keychain"] 


# In[6]:


customer_orders = {}


# In[7]:


customer_orders = (input("Please pick a product from the list:"), input("Please pick another product from the list:"), input("Please pick your final product from the list:"))


# In[8]:


print(customer_orders)


# In[9]:


total_products_ordered = len(customer_orders)
percentage_ordered = (len(customer_orders)/len(inventory)*100)

order_status = (total_products_ordered, percentage_ordered)


# In[10]:


print('Order Statistics:')
print('Total Products Ordered:', total_products_ordered) 
print('Percentage of Products Ordered:', percentage_ordered)


# In[12]:


mug_2 = inventory["mug"]-1
hat_2 = inventory["hat"]-1
keychain_2 = inventory["keychain"]-1

print(inventory)


# In[ ]:




