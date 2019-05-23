s='azcbobobegghakl'
order1='a'
order2='a'
for letter in s[1:-1]:
    if ord(letter)>=ord(order1[-1]):
        order1+=letter
    else:
        if len(order2)<=len(order1):
            order2=order1
        order1=letter
print("Longest substring in alphabetical order is:",order2)
    
