2dintegral
RNG:numpy.random.random
Python version:3.11

允许积分类型
\int\int f(x,y)dxdy

test.py 
	X_start = 0
	Y_start = 0

	X_end = 1
	Y_end = 1

	f = lambda x,y : x**2 + y**2
	
	true:1.11111...
	
	test_result:0.11103385028545024 \pm 5.256192379075023e-05

main.py
	
	若实现手动输入方程功能会增加程序解析负担,大约是十倍左右,故不予实现
若需要实现,可以仿照如下例子:

def main(X_start=0, X_end=1, Y_start=0, Y_end=1):
    print("RNG:numpy.random.random")
    print("")
    funstr = input("输入方程")
    #funstr = "x**2*y**2"
    f = lambda x,y: eval(funstr)
    #f = lambda x,y:x**2*y**2
    print("运算开始")
    
    N = 10000
    
    start = time.time()
    random_xpoints = np.random.uniform(X_start, X_end, N)
    random_ypoints = np.random.uniform(Y_start, Y_end, N)

    X = np.arange(X_start, X_end, 100)
    Y = np.arange(Y_start, Y_end, 100)

    guess = np.array(list(map(f, random_xpoints, random_ypoints)))

    ave = sum(guess)/N
    I = ave*(X_end-X_start)*(Y_end-Y_start)

    S2 = sum((guess-ave)**2)/(N-1)
    S  = S2**0.5
    end = time.time()
    
    print(I, "\pm", S/N**0.5)
    print("运算结束,用时:", round(end-start, 4))
