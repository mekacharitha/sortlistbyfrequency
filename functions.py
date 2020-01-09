def sorting(lis):
  lis1=[]
  lis2=[]
  for i in lis:
    lis1.append([len(i),i])
    lis2.append(len(i))
  for i in range(len(lis1)):
    k=lis2.count(lis1[i][0])
    lis1[i][0]=k
  lis1.sort(key=lambda x:x[0])
  lis2=[]
  for i in range(len(lis1)):
    lis2.append(lis1[i][1])
  return(lis2)