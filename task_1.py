def arithmetic(num_1, num_2, operation):
    x = 0
    if operation == '+':
        x = num_1 + num_2
    elif operation == '-':
        x = num_1 - num_2
    elif operation == '*':
        x = num_1 * num_2
    elif operation == '/':
        x = num_1 / num_2
    return x

print(arithmetic(10,5,'+'))
print(arithmetic(10,5,'-'))
print(arithmetic(10,5,'*'))
print(arithmetic(10,5,'/'))