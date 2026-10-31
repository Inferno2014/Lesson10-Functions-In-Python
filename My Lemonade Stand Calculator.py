def sum(total,quantity):
    print('Your total is',total * quantity,'and quantity is', quantity,'Lemonades')
def give(total,quantity,change):
    print('You get',change - (total * quantity),'change. Thank you for visiting. See you soon.')
total = 20
print('Greetings and welcome to my lemonade shop. Enter the quantity of lemonades below.')
quantity = int(input('Enter how many lemonades you need.: '))
sum(total,quantity)
change = int(input('Enter amount you will pay.It should be equal or greater than the total.: '))
give(total,quantity,change)
