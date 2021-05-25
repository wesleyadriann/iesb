install.packages("e1071")
library("e1071")

planejamento<-read.table('topicos_bd/algoritmos/dados/planejamento.csv', header = TRUE,  sep = ';')
planejamento
modelo_NB<-naiveBayes(planejamento[1:4], planejamento$VENDER)
modelo_NB
exemplar_teste<-data.frame(PREVISAO="sol", TEMPERATURA="frio",UMIDADE="normal",VENTO="sim")
exemplar_teste
p<-predict(modelo_NB, exemplar_teste, type = "class")
p
