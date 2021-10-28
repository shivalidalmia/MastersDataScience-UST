  ## define plot data
  xlim <- c(0,1000);
  ylim <- c(0,1000);
  px <- c(0,10,50,60,100);
  py <- c(0,0,0,0,0);
  lx.buf <- 5;
  lx <- seq(xlim[1]+lx.buf,xlim[2]-lx.buf,len=length(px));
  ly <- 20;
  
  ## create basic plot outline
  par(xaxs='i',yaxs='i',mar=c(5,1,1,1));
  plot(NA,xlim=xlim,ylim=ylim,axes=F,ann=F);
  axis(1);
  
  ## plot elements
  segments(px,py,lx,ly);
  points(px,py,pch=16,xpd=NA);
  text(lx,ly,px,pos=3);
  
?dotchart

dotchart(c(0,50,300,550,600),xlim = c(-1,700),main = "Distribution 1")  

?boxplot

scores = c(57, 66, 69, 71, 72, 73, 74, 77, 78, 78, 79, 79, 81, 81, 82, 83, 83, 88, 89, 94)
par(mfrow = c(1, 2))
boxplot(scores)
boxplot(scores)
abline(h = min(scores), col = "Blue")
abline(h = max(scores), col = "Yellow")
abline(h = median(scores), col = "Green")
abline(h = quantile(scores, c(0.25, 0.75)), col = "Red")

gpa = c(1.990,3.359,3.085,0.735,2.248,1.978,1.388,1.339,1.388,1.637)
act = c(20,28,33,14,26,18,15,18,15,19)

stu <- data.frame(gpa = c(1.990,3.359,3.085,0.735,2.248,1.978,1.388,1.339,1.388,1.637) , act=c(20,28,33,14,26,18,15,18,15,19), height = c(68,71,67,66,67,68,72,70,72,75))

plot(stu$gpa,stu$height)
