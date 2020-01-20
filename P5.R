d=read.csv("C:\\Users\\Admin\\Desktop\\New folder\\RICFiles\\blood_pressure.csv")
install.packages("BSDA")
library("BSDA")
r=z.test(d$bp_before,sigma.x = sd(d$bp_before),mu=156)
if(r$p.value>r$statistic)
{
  print("H0 is Accepted")
  } else
    {
      print("H0 is Rejected")
      }
