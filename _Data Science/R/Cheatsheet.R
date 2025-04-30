# 1.compute definite integral
integrate(function(x) x^2,lower=0,upper=5)

# 2.create data.frame
df <- data.frame(price=c(1,2,3),symbol=c("a","b","d"),action=c("13","asdf",12))
dimnames(df) <- list(c("a","b",5),c("col1","col2","col3"))
df

# 3.plot scatter plots
x=data.frame(AAPL=c(12,14,15,16),IBM=c(66,64,67,61),CME=c(22,27,33,38))
pairs(x)

# 4.rows without NAs
x[,4] <- c(12,rep(NA,3))
complete.cases(x) #by row #why by row? because for data.frame, cols are features, rows are observations
na.omit(x)
x

# 5.correlation matrix can be directly computed
cor(x[, 1:3])

# 6.reverse a vector
y=1:7
rev(y)

# 7. objects in environment
save()
load()
rm() #remove
identical() #check if two objects are the same

# 8. test EMA using different start points
df <- read.csv("0700.HK.csv", stringsAsFactors=FALSE)
df <- df[,c(1,6)]
df$EMA <- ema(df$Adj.Close,10)
