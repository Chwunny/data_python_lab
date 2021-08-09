
import plotly.graph_objects as go

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
    line = line.rstrip('\n').split(',')
    for i in range(len(line)):
        if line[i] == 'Chocolate':
            chocolate += 1
            choc_total += float(line[i + 1]) * float(line[i + 2])
        elif line[i] == 'Vanilla':
            vanilla += 1
            van_total += float(line[i + 1]) * float(line[i + 2])
        elif line[i] == 'Strawberry':
            strawberry += 1
            straw_total += float(line[i + 1]) * float(line[i + 2])


print("Chocolate", chocolate, "Vanilla", vanilla, "Strawberry", strawberry)
# print(choc_total, van_total, round(straw_total, 2))

open_file.close()


open_file = open('CupcakeInvoices.csv')

total = 0

for line in open_file:
    subtotal = 0
    line = line.rstrip('\n').split(',')
    subtotal = float(line[3]) * float(line[4])
    total += subtotal


print(round(total, 2))


open_file.close()

fig = go.Figure(data=go.Bar(y=[choc_total, van_total, round(
    straw_total, 2)], x=["Chocolate", "Vanilla", "Strawberry"]))
fig.show()
