ten_things = "Apples Oranges Crows Telephone Light Sugar"
# 给一个名为”ten_things"的东西赋值。

print "Wait there's not 10 things in that list, let's fix that."
# 打印这一行文字。

stuff = ten_things.split(' ')
# 给一个名为“stuff”的东西赋值， 值是把ten_things拿来split
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "boy"]
# 增加一个变量名为more_stuff，共有8个值

while len(stuff) != 10:
#当stuff这个变量的长度不等于10
   next_one = more_stuff.pop()
   # 一个变量名为next_one, 它的值为more_stuff里面pop出来的
   print "Adding: ", next_one
   # 打印“Adding：” 及pop出来的词
   stuff.append(next_one)
   # 把“next_one"添加到stuff里面
   print "There's %d times now." % len(stuff)
   # 打印这行文字，用到%这个参数
   
print "There we go:", stuff
#打印这行文字及stuff现在的赋值

print "Let's do some things with stuff."
#打印这行文字
print stuff[1]
#打印stuff这个变量里位置1的值
print stuff[-1]
#打印stuff这个变量位置-1的值
print stuff.pop()
#打印stuff这个变量里pop出来的值
print ' '.join(stuff)
#打印出‘’里和stuff加在一起的值
print '#'.join(stuff[3:5])
# 打印出‘#’和stuff里位置3到位置5的值连在一起的东西

