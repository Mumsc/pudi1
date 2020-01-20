i = mtcars[,c("am","cyl","hp","wt")]
data = glm(formula = am ~ cyl + hp +wt,data = i,family = binomial)
print(summary(data))
newdata = data.frame(wt = 2.1, hp =180, cyl = 1)
predict(data, newdata, type = "response")

