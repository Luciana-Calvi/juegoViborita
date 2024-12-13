import turtle
import time
import random
 
pantalla = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.speed(1)
pantalla.title("Juego de la Viborita")
pantalla.bgcolor("purple")
pantalla.setup(width=700, height=700)
pantalla.tracer(0) 

jugador = pantalla.textinput("Nuevo jugador", "Ingresa tu nombre")


if not jugador:
    jugador = "Jugador1"
  
  
colores_disponibles = {"blue", "red", "orange"}
color_serpiente = None


while color_serpiente not in colores_disponibles:
   seleccion_color = pantalla.textinput(jugador+" selección de Color", f"Elige el color de tu serpiente:\n{', '.join(colores_disponibles)}")
   if seleccion_color:
       seleccion_color = seleccion_color.lower()
       if seleccion_color in colores_disponibles:
           color_serpiente = seleccion_color
       else:
           pantalla.textinput("Selección de Color", f"Color inválido. Por favor, elige uno de los siguientes:\n{', '.join(colores_disponibles)}")
   else:
       # Asignar un color por defecto si el usuario no ingresa nada
       color_serpiente = "blue"


# Dibujar el borde del escenario
dibujante = turtle.Turtle()
dibujante.speed(0)
dibujante.color("black")
dibujante.penup()
dibujante.goto(-250, -250)
dibujante.pendown()
dibujante.pensize(3)

# Dibuja el cuadrado del escenario
for _ in range(4):
   dibujante.forward(500)
   dibujante.left(90)

dibujante.hideturtle()

# Crear la serpiente en el centro
serpiente = turtle.Turtle()
serpiente.speed(0)  # Velocidad de animación de la tortuga
serpiente.shape("turtle")  # Forma de la serpiente
serpiente.color(color_serpiente)  # Color de la serpiente
serpiente.penup()  # Levantar el lápiz para no dibujar al moverse
serpiente.goto(0, 0)  # Posicionar la serpiente en el centro
serpiente.direction = "stop"  # Dirección inicial


# Lista para almacenar los segmentos de la serpiente
segmentos = []

# Dibujar la comida 
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
#comida.goto(0, 50)

    # Dibujar obstaculo
obstaculos = []

def posicion_dentro_borde():
    return random.randint(-240, 240)

def mostrarObstaculo():
    for _ in range(3):
        obstaculo = turtle.Turtle()
        obstaculo.speed(0)
        obstaculo.shape("triangle")
        obstaculo.color("black")
        obstaculo.penup()
        obstaculo.goto(posicion_dentro_borde(), posicion_dentro_borde())
        
        obstaculo.direction = random.choice(["up","down","left","right"])
        obstaculos.append(obstaculo)

def moverObstaculo():
    for obstaculo in obstaculos:
        if obstaculo.direction == "up":
            obstaculo.sety(obstaculo.ycor()+20)
        if obstaculo.direction == "down":
            obstaculo.sety(obstaculo.ycor()-20)
        if obstaculo.direction == "left":
            obstaculo.setx(obstaculo.xcor()-20)
        if obstaculo.direction == "right":
            obstaculo.setx(obstaculo.xcor()+20)

        # Envoltura de los bordes
        if obstaculo.xcor() > 240 or obstaculo.xcor() < -240 or obstaculo.ycor() > 240 or obstaculo.ycor() < -240:
            obstaculo.goto(posicion_dentro_borde(), posicion_dentro_borde())
            obstaculo.direction = random.choice(["up", "down", "left", "right"])

        # Cambiar dirección aleatoriamente
        if random.randint(1, 10) == 1:
            obstaculo.direction = random.choice(["up", "down", "left", "right"])

         
        
    pantalla.ontimer(moverObstaculo, 100)

def reiniciar_juego(x, y):
    global puntaje, toques
    toques += 1
    if toques > 3:
        pantalla.clearscreen()
        pantalla.setup(width=480, height=480)
        mensaje_perdido = turtle.Turtle()
        mensaje_perdido.hideturtle()
        mensaje_perdido.penup()
        mensaje_perdido.goto(0, 0)
        mensaje_perdido.write("¡Perdiste!", align="center", font=("Arial", 24, "normal"))
    else:
        puntaje += 1
        pantalla.clearscreen()  # Limpiar la pantalla
        pantalla.setup(width=550, height=550)  # Configurar el tamaño de la ventana nuevamente
        obstaculos.clear()  # Limpiar la lista de triángulos
        mostrarObstaculo()  # Crear nuevos triángulos
        moverObstaculo()  # Iniciar el movimiento de los triángulos
        
