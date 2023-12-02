import random
print('')
ascii_art = r'''   ____                           _               _           
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  | |__  _   _ 
| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| | '_ \| | | |
| |_| |  __/ | | |  __/ | | (_| | || (_) | |    | |_) | |_| |
 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    |_.__/ \__, |
                                                       |___/ 
 _   _    _    _     ___  _  _   _  _    ___  
| | | |  / \  | |   / _ \| || | | || |  / _ \ 
| |_| | / _ \ | |  | | | | || |_| || |_| | | |
|  _  |/ ___ \| |__| |_| |__   _|__   _| |_| |
|_| |_/_/   \_\_____\___/   |_|    |_|  \___/ 
'''
print(ascii_art)
print()
print()
bin_list = []
quantity = 0
random_num = 0
cvv = 862
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
def bin_input ():
    bin = int(input('Enter your bin here :'))
    random_number_size = 16 - len(str(bin))
    print(random_number_size)
    if len(str(bin)) >= 6 :
       print('valid input ✅')
       global quantity
       print()
       quantity = int(input('How many Card Do you want :'))
       month = int(input('Enter month (january = 1 - december = 12 / random = 13) :'))
       if month >= 1 and month <= 12 :
            print()
            print(month_list[month - 1],'✅')
            year = int(input('Enter Year (ex:- 2023/2025/2022 or random = -1) :')) 
            if year != -1:
                print()
                print(year ,'✅')   
                print()
                global cvv
                cvv = int(input('Enter CVV(random = -1/custom = 1) :'))
                print()
                if cvv == -1:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    while quantity != 0 :
                        
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        random_cvv = random.randint(100,999)
                        sym = '|'
                        
                        card =  str(bin) + str(random_num) + sym + str(month) + sym + str(year) + sym + str(random_cvv)
                        print(card)
                        quantity = quantity - 1
                else:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    random_cvv = input('Enter CVV :')
                    print(random_cvv)
                    while quantity != 0 :
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        
                        sym = '|'
                        card =  str(bin) + str(random_num) + sym + str(month) + sym + str(year) + sym + random_cvv
                        print(card)
                        quantity = quantity - 1   
            else:
                month_random = [2023,2024,2025,2026,2027,2028,2029,2030]
                
                cvv = int(input('Enter CVV(random = -1/custom = 1) :'))
                print()
                if cvv == -1:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    while quantity != 0 :
                        
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        random_cvv = random.randint(100,999)
                        random_month = random.randint(0,7)
                        sym = '|'
                        
                        card =  str(bin) + str(random_num) + sym + str(month) + sym + str(month_random[random_month]) + sym + str(random_cvv)
                        print(card)
                        quantity = quantity - 1
                else:
                    month_random = [2023,2024,2025,2026,2027,2028,2029,2030]
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    random_cvv = input('Enter CVV :')
                    print(random_cvv)
                    while quantity != 0 :
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        random_month = random.randint(0,7)
                        sym = '|'
                        card =  str(bin) + str(random_num) + sym + str(month) + sym + str(month_random[random_month]) + sym + random_cvv
                        print(card)
                        quantity = quantity - 1 

                        
       elif month == 13 :
            random_mont = ['01','02','03','04','05','06','07','08','09','10','11','12']
            
            print()
            year = int(input('Enter Year (ex:- 2023/2025/2022 or random = -1) :')) 
            if year != -1:
                print()
                print(year ,'✅')   
                print()
                
                cvv = int(input('Enter CVV(random = -1/custom = 1) :'))
                print()
                if cvv == -1:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    while quantity != 0 :
                        mont_random = random.randint(0,12)
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        random_cvv = random.randint(100,999)
                        sym = '|'
                        
                        card =  str(bin) + str(random_num) + sym + random_mont[mont_random] + sym + str(year) + sym + str(random_cvv)
                        print(card)
                        quantity = quantity - 1
                else:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    random_cvv = input('Enter CVV :')
                    print(random_cvv)
                    while quantity != 0 :
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        mont_random = random.randint(0,12)
                        sym = '|'
                        card =  str(bin) + str(random_num) + sym + random_mont[mont_random] + sym + str(year) + sym + random_cvv
                        print(card)
                        quantity = quantity - 1   
            else:
                month_random = [2023,2024,2025,2026,2027,2028,2029,2030]
                
                cvv = int(input('Enter CVV(random = -1/custom = 1) :'))
                print()
                if cvv == -1:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    while quantity != 0 :
                        
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        random_cvv = random.randint(100,999)
                        random_month = random.randint(0,7)
                        sym = '|'
                        mont_random = random.randint(0,11)
                        card =  str(bin) + str(random_num) + sym + random_mont[mont_random] + sym + str(month_random[random_month]) + sym + str(random_cvv)
                        print(card)
                        quantity = quantity - 1
                else:
                    start_number = '1'
                    end_number = '9'
                    start_random_number = start_number*random_number_size
                    end_random_number = end_number*random_number_size
                    random_cvv = input('Enter CVV :')
                    print(random_cvv)
                    while quantity != 0 :
                        random_num = random.randint(int(start_random_number), int(end_random_number))
                        mont_random = random.randint(0,12)
                        sym = '|'
                        random_month = random.randint(0,7)
                        card =  str(bin) + str(random_num) + sym + random_mont[mont_random] + sym + str(month_random[random_month]) + sym + random_cvv
                        print(card)
                        quantity = quantity - 1 
                    
           
       else:
           print()
           print('unvalid input ⚠️')
           bin_input()
       
          
    else:
        print()
        print('Unvalid bin ⚠️')
        print()
        bin_input()   
       



bin_input()     
