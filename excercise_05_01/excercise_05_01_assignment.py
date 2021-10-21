saved_list = []

while True:
    Saved_value = input(['Enter a number:'])
        
    if Saved_value == 'done':
        break
    try:
        Float_value = int(Saved_value)
        saved_list.append(Float_value)
        
    except:
        print('Invalid input')
        continue
    

# print('ALL DONE')
print('Maximum is',max(saved_list))
print('Minimum is',min(saved_list))