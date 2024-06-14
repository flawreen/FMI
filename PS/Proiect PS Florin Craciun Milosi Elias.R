# Milosi Elias - Florin Craciun -241

# 1
n <- 3
m <- 2

#* am calculat numarul maxim de valori necunoscute cu formula (m + n - 1)
#* am reusit doar pentru cazul (3, 2)
#* generez mai intai repartitiile marginale pentru X si Y si valorile pi pentru repartitia comuna
#* apoi generez pozitii random in matrice pe care sa le fac necunoscute
frepcomgen <- function(n, m) {

    lim_inf <- -(n+m)
    lim_sup <- (n+m)
    missing_values <- m + n - 1 # destule valori necunoscute
    
    x_values <- sample(lim_inf:lim_sup, n, replace=FALSE)
    y_values <- sample(lim_inf:lim_sup, m, replace=FALSE)
    
    p_values <- c(0.25, 0.4, 0.35)
    q_values <- c(0.35, 0.65)
    
    pi_values <- matrix(c(0.15, 0.05, 0.15, 0.10, 0.35, 0.20), nrow=n, ncol=m)
    
    while (missing_values > 0) {
        i <- sample(1:(n+1), 1)
        j <- sample(1:(m+1), 1)
        
        if (i <= n && j <= m) {
            if (is.na(pi_values[i,j])) next
            missing_values <- missing_values - 1
            pi_values[i,j] <- NA
            next
        }
        if (i <= n) {
            if (is.na(p_values[i])) next
            missing_values <- missing_values - 1
            p_values[i] <- NA
            next
        }
        if (j <= m) {
            if (is.na(q_values[j])) next
            missing_values <- missing_values - 1
            q_values[j] <- NA
        }
    }
    
#    print(pi_values)
    pi_values <- cbind(pi_values, p_values)
    pi_values <- rbind(pi_values, c(q_values, 1))
#    print(pi_values)
    
    rez <- data.frame(pi_values)
    colnames(rez) <- NULL
    rownames(rez) <- NULL
    
    colnames(rez) <- c(y_values, 'p')
    rownames(rez) <- c(x_values, 'q')
    
    return(rez)
}


fcomplrepcom <- function() {
    # Variabila ok are valoarea 1 atat timp cat mai exista valori necunoscute
    ok <<- 1
    while (ok != 0) {
        # for pe linii
        for (i in (n+1):1) {
            ok <<- 0
            # verific daca exista valoare necunoscuta pe linie
            na_values = sum(is.na(tabel[i,]))
            # verific cate valori necunoscute exista pe linie pentru variabila ok
            # daca sunt mai multe atunci nu le pot afla dintr-un calcul
            # calculez doar daca exista o necunoscuta
            if (na_values >= 1) ok <<- 1
            if (na_values == 1) {
                if (is.na(tabel[i,3])) tabel[i,3] <<- tabel[i,1] + tabel[i,2]
                else {
                    if (is.na(tabel[i,1])) tabel[i,1] <<- tabel[i,3] - tabel[i,2]
                    else tabel[i,2] <<- tabel[i,3] - tabel[i,1]
                }
            }
        }
        
        ok <<- 0
        # for pe coloane
        for (j in (m+1):1) {
            na_values = sum(is.na(tabel[,j]))
            if (na_values >= 1) ok <<- 1
            if (na_values == 1) {
                if (is.na(tabel[4,j])) tabel[4,j] <<- sum(tabel[1:3,j])
                else {
                    if (is.na(tabel[1,j])) tabel[1,j] <<- tabel[4,j] - sum(tabel[2:3, j])
                    else if (is.na(tabel[2,j])) tabel[2,j] <<- tabel[4,j] - (tabel[1,j] + tabel[3,j])
                    else tabel[3,j] <<- tabel[4,j] - sum(tabel[1:2, j])
                }
            }
        }
    }
}
tabel <- frepcomgen(n, m)
print(tabel)
fcomplrepcom()
print(tabel)

# construieste o repartitie marginala cu valorile date
# se apeleaza frepmarginal(n, as.numeric(rownames(tabel)[1:3]), as.numeric(tabel[1:3,3]))
# functia construieste o matrice de 2 linii reprezentand reparitia marginala
frepmarginal <- function(k, X, p) {
    temp <<- matrix(nrow=0, ncol=k)
    temp <<- rbind(temp, X)
    temp <<- rbind(temp, p)
    return(temp)
}


# functie care calculeaza P(numeVa1 | numeVa2 = val)
fPcond <- function(numeVa1, numeVa2, val) {
    if (numeVa1 == "X") {
        temp <- rep_marg_x
        for (i in 1:n) {
            temp[2,i] <- round(tabel[i,val] / tabel[(n+1),val], 2)
        }
        return(temp)
    } else {
        temp <- rep_marg_y
        for (i in 1:m) {
            temp[2, i] <- round(tabel[val,i] / tabel[val,(m+1)], 2)
        }
        return(temp)
    }
}

# calculeaza o probabilitate pentru (X, Y)
# exemplu: fPcomun("X", ">", 0.2, "Y", "<", 1.7) calculeaza P(X > 0.2, Y < 1.7)
fPcomun <- function(numeVa1, semn1, val1, numeVa2, semn2, val2) {
    rez <- 0
    if (numeVa1 == "X") {
        for (i in 1:n) {
            for (j in 1:m) {
                # pentru P(X > 0.2, Y < 1.7) verifica daca xi > 0.2 si yj < 1.7
                if (eval(parse(text=paste(rownames(tabel)[i], semn1, val1))) && eval(parse(text=paste(colnames(tabel)[j], semn2, val2)))) {
                    # print(tabel[i,j])
                    rez <- rez + tabel[i,j]
                }
            }
        }
    } else {
        for (i in 1:m) {
            for (j in 1:n) {
                if (eval(parse(text=paste(rownames(tabel)[i], semn1, val1))) && eval(parse(text=paste(colnames(tabel)[j], semn2, val2)))) {
                    rez <- rez + tabel[i,j]
                }
            }
        }
    }
    return(rez)
}

# verifica daca repartitia comuna data este independenta prin relatia pi(i, j) = p(i) * q(j)
fverind <- function() {
    for (i in 1:n) {
        for (j in 1:m) {
            if (tabel[i, j] != (tabel[i, (m+1)] * tabel[(n+1), i])) {
                return(0)
            }
        }
    }
    return(1)
}


#rep_marg_x <- frepmarginal(n, as.numeric(rownames(tabel)[1:3]), as.numeric(tabel[1:3,3]))
#rep_marg_y <- frepmarginal(m, as.numeric(colnames(tabel)[1:2]), as.numeric(tabel[4, 1:2]))
print(X)
print(Y)

XcY <- fPcond("Y", "X", 2)
print(XcY)
g3 <- fPcomun("X", ">", 0.2, "Y", "<", 1.7)
print(rez)
suntIndep <- fverind()
print(suntIndep)



# incercarea sa p, q si pi random, dar nu am reusit sa generez pi a.i suma(linia i) = pi
# si suma(coloana i) = qi pentru x si y dependente
incercare <- function() {
    pi_values <- matrix(runif(m*n, min=0.01, max=min(c(p_values, q_values))/2), nrow = n, ncol = m)
    pi_values <- round(pi_values * (1 / sum(min(q_values, p_values))), 2)
    sp <- 0.99
    sq <- 0.99
    while(sp != 1) {
        p_values <- runif(n, min=0.01, max=1)
        p_values <- round(p_values * (1 / sum(p_values)), 2)  # sa aiba suma 1, cu 2 zecimale
        sp <- sum(p_values)
    }
    
    
    while(sq != 1) {
        q_values <- runif(m, min=0.01, max=1)
        q_values <- round(q_values * (1 / sum(q_values)), 2)
        sq <- sum(q_values)
    }
}

#a
library(shiny)

library(animate)

# Definirea funcției pentru calculul integralei duble
calculeaza_integrala_dubla <- function(f, a, b, c, d) {
    integrare <- integrate(function(y) {
        sapply(y, function(yy) integrate(function(x) f(x, yy), c, d)$value)
    }, a, b, subdivisions = 100)$value
    
    mesaj <- if (is.finite(integrare)) {
        "Teorema lui Fubini poate fi aplicată. Rezultatul integraliei este:"
    } else {
        "Teorema lui Fubini nu poate fi aplicată pentru această funcție."
    }
    
    rezultat <- list(integrare = integrare, mesaj = mesaj)
    return(rezultat)
}

# Interfața Shiny
ui <- fluidPage(
    titlePanel("Verificarea Teoremei lui Fubini pentru integrale duble"),
    sidebarLayout(
        sidebarPanel(
            textInput("functie", "Introdu funcția (ex: x^2 + y^2)"),
            numericInput("a", "Limita inferioară pentru x:", 0),
            numericInput("b", "Limita superioară pentru x:", 1),
            numericInput("c", "Limita inferioară pentru y:", 0),
            numericInput("d", "Limita superioară pentru y:", 1),
            actionButton("calculeaza", "Calculează")
        ),
        mainPanel(
            textOutput("rezultat_text")
        )
    )
)

# Server logic
server <- function(input, output) {
    observeEvent(input$calculeaza, {
        tryCatch({
            # Convertirea string-ului introdus într-o funcție R
            f <- function(x, y) eval(parse(text = input$functie))
            # Calculul integraliei duble și afișarea rezultatului
            rezultat <- calculeaza_integrala_dubla(f, input$a, input$b, input$c, input$d)
            output$rezultat_text <- renderText({
                paste0(rezultat$mesaj, " ", rezultat$integrare)
            })
            
        }, error = function(e) {
            output$rezultat_text <- renderText({
                paste("Eroare:", e$message)
            })
        })
    })
}
shinyApp(ui, server)





#c

library(shiny)
library(animate)
calculeaza_integrala_dubla <- function(f, a, b, c, d) {
    integrare <- integrate(function(y) {
        sapply(y, function(yy) integrate(function(x) f(x, yy), c, d)$value)
    }, a, b, subdivisions = 100)$value
    
    mesaj <- if (is.finite(integrare)) {
        "Teorema lui Fubini poate fi aplicată. Rezultatul integraliei este:"
    } else {
        "Teorema lui Fubini nu poate fi aplicată pentru această funcție."
    }
    
    rezultat <- list(integrare = integrare, mesaj = mesaj)
    return(rezultat)
}

# Interfața Shiny
ui <- fluidPage(
    titlePanel("Verificarea densității de probabilitate"),
    sidebarLayout(
        sidebarPanel(
            textInput("functie", "Introdu funcția (ex: exp(-x^2 - y^2))"),
            numericInput("a", "Limita inferioară pentru x:", 0),
            numericInput("b", "Limita superioară pentru x:", 1),
            numericInput("c", "Limita inferioară pentru y:", 0),
            numericInput("d", "Limita superioară pentru y:", 1),
            actionButton("verifica", "Verifică")
        ),
        mainPanel(
            textOutput("rezultat_text")
        )
    )
)

# Server logic
server <- function(input, output) {
    observeEvent(input$verifica, {
        tryCatch({
            # Convertirea string-ului introdus într-o funcție R
            f <- function(x, y) eval(parse(text = input$functie))
            # Calculul integraliei duble și afișarea rezultatului
            volum <- calculeaza_integrala_dubla(f, input$a, input$b, input$c, input$d)
            output$rezultat_text <- renderText({
                paste0(volum$mesaj, " ", volum$integrare)
            })
            
            # Verificarea condițiilor pentru densitatea de probabilitate
            conditie1 <- all(sapply(seq(0, 1, length.out = 100), function(y) all(f(seq(0, 1, length.out = 100), y) >= 0)))
            conditie2 <- volum$integrare == 1
            
            # Afișarea rezultatului
            rezultat_text <- if (conditie1 && conditie2) {
                "Funcția este o densitate de probabilitate."
            } else {
                "Funcția NU este o densitate de probabilitate."
            }
            output$rezultat_text <- renderText({
                rezultat_text
            })
            
            # Salvarea animației într-un document LaTeX
            #output$grafic <- renderUI({
            #    saveLatex({
            #        ani.options(interval = 0.1)
            #        curve3d(f, xlim = c(input$a, input$b), ylim = c(input$c, input$d), col = "blue", theta = 30, phi = 30)
            #    }, interval = 0.1, movie.name = "densitate.tex", ani.width = 400, ani.height = 400)
            #    tags$iframe(src = "densitate.tex", height = 400, width = 400)
            #})
        }, error = function(e) {
            output$rezultat_text <- renderText({
                paste("Eroare:", e$message)
            })
        })
    })
}

# Rulează aplicația Shiny
shinyApp(ui, server)




#e

#LIMITARE: creaza grafice pentrtu functia scrisa de noi la densitatea_comuna

# Încărcare librării
library(shiny)

# Densitatea comună
densitate_comuna <- function(x, y) {
    exp(-x^2 - y^2)
}

# Densitatea marginală a lui X
densitate_marginala_X <- function(x) {
    integrate(function(y) densitate_comuna(x, y), lower = -Inf, upper = Inf)$value
}

# Densitatea marginală a lui Y
densitate_marginala_Y <- function(y) {
    integrate(function(x) densitate_comuna(x, y), lower = -Inf, upper = Inf)$value
}

# Densitatea condiționată a lui Y dat fiind X = x
densitate_conditionata_Y_X <- function(y, x) {
    densitate_comuna(x, y) / densitate_marginala_X(x)
}

# Interfața Shiny
ui <- fluidPage(
    titlePanel("Construirea densităților marginale și condiționate"),
    sidebarLayout(
        sidebarPanel(
            
        ),
        mainPanel(
            plotOutput("plot_marginala_X"),
            plotOutput("plot_marginala_Y"),
            plotOutput("plot_conditionata_Y_X")
        )
    )
)

# Server logic
server <- function(input, output) {
    output$plot_marginala_X <- renderPlot({
        x_vals <- seq(-3, 3, length.out = 100)
        y_vals <- sapply(x_vals, function(x) densitate_marginala_X(x))
        plot(x_vals, y_vals, type = "l", col = "blue", xlab = "X", ylab = "Densitate marginală a lui X")
    })
    
    output$plot_marginala_Y <- renderPlot({
        y_vals <- seq(-3, 3, length.out = 100)
        x_vals <- sapply(y_vals, function(y) densitate_marginala_Y(y))
        plot(y_vals, x_vals, type = "l", col = "red", xlab = "Y", ylab = "Densitate marginală a lui Y")
    })
    
    output$plot_conditionata_Y_X <- renderPlot({
        y_vals <- seq(-3, 3, length.out = 100)
        x_val <- input$x_val
        densitati_conditionate <- sapply(y_vals, function(y) densitate_conditionata_Y_X(y, x_val))
        plot(y_vals, densitati_conditionate, type = "l", col = "green", xlab = "Y", ylab = "Densitate condiționată a lui Y dat fiind X = x")
    })
}

# Rulează aplicația Shiny
shinyApp(ui, server)





#f
# Încărcare librării
library(shiny)
library(stats)
library(animate)

# Funcție de densitate de probabilitate - Exemplu: Distribuție normală unidimensională
densitate_probabilitate_unidimensionala <- function(x, mu, sigma) {
    dnorm(x, mean = mu, sd = sigma)
}

# Funcție de densitate de probabilitate - Exemplu: Distribuție normală bidimensională
densitate_probabilitate_bidimensionala <- function(x, y, mu_x, mu_y, sigma_x, sigma_y) {
    (1 / (2 * pi * sigma_x * sigma_y)) * exp(-0.5 * ((x - mu_x)^2 / sigma_x^2 + (y - mu_y)^2 / sigma_y^2))
}

