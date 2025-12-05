import plotly.express as px

#  data
items = ['Soap', 'Chocolates', 'Books', 'Pens', 'Laptop', 'Mobile']
quantity = [50, 10, 50, 30, 70, 60]
price = [55, 15, 45, 5, 80, 45]


data = {
    'Items': items,
    'Quantity': quantity,
    'Price': price
}


# Donut Chart: Quantity Distribution
fig_donut = px.pie(
    data_frame=data,
    names='Items',
    values='Quantity',
    hole=0.4,  # Makes it a donut chart
    title='Quantity Distribution of Items'
)
fig_donut.update_traces(textinfo='percent+label')  # Show both percent and labels


# Bar Chart: Price of Items
fig_bar = px.bar(
    data_frame=data,
    x='Items',
    y='Price',
    text='Price',
    title='Price of Items',
    color='Items'  # Optional: different colors for each item
)
fig_bar.update_traces(textposition='outside')


fig_donut.show()
fig_bar.show()