mostrarObstaculo()
moverObstaculo()
# Puntaje
puntaje = 0
puntaje_mas_alto = 0
nivel = 1
velocidad = 0.1

# Mostrar el puntaje y nombre del jugador
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Jugador: {jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_mas_alto}    Nivel: {nivel}", align= "center", font =("Arial", 16, "normal"))


# Crear segmentos iniciales de la serpiente
for i in range(1):
   nuevo_segmento = turtle.Turtle()
   nuevo_segmento.speed(0)
   nuevo_segmento.shape("turtle")
   nuevo_segmento.color(color_serpiente)
   nuevo_segmento.penup()
   nuevo_segmento.goto(-20 * (i + 1), 0)  # Posiciones alineadas horizontalmente
   
   segmentos.append(nuevo_segmento)

#Función para mover la serpiente
def mover():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x-20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x+20)

    # Envoltura de los bordes
    if serpiente.xcor() > 240:
        serpiente.setx(-240)
    elif serpiente.xcor() < -240:
        serpiente.setx(240)
    if serpiente.ycor() > 240:
        serpiente.sety(-240)
    elif serpiente.ycor() < -240:
        serpiente.sety(240) 

    for obstaculo in obstaculos:
        if serpiente.distance(obstaculo) < 20:
            reiniciar_juego()
    
#Función para actualizar el puntaje en la pantalla
def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_mas_alto}    Nivel: {nivel}", align= "center", font =("Arial", 16, "normal"))

#Función reiniciar el juego
def reiniciar_juego():
    global puntaje, puntaje_mas_alto, nivel, velocidad
    time.sleep(1)
    serpiente.goto(0,0)
    serpiente.direction = "stop"

    #Ocultar los segmentos
    for segmento in segmentos:
        segmento.goto(1000,1000)

    #Limpiar los segmentos
    segmentos.clear()

    #Resetearlo puntaje y nivel
    if puntaje > puntaje_mas_alto:
        puntaje_mas_alto = puntaje
    puntaje = 0
    nivel = 1
    velocidad = 0.1
    actualizar_puntaje()
   


#funciones para mover la tortuga
def arriba():
    if serpiente.direction != "down":
        serpiente.direction = "up"

def abajo():
    if serpiente.direction != "up":
        serpiente.direction = "down"

def derecha():
    if serpiente.direction != "left":
        serpiente.direction = "right"

def izquierda():
    if serpiente.direction != "right":
        serpiente.direction = "left"

#Asignar las teclas
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")


#Bucle principal del juego
while True:
    pantalla.update()

    #Guardar la posición actual antes de mover
    ultima_posicion = serpiente.position()

    mover()
   

    #Detectar colisión con la comida
    if serpiente.distance(comida) < 20:
        # Añadir un segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("turtle")
        nuevo_segmento.color(color_serpiente)
        nuevo_segmento.penup()

        # Colocar nuevo segmento al último de la serpiente
        if len(segmentos) > 0:
            ultimo_segmento = segmentos[-1]
            nuevo_segmento.goto(ultimo_segmento.position())
        else:
            nuevo_segmento.goto(ultima_posicion)
        
        segmentos.append(nuevo_segmento)

        # Mover la comida a una posición aleatoria
        while True:
            x = random.randint(-230,230)
            y = random.randint(-230,230)
            nueva_posicion = (x,y)

            #Verificamos que la nueva posicion de la comida no esté cerca de la serpiente
            distancia_serpiente = serpiente.distance(nueva_posicion)
            distancia_segmentos = all(segmento.distance(nueva_posicion) > 20 for segmento in segmentos)
            if distancia_serpiente > 20 and distancia_segmentos:
                comida.goto(x,y)
                break
        
        #Aumentar el puntaje
        puntaje += 10
        actualizar_puntaje()

        #Aumentar nivel
        if puntaje > 50:
            nivel += 1
            velocidad *= 0.9
            actualizar_puntaje()    

        # mover los segmentos en orden inverso
    for i in range(len(segmentos)-1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x,y)

    # mover el primer segmento
    if len(segmentos) > 0:
        x = ultima_posicion[0]
        y = ultima_posicion[1]
        segmentos[0].goto(x, y)     

    #Detectar colisiones con la serpiente 
    for segmento in segmentos:
        if segmento.distance(serpiente) < 20:
            reiniciar_juego()
            break


    time.sleep(velocidad) 
    tortuga.hideturtle()



