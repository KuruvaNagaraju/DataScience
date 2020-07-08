
#######################################################
## By the end of this activity you will be familiar with 
## plotting graps in R using packages graphics & ggplot2
rm(list=ls(all=TRUE)) ## Clear the environment varibles.
setwd("D:/DataScience/Pratice/Visualization/Visualizations_in_R")
##################################
## Topics Covered:
## Visualizing numeric attributes ,using histograms, boxplots and scatter plots.
## Visualizing categorical attributes using bar plots.
## Visualizing association of numerical and categorical attributes.
## Visualizations using ggplot2.

##################################
#Packages to be installed.
#install.packages("ggplot2")
library(ggplot2)

##################################
###Data reading and prepping
cars_data <- read.csv("Automobiles.csv") ## Read data.
colnames(cars_data) ## Display column names.
colnames(cars_data)[1]<-"aspiration" ## Replace column 1 name with aspiration.
str(cars_data) ## Get the structure of the data.
sum(is.na(cars_data)) ## Get sum of null values for the data.
cars_data <- na.omit(cars_data) ## omitting missing values
summary(cars_data) ## Get summary statistics of the data.



#Do if needed:
#Find prospective numeric attributes and convert them into numeric
#Find prospective categorical attributes and convert them into categorical

##################################
###Visualizing numeric attribtues

## Histograms : To view the distribution of one-dimensional data.
attach(cars_data) ## attach the dataframe so that columns can be referenced directly.
par(mfrow=c(1,1)) ## Customize the params; mfrow=c(1,2) specifies 2 multiple figures in 1 row;
#mfrow-->make for row
### A dry plot.
hist(city_mpg)


## Adding variable names and some beautification to histo gram.
hist(city_mpg, col="green", xlab="City Mileage",
     main="Frequency Histogram:City Mileage",
     xlim = c(10,60), ylim = c(0,70))

## Histogram for highway mileage column.
hist(highway_mpg, col="red", xlab="Highway Mileage",
     main="Frequency Histogram:Highway Mileage", xlim = c(10,60), ylim = c(0,70)) 


## Boxplots : To view & compare distributions of data.
## Boxplot to view the distribution of data:
par(mfrow=c(1,1))
boxplot(city_mpg,
        main = "Box Plot: City Mileage",
        ylab = "City Mileage")

boxplot(highway_mpg,
        main = "Box Plot: Highway Mileage",
        ylab = "Highway Mileage")

## Boxplot to compare the values of numeric attribute with respect to a categorical attribute:
par(mfrow=c(1,1))
boxplot(city_mpg ~ aspiration, 
        main = "Mileage Vs. Engine Aspiration Type", 
        xlab="Aspiration", 
        ylab="mileage")

## install.packages("corrplot")
library(corrplot)
## Using plot() : when a factor of x values and a vector of y values is given to plot(), it automatically prints a boxplot.
plot(aspiration,city_mpg,
     main = "Mileage Vs. Engine Aspiration Type")

## correlation plots.
library(corrplot)
corMat <- cor(cars_data[,sapply(cars_data, is.numeric)])
corrplot::corrplot(corMat) ## corrplot:: is used bcz if another package also have corrplot() method then we may  get problem,so here are we are mentioning package name along with method name
corrplot::corrplot(corMat,tl.cex = 0.7)
corrplot::corrplot(corMat, tl.cex = 0.7, method = "number")
## tl.cex text size of the columns 

#######################################
### Visualizing Categorical attributes

## Bar Charts: To display numeric values(on y-axis), for different categories(on x-axis).
plot(aspiration,main = "Distribution of aspiration types")

plot(aspiration,
     main = "Distribution of aspiration types",
     horiz = T) ## For horizontal bars.  


barplot(table(aspiration),
        main = "Distribution of aspiration types")


