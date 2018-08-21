read_q <- function(filename){
  # Load connectivity matrix
  csv <- read.csv(filename, header=F)
  data = t(as.matrix(csv))
  # row y, col x
  rownames(data) = 1:12
  colnames(data) = 1:7
  return(data)}


plot_grid <- function(data){
  library(reshape2)
  library(ggplot2)
  melted_data <- melt(data, id = rolnames(data))
  # csv.m$V1 <- factor(csv.m$V1, levels=unique(as.character(csv.m$V1)) )
  qplot(x=Var1, y=Var2, data=melted_data, fill=value, geom="tile") +
    theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
    scale_fill_gradient2(low = "blue", mid = "white", high = "red")}

# Set a gradient of colors that we will use for as many of the plots as possible
# The gradient goes from blue (negative correlations) to white (0) to red (positive correlations)
# cols2 <- colorRampPalette(c("blue","white","red"))(256)

# Notice how we are only using columns 2 through 14 for the plot.
# The first column contains the region labels
# image(data,  col = cols2, zlim=c(-1, 1))

# library(lattice)
# heatmap(data, Rowv=NA, Colv=NA, col = cols2, zlim=c(-1, 1))
# levelplot(data, at=seq(-.5, .5, .01), col.regions=cols2)

data.0.1 = read_q("0_1.csv")
data.0.2 = read_q("0_2.csv")
data.1.2 = read_q("1_2.csv")
total = data.0.1 + data.0.2 + data.1.2


plot_grid(data.0.1)
plot_grid(data.0.2)
plot_grid(data.1.2)
plot_grid(total)