# Funcție de repartiție - Exemplu: Repartiție normală unidimensională
functie_repartitie_unidimensionala <- function(x, mu, sigma) {
    pnorm(x, mean = mu, sd = sigma)
}

# Funcție de repartiție - Exemplu: Repartiție normală bidimensionă
functie_repartitie_bidimensionala <- function(x, y, mu_x, mu_y, sigma_x, sigma_y) {
    pnorm(x, mean = mu_x, sd = sigma_x) * pnorm(y, mean = mu_y, sd = sigma_y)
}

# Interfața Shiny
ui <- fluidPage(
    titlePanel("Reprezentarea grafică a densității și funcției de repartiție"),
    sidebarLayout(
        sidebarPanel(
            selectInput("dimensiune", "Dimensiune variabilă aleatoare:", c("Unidimensională", "Bidimensională")),
            numericInput("mu", "Medie (mu):", 0),
            numericInput("sigma", "Deviație standard (sigma):", 1),
            numericInput("mu_x", "Medie X:", 0),
            numericInput("mu_y", "Medie Y:", 0),
            numericInput("sigma_x", "Deviație standard X:", 1),
            numericInput("sigma_y", "Deviație standard Y:", 1),
            sliderInput("parametru", "Valoare parametru:", min = 0, max = 5, value = 2, step = 0.1),
            actionButton("reprezinta", "Reprezintă")
        ),
        mainPanel(
            plotOutput("plot_densitate"),
            plotOutput("plot_repartitie"),
            uiOutput("animatie")
        )
    )
)