## Stacked bar plots.
counts <-table(drive_wheel,aspiration)
barplot(counts, main="Distribution of drive-wheel in each aspiration type",
        col=rainbow(7),
        xlab="Engine Aspiration",
        ylab = "#Cars",
        legend.text = TRUE, ## it will give one color box ## default legend.text is TRUE
        args.legend = list(x = "topright", ## where u wan box
                           bty = "o", cex = 0.6, ## bty = box type, cex = size of box
                           ncol=1)) ## right side column box columns

## Grouped bar plots.
counts <-table(drive_wheel,aspiration)
barplot(counts, main="Distribution of drive-wheel in each aspiration type",
        col=rainbow(7),
        xlab="Engine Aspiration", ylab = "#Cars",
        legend.text = TRUE,
        args.legend = list(x = "topright", bty = "n", cex = 0.6, ncol=2),
        beside = TRUE)


## A note on differences between histograms and bar charts: 
## Histograms are used to show distributions of variables while bar charts are used to compare variables. 
## Histograms plot binned quantitative data while bar charts plot categorical data. 
## Bars can be reordered in bar charts but not in histograms.

## Scatter Plots: To display the relationship between two continuous variables.
plot(city_mpg, price, 
     ylab="Price",
     main="Kerb_weight Vs. Car Price",
     pch=1)

## Often, a scatterplot will also have a line showing the predicted values based on some statistical model.
## Add fit lines.
abline(lm(price~city_mpg),
       col="green") # regression line (y~x) 
abline(h=mean(price,na.rm = T),col='red')
abline(v=mean(city_mpg,na.rm=T),col='black')

##################################
###VISUALIZATIONS USING ggplot2
## ggplots are built based on the idea of "grammar of graphics" by Leland Wilkinson, where,
## Noun -> Data 
## Verb -> "geom_" + plot type
## Adjectives -> Aesthetics (x,y,color, shape, size, fill, etc)

## Bar plots.
## Start with a basic graph  in ggplot.
## If y is a numeric vector, use stat="identity"; the default is stat="bin" for categorical.
library(ggplot2)
ggplot(cars_data,aes(x=fuel_system))+  ## First one is target,second one is source(aes).
  geom_bar() +   ## what kind of plot u want,if we didn't mention any prameter for bar() method then it take deault values.
  xlab("Fuel_system") + 
  ylab("# Cars") 
  

## Add title to ggplot.
ggplot(cars_data,aes(x=fuel_system)) + geom_bar() +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("Numer of Cars in various fuel system types")

## Fill color based on number of cylinders.
ggplot(cars_data,
       aes(x=fuel_system, fill=num_cyl)) + ## fill will give number of cylinder,fill is categorical attribute
  geom_bar() +
  xlab("Fuel_system") + ylab("# Cars")  +
  ggtitle("Numer of Cars in various fuel system types")


ggplot(cars_data,aes(x=fuel_system)) +
  geom_bar(aes(fill=num_cyl)) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types") +
  scale_fill_manual(values=c("blue4", "orangered2", "red",
                            "goldenrod", "darkolivegreen1", "black", 'firebrick'))
## Number of colors should be equals to no of cylinders.

## Make a grouped bar chart with similar graph attributes.
ggplot(cars_data,aes(x=fuel_system, 
                     fill=num_cyl)) + 
        geom_bar(position = "dodge") +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")

## To adjust the width of the bars.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")

## To add a black outline to the bars.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) + 
        geom_bar(width = 0.5, colour = "black" ) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")

## Change back ground.
## To remove grey background in plot.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")+
        theme_bw() #theme_classic

## To remove grey and gridlines in the Bg.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")+
        theme_classic()

## Adjust text size and angle of labels.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")+
        theme_classic()+
        theme(axis.text.x=element_text(angle=45,
                                       size=12),
              text=element_text(size=14))

## Now remove the legend position.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")+
        theme_classic()+
        theme(axis.text.x=element_text(angle=45,size=12),
              text=element_text(size=10), 
              legend.position = "none")

