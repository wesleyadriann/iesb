install.packages('rpart','rpart.plot')

library('rpart')
library('rpart.plot')
servico = read.table('topicos_bd/algoritmos/dados/qualidade_servico.csv', header = TRUE,  sep = ';')
modelo_ad<-rpart(
    R ~ EP + QR + LE,
    data = servico,
    method = "class",
    control = rpart.control(minsplit = 1),
    parms=list(split="Information")
    )
plot.modelo<-rpart.plot(modelo_ad, type=3)