# Server logic
server <- function(input, output) {
    output$plot_densitate <- renderPlot({
        parametru <- input$parametru
        if (input$dimensiune == "Unidimensională") {
            x_vals <- seq(-5, 5, length.out = 100)
            y_vals <- densitate_probabilitate_unidimensionala(x_vals, input$mu, input$sigma)
            plot(x_vals, y_vals, type = "l", col = "blue", xlab = "X", ylab = "Densitate de probabilitate")
            abline(v = parametru, col = "red", lty = 2)
        } else {
            x_vals <- seq(-5, 5, length.out = 100)
            y_vals <- seq(-5, 5, length.out = 100)
            z_vals <- matrix(0, nrow = length(x_vals), ncol = length(y_vals))
            for (i in 1:length(x_vals)) {
                for (j in 1:length(y_vals)) {
                    z_vals[i, j] <- densitate_probabilitate_bidimensionala(x_vals[i], y_vals[j], input$mu_x, input$mu_y, input$sigma_x, input$sigma_y)
                }
            }
            persp(x_vals, y_vals, z_vals, col = "lightblue", theta = 30, phi = 30, xlab = "X", ylab = "Y", zlab = "Densitate de probabilitate")
            lines(c(parametru, parametru), c(-5, 5), c(0, 0), col = "red", lty = 2)
        }
    })
    
    output$plot_repartitie <- renderPlot({
        parametru <- input$parametru
        if (input$dimensiune == "Unidimensională") {
            x_vals <- seq(-5, 5, length.out = 100)
            y_vals <- functie_repartitie_unidimensionala(x_vals, input$mu, input$sigma)
            plot(x_vals, y_vals, type = "l", col = "green", xlab = "X", ylab = "Funcție de repartiție")
            abline(v = parametru, col = "red", lty = 2)
        } else {
            x_vals <- seq(-5, 5, length.out = 100)
            y_vals <- seq(-5, 5, length.out = 100)
            z_vals <- matrix(0, nrow = length(x_vals), ncol = length(y_vals))
            for (i in 1:length(x_vals)) {
                for (j in 1:length(y_vals)) {
                    z_vals[i, j] <- functie_repartitie_bidimensionala(x_vals[i], y_vals[j], input$mu_x, input$mu_y, input$sigma_x, input$sigma_y)
                }
            }
            persp(x_vals, y_vals, z_vals, col = "lightgreen", theta = 30, phi = 30, xlab = "X", ylab = "Y", zlab = "Funcție de repartiție")
            lines(c(parametru, parametru), c(-5, 5), c(0, 0), col = "red", lty = 2)
        }
    })
    
    output$animatie <- renderUI({
        if (input$dimensiune == "Unidimensională") {
            sliderInput("parametru_animatie", "Valoare parametru (animație):", min = 0, max = 5, value = 2, step = 0.1)
        } else {
            sliderInput("parametru_animatie", "Valoare parametru (animație):", min = -5, max = 5, value = 0, step = 0.1)
        }
    })
    
    observeEvent(input$reprezinta, {
        parametre_animatie <- seq(0, input$parametru_animatie, length.out = 100)
        saveLatex({
            for (param in parametre_animatie) {
                if (input$dimensiune == "Unidimensională") {
                    x_vals <- seq(-5, 5, length.out = 100)
                    y_vals <- densitate_probabilitate_unidimensionala(x_vals, input$mu, input$sigma)
                    plot(x_vals, y_vals, type = "l", col = "blue", xlab = "X", ylab = "Densitate de probabilitate")
                    abline(v = param, col = "red", lty = 2)
                } else {
                    x_vals <- seq(-5, 5, length.out = 100)
                    y_vals <- seq(-5, 5, length.out = 100)
                    z_vals <- matrix(0, nrow = length(x_vals), ncol = length(y_vals))
                    for (i in 1:length(x_vals)) {
                        for (j in 1:length(y_vals)) {
                            z_vals[i, j] <- densitate_probabilitate_bidimensionala(x_vals[i], y_vals[j], input$mu_x, input$mu_y, input$sigma_x, input$sigma_y)
                        }
                    }
                    persp(x_vals, y_vals, z_vals, col = "lightblue", theta = 30, phi = 30, xlab = "X", ylab = "Y", zlab = "Densitate de probabilitate")
                    lines(c(param, param), c(-5, 5), c(0, 0), col = "red", lty = 2)
                }
                Sys.sleep(0.1)
            }
        }, interval = 0.1, movie.name = "reprezentare_animatie.tex", ani.width = 400, ani.height = 400)
    })
}

# Rulează aplicația Shiny
shinyApp(ui, server)




#g
library(shiny)

# Definirea funcției de densitate de probabilitate bidimensională f(x, y)
f <- function(x, y) {
    x + y
}

# UI
ui <- fluidPage(
    titlePanel("Calculul Momentelor pentru Variabilele Aleatoare Bidimensionale"),
    sidebarLayout(
        sidebarPanel(
            numericInput("xmin", "Valoare minimă pentru X:", value = 0, min = -Inf, max = Inf),
            numericInput("xmax", "Valoare maximă pentru X:", value = 1, min = -Inf, max = Inf),
            numericInput("ymin", "Valoare minimă pentru Y:", value = 0, min = -Inf, max = Inf),
            numericInput("ymax", "Valoare maximă pentru Y:", value = 1, min = -Inf, max = Inf),
            actionButton("calculeaza", "Calculează")
        ),
        mainPanel(
            verbatimTextOutput("rezultate")
        )
    )
)

