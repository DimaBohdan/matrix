def space_separated_row_by_row(row_num):
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input('Input row: ').split(" ")]
      matrix_list.append(row_list)
   return matrix_list

def fill(str):
   a = str.split(']')
   list = []
   list.append([i for i in a if i != ''])
   for i in list[0]:
      if ',[' in i:
         b = ',['
   c = []
   c.append(list[0][0].replace('[[', ""))
   l = [i.replace(b, '') for i in list[0][1:]]
   for i in l:
      c.append(i)
   new_lis = [i.split(",") for i in c]
   new = []
   for k in new_lis:
      new.append([int(i) for i in k])
   return new
