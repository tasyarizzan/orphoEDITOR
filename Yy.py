def distance(a, b):

    n, m = len(a), len(b)
    t = b
    if n > m:

        a, b = b, a
        n, m = m, n
        t = a

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
                add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
                if a[j-1] != b[i-1]:
                    change += 1
               # if  min(add, delete, change) < 4 and min(add, delete, change) > 0  :
                current_row[j] = min(add, delete, change)

    return [current_row[n], t]
#dic = [  'кювет', 'креветка', 'маршрутка', 'привет', 'привод', 'котел','пиздец']
#dic = [ 'кювет', 'креветка', 'рривет', 'привет', 'прикет', 'превед']
dict_file = "dictrus.txt"
dic = []

with open(dict_file, 'r') as read_file:
    for line in read_file:
        dic.append(line.strip('\n'))


s1 = input("s1 = ")
variants = [[3, '455']];
for s2 in dic :
    d = distance(s1, s2)
    if d[0] <= int (variants[len(variants)-1][0]) :
       #  variants.clear()
         variants.append(d)

#with open(dict_file, 'r') as read_file:
 #   for line in read_file:
  #      d = distance(s1, line)
   #     if d[0] <= int (variants[len(variants)-1][0]) :
    #      #variants.clear()
     #     variants.append(d)


print (variants)
print (len(variants))
print('Ваше слово было исправлено на:', variants[len(variants)-1][1])