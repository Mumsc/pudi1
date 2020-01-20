d = read.csv("C:\\Users\\Admin\\Desktop\\New folder\\Ages1.csv")
x=d$Experimental
y=d$Comparison
r=lm(y~poly(x,2))
r
