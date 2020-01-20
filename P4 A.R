d=read.csv("C:\\Users\\Admin\\Desktop\\New folder\\System.csv")
tbl=table(d$A,d$B)
chisq.test(tbl)
