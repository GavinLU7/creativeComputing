sum1 = 0
num = 0
count = 0
symbol = ''
while num != '':
        num = float(num)
        sum1 += num
        count += 1
        if count // 10 == 1 or count % 10 > 3:
                symbol = 'th'
        elif count % 10 == 0:
                symbol = 'th'
        elif count % 10 == 1:
                symbol = 'st'
        elif count % 10 == 2:
                symbol = 'nd'
        else:
                symbol = 'rd'
        num = input('Please input the '+ str(count) + symbol + ' number: ')
        isnum = False
        while not isnum  and num != '':
                preventError = num
                preventError = list(preventError)
                if num.find('-') == 0 :
                        preventError.remove('-')
                if num.find('.') > 0 :
                        preventError.remove('.')
                preventError = ''.join(preventError)
                isnum = preventError.isnumeric()
		
                if not isnum:
                        num = input('Please input correct the number: ')         
		
print('Your input', count-1, 'numbers')	
print('sum of numbers:',sum1)