# Server logic
server <- function(input, output) {
    observeEvent(input$calculeaza, {
        # Calculul mediei (momentului de ordin 1) pentru X și Y
        medie_x <- integrate(function(x) x * integrate(function(y) f(x, y), input$ymin, input$ymax)$value, input$xmin, input$xmax)$value
        medie_y <- integrate(function(y) y * integrate(function(x) f(x, y), input$xmin, input$xmax)$value, input$ymin, input$ymax)$value
        
        # Calculul dispersiei (momentului de ordin 2) pentru X și Y
        var_x <- integrate(function(x) (x - medie_x)^2 * integrate(function(y) f(x, y), input$ymin, input$ymax)$value, input$xmin, input$xmax)$value
        var_y <- integrate(function(y) (y - medie_y)^2 * integrate(function(x) f(x, y), input$xmin, input$xmax)$value, input$ymin, input$ymax)$value
        
        # Calculul momentelor initiale și centrate până la ordinul 4 (dacă există)
        moment_ord_3_x <- integrate(function(x) (x - medie_x)^3 * integrate(function(y) f(x, y), input$ymin, input$ymax)$value, input$xmin, input$xmax)$value
        moment_ord_3_y <- integrate(function(y) (y - medie_y)^3 * integrate(function(x) f(x, y), input$xmin, input$xmax)$value, input$ymin, input$ymax)$value
        
        moment_ord_4_x <- integrate(function(x) (x - medie_x)^4 * integrate(function(y) f(x, y), input$ymin, input$ymax)$value, input$xmin, input$xmax)$value
        moment_ord_4_y <- integrate(function(y) (y - medie_y)^4 * integrate(function(x) f(x, y), input$xmin, input$xmax)$value, input$ymin, input$ymax)$value
        
        # Afișarea rezultatelor sau mesajelor corespunzătoare dacă momentele nu există
        if (is.na(medie_x) || is.na(medie_y) || is.na(var_x) || is.na(var_y)) {
            output$rezultate <- renderPrint({
                "Densitatea comună nu este bine definită."
            })
        } else {
            output$rezultate <- renderPrint({
                paste(
                    "Media X:", medie_x, "\n",
                    "Media Y:", medie_y, "\n",
                    "Dispersia X:", var_x, "\n",
                    "Dispersia Y:", var_y, "\n",
                    "Momentul de ordin 3 pentru X:", moment_ord_3_x, "\n",
                    "Momentul de ordin 3 pentru Y:", moment_ord_3_y, "\n",
                    "Momentul de ordin 4 pentru X:", moment_ord_4_x, "\n",
                    "Momentul de ordin 4 pentru Y:", moment_ord_4_y, "\n"
                )
            })
        }
    })
}

# Rularea aplicației Shiny
shinyApp(ui, server)




#h
library(shiny)

# UI
ui <- fluidPage(
    titlePanel("Calculul Așteptării și Dispersiei pentru o Funcție Unidimensională"),
    sidebarLayout(
        sidebarPanel(
            textInput("g_expresie", "Introduceți funcția g(x):", "x^2"),
            actionButton("calculeaza", "Calculează")
        ),
        mainPanel(
            verbatimTextOutput("rezultate")
        )
    )
)

# Server logic
server <- function(input, output) {
    observeEvent(input$calculeaza, {
        # Convertirea expresiei într-o funcție
        g <- function(x) eval(parse(text = input$g_expresie))
        
        # Definirea densității marginale pentru X (pentru exemplu, am folosit o densitate normală standard)
        f_X <- function(x) {
            dnorm(x, mean = 0, sd = 1)
        }
        
        # Funcția pentru E[g(X)]
        E_gX <- function(x) {
            g(x) * f_X(x)
        }
        
        # Funcția pentru E[g(X)^2]
        E_gX2 <- function(x) {
            g(x)^2 * f_X(x)
        }
        
        # Calculul E[g(X)]
        integrate_E_gX <- integrate(E_gX, lower = -Inf, upper = Inf)
        E_gX_value <- integrate_E_gX$value
        
        # Calculul E[g(X)^2]
        integrate_E_gX2 <- integrate(E_gX2, lower = -Inf, upper = Inf)
        E_gX2_value <- integrate_E_gX2$value
        
        # Calculul dispersiei
        Var_gX <- E_gX2_value - E_gX_value^2
        
        # Afișarea rezultatelor
        output$rezultate <- renderPrint({
            paste(
                "E[g(X)]:", E_gX_value,
                "Var(g(X)):", Var_gX
            )
        })
    })
}

# Rularea aplicației Shiny
shinyApp(ui, server)


