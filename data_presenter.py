

import plotly.graph_objects as go # This line imports the plotly library and assigns it to the variable 'go'

open_file = open('CupcakeInvoices.csv')

# for line in open_file:   # Non dynamic way of doing it
#     line = line.rstrip('\n').split(',')
#     print(line[2])
#     print(float(line[4]))


chocolate = 0
vanilla = 0
strawberry = 0

choc_total = 0
van_total = 0
straw_total = 0

for line in open_file:
    # Splits the string into an array on ',' This makes it easier to accessthe values we want
    line = line.rstrip('\n').split(',')
    # This is essentially like a .js for loop. It's saying for 'i' in 'length' of 'line' do this =>
    for i in range(len(line)):
        if line[i] == 'Chocolate':  # If at the index [i] the value is equal to the string 'Chocolate',
            chocolate += 1  # Add 1 to the value of chocolate
            choc_total += float(line[i + 1]) * float(line[i + 2]) # Multiply the value of [i + 1] and [i + 2], in this case it would be the two values after 'Chocolate'
        elif line[i] == 'Vanilla': # Remaining lines work same as above
            vanilla += 1
            van_total += float(line[i + 1]) * float(line[i + 2])
        elif line[i] == 'Strawberry':
            strawberry += 1
            straw_total += float(line[i + 1]) * float(line[i + 2])


print("Chocolate", chocolate, "Vanilla", vanilla, "Strawberry", strawberry)
# print(choc_total, van_total, round(straw_total, 2))   # Test code

open_file.close()


open_file = open('CupcakeInvoices.csv')

total = 0

for line in open_file: 
    subtotal = 0 # For each line in open_file initialize a subtotal of zero
    line = line.rstrip('\n').split(',') # Once again turns line into an array split on ','
    subtotal = float(line[3]) * float(line[4])  # Turns the values of index [3] and index [4] into a float number and then multiplies them
    total += subtotal # Adds the subtotal that we calculated on the line above to the total then restarts the loop


print(round(total, 2)) # print the total from above, rounded to two decimal places


open_file.close()

fig = go.Figure(data=go.Bar(y=[choc_total, van_total, round(straw_total, 2)], x=["Chocolate", "Vanilla", "Strawberry"]))
# The above line creates a var 'fig' and sets the value to the plotly figure 'Bar graph', y axis will display the values of choc, van, and straw
# from line 17-19, the x axis will display Chocolate, Vanilla, and Strawberry as strings
fig.show() 
# this will show the var fig in the browser
