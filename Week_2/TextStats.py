class TextStats:
  def __init__(self,text):
    self.text = text
    
 
  def stat(self):
    self.Dic = {}
    f = open(self.text,encoding = 'utf-8')
    for i in f:
      word = i.split()
      for i in word:
        if i in self.Dic:
          self.Dic[i] += 1
        else:
          self.Dic[i] = 1
    print(self.Dic)
    f.close()

  def top(self,k):
    self.Sort = sorted(self.Dic.items(), key=lambda x: x[1], reverse=True)
    print(self.Sort)
    for i in range(k):
      print(self.Sort[i])

  def save(self):
    Save = dict(self.Sort)
    with open("OUTPUT.txt",'w',encoding = 'utf-8') as f:
      for x,y in Save.items():
          f.write(str(x))
          f.write(" ")
          f.write(str(y))
          f.write("\n")



       
s = "INPUT.txt"
f  =TextStats(s)
f.stat()
f.top(3)
f.save()