## Add counts on top of each bin.
ggplot(cars_data,aes(x=fuel_system,
                     fill=num_cyl)) +
        geom_bar(width = 0.5) +
        xlab("Fuel_system") + ylab("# Cars")  +
        ggtitle("#Cars in various fuel system types")+
        theme_classic()+
        theme(axis.text.x=element_text(angle=45,size=12),
              text=element_text(size=14),
              legend.position = "none") +
        geom_text(stat="count",aes(label=..count..),vjust=0) 

## Check the number of 2-cylindered cars.
sum((num_cyl)=="two")

## Scatterplot.
## Basic scatterplot with 2 dimensions, x and y.
ggplot(data=cars_data, aes(x=city_mpg,
                           y=price))+ geom_point() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("City_mpg Vs. Car Price")


## Scatterplot with 3 dimensions (by adding color to the basic plot).
ggplot(data=cars_data, aes(x=city_mpg,
                           y=price, 
                           colour = aspiration)) + 
        geom_point() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("City_mpg Vs. Car Price")

## Scatterplot with 5 dimensions (by adding color, shape, & size to the basic plot).
ggplot(data=cars_data, aes(x=city_mpg, y=price,
                           colour = aspiration, 
                           size = hoesepower, 
                           shape = drive_wheel)) + 
        geom_point() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("City_mpg Vs. Car Price")

## We see that rear wheel drives give less mileage and are very costly.
## Also, higher the horsepower, higher is the cost and lesser is the mileage.

## Faceting: To create a subplot for each level of a factor variable.
ggplot(data=cars_data, aes(x=city_mpg, y=price, colour = aspiration, size = hoesepower, shape = drive_wheel)) + 
        geom_point() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("City_mpg Vs. Car Price") + 
        facet_wrap(~fuel_system)



## We see that majority of idi and mfi systems are turbo aspirated
## Majority of idi types have rear-wheel drive systems
## Bluebarrel types are not turo aspirated
## mpfi covers good range of price, in combination with hp, aspiration and drive_wheels.

## Add jitter. 
## without jitter, points might be overlapped/crowded at a level.
ggplot(data=cars_data, 
       aes(x=drive_wheel, y=price,
           colour = aspiration, size = hoesepower)) + 
        geom_point() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("drive_wheel Vs. Car Price") 

## Jitter widens the point space for each level.
ggplot(data=cars_data, aes(x=drive_wheel, y=price, colour = aspiration, size = hoesepower)) + 
        geom_jitter() + 
        xlab("City_mpg")+ylab("Price") + 
        ggtitle("drive_wheel Vs. Car Price") 

## Managing and grouping graphical gg objects to plot graphs.
p1 <- ggplot(data = cars_data)
p2 <- aes(x = num_cyl, y = price)

p1 + p2 + geom_point() ## scatterplot.
p1 + p2 + geom_point(aes(color = factor(aspiration))) ## scatterplot with 3 dimensions.
p1 + p2 + geom_boxplot() ## boxplot.
p1 + p2 +geom_bar(stat="identity") ## barplot.

detach(cars_data) ## detach the dataframe.

## To save plot.
ggsave("plotName.png",plot = last_plot())

###############################################################
## References:
## https://cran.r-project.org/web/packages/ggplot2/ggplot2.pdf
## https://www.forbes.com/sites/naomirobbins/2012/01/04/a-histogram-is-not-a-bar-chart/#53a11ed36d77
## http://www.cookbook-r.com/Graphs/Bar_and_line_graphs_(ggplot2)/
## https://web.stanford.edu/~imalone/VAM/VAMSlides.pdf

###############################################################
## Viz-Paradigms :
## https://towardsdatascience.com/data-visualization-best-practices-less-is-more-and-people-dont-read-ba41b8f29e7b
## http://socialmediaguerilla.com/content-marketing/less-is-more-improving-the-data-ink-ratio/
## http://www.infovis-wiki.net/index.php/Data-Ink_Ratio


