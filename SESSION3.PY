#برنامه ای که تا وقتی کاربر 0 وارد نکرده عدد دریافت کند - اعداد بزگتر از میانگین را چاپ کند
number_list = []

while True:
    x = int(input("please enter a number:"))
    if x == 0:
        break
    number_list.append(x)
    
n = len(number_list)
avg = sum(number_list) / n

print("average is", avg)



upper_avg = []

lower_avg = []

for i in range(0,n,1):
     if number_list[i] > avg:
         upper_avg.append(number_list[i])
        
     elif number_list[i] < avg: 
        lower_avg.append(number_list[i])
       
       
       
       
print("upper avg is :", upper_avg)

print("lower avg is :", lower_avg)



    
    
