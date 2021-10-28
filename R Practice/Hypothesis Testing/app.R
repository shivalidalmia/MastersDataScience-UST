#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(tibble)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("Sampling Distributions"),
  
  sidebarLayout(
    sidebarPanel(
      numericInput("p", "True Proportion", 0.65),
      numericInput("n", "Sample Size:",10),
      actionButton("update","Update View"),
      h4("Summary"),
      verbatimTextOutput("samps")
    ), 
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot")
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  Values <- reactiveValues(samp_props = NULL, w = 0.05)
  #s <- sqrt((input$n)*p*(1-p))
  
  observeEvent(input$update, {
    Values$samp_props <- NULL
    for(i in 1:1000){
      temp_samp <- sample(c(1,0),input$n,prob = c(input$p,1-input$p),replace = TRUE)
      Values$samp_props <- c(Values$samp_props,mean(temp_samp))
    }
    if(input$n < 20){
      Values$w = 0.1
    } else if(input$n < 50) {
      Values$w = 0.05
    } else {
      Values$w = 0.01
    }
    
  })
  
  output$distPlot <- renderPlot({
    if(is.null(Values$samp_props)){
      ggplot()+
        xlim(c(-0.05,1.05)) + 
        ylim(c(0,0.4)) +
        labs(title = "Sampling Distribution for a Proportion. Red Line Indicates the True Proportion", x="Sample Proportion", y="Proportion")
    } else {
      tb <- tibble(data = Values$samp_props)
      ggplot(tb,aes(x=tb$data, y = stat(count/sum(count))))+
        geom_histogram(breaks = seq(from = 0-Values$w, to = 1+Values$w, by = Values$w),
                       col = "blue",
                       fill = "green",
                       alpha = 0.2) +
        xlim(c(-0.05,1.05)) + 
        ylim(c(0,0.4)) +
        labs(title = "Sampling Distribution for a Proportion. Red Line Indicates the True Proportion", x="Sample Proportion", y="Proportion") +
        geom_vline(xintercept = input$p, color = "red")
    }
  })
  
  output$samps <- renderPrint({
    if(is.null(Values$samp_props)){  
      cat(" Mean:","\n","Standard Deviation:")
    } else {
      cat(" Mean:", mean(Values$samp_props), "\n",
          "Standard Deviation:", sd(Values$samp_props))
    }
  })
  
}

# Run the application 
shinyApp(ui = ui, server = server)

