d=mtcars
d
x=d$mpg
y=d$wt
s=cor(x,y,method="pearson")
install.packages("ggpubr")
library("ggpubr")
ggscatter(d,x = "mpg",y = "wt",
          add="reg.line", conf.int = TRUE,
          cor.coef = TRUE,cor.method = "pearson",
          xlab = "X unit", ylab = "Y unit")

