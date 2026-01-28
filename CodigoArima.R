# Carga de datos y análisis preliminar de los mismos
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
data <- read.csv("data_monthly.csv")
data.ts <-ts(data$MONTHLY_AVG, start = c(2010,1), frequency = 12)
data.ts
plot(data.ts)

# Tema 1: Tratamiento mediante suavizado de los datos
library(timsac)

# Por defecto de tipo "aditivo"
descomp1=decompose(data.ts)
plot(descomp1)
data.tsDES=data.ts-descomp1$seasona
plot(data.tsDES,col="blue")
par(new=T)
plot(data.ts,col="red")

# Cambiamos a tipo "multiplicativo"
descomp1=decompose(data.ts,type="multiplicative")
plot(descomp1)
data.tsDES=data.ts-descomp1$seasona
plot(data.tsDES,col="blue")
par(new=T)
plot(data.ts,col="red")


# Tema 2: 
