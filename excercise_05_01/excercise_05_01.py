running_count = 0
running_total = 0.0
while True:
    saved_value = input('Enter a number: ')
    if saved_value == 'done':
        break
    try:
        float_value = float(saved_value)
    except:
        print('Invalid input')
        continue
    # print(float_value)
    running_count = running_count + 1
    running_total = running_total + float_value

# print('ALL DONE')
print(running_total, running_count, running_total/running_count)
