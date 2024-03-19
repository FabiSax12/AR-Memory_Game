"""
Fabian Vargas y Kenneth Araya

https://github.com/FabiSax12/AR-Memory_Game

"""

import ARMem as ar
import random
import time
import terminal

# Grabación de los datos de cada jugador, similar a una base de datos NoSQL.
# Cada jugador contiene los datos de su nombre de usuario, tiempo por nivel y tiempo total.
players: dict = {}
config: dict = {
  "time_sleep": 3,
  "image_set": "fruits"
}

# Sets de imagenes que están disponibles para usar
image_sets = {
  "fruits": ["Piña", "Cereza", "Uva", "Pera", "Guanabana"],
  "pc_components": ["CPU", "Gráfica", "RAM", "SSD", "Motherboard"]
}

def error_message(msj: str, duration: int):
  """
  Muestra un mensaje de error en la terminal y luego limpia la pantalla después de un cierto tiempo.

  Args:
      msj (str): El mensaje de error que se mostrará en la terminal.
      duration (int): La duración en segundos durante la cual se mostrará el mensaje de error antes de limpiar la pantalla.

  Returns:
      None
  """
  terminal.clear()
  terminal.color("Regular", "Red")
  print(msj)
  time.sleep(duration)

def request_data() -> dict:
  """
    Solicita al usuario toda la información necesaria para personalizar el juego.
  """
  terminal.clear()
  config["time_sleep"] = int(input("Tiempo para memorizar la secuencia (segundos): "))

  terminal.clear()
  print("Personaliza las imagenes para jugar...")
  print("1) Frutas")
  print("2) Componentes de PC")
  option = int(input("Set de imágenes: "))
  if option == 1: config["image_set"] = "fruits"
  elif option == 2: config["image_set"] = "pc_components"

def init_players():
  """
    Inicializa la estructura de datos de los jugadores.
  """
  terminal.clear()

  try:
    amount_of_players = int(input("Cantidad de jugadores: "))
  except:
    error_message("La cantidad de jugadores debe ser un número entero mayor a 0", 2)
    init_players()

  players.clear()
  for n in range(amount_of_players):
    if len(players.fromkeys(players)) > 0:
      print(f"Jugadores: {", ".join(players.fromkeys(players))}")
    else:
      print("Aún no hay jugadores")

    new_player = input(f"Nombre del jugador {n+1}: ")
    players[new_player] = {
      "Nivel 1": 0,
      "Nivel 2": 0,
      "Nivel 3": 0,
      "Tiempo Total": 0
    }
    terminal.clear_line(2)

def generate_game(amount: int) -> list:
  """Genera una secuencia de juego aleatoria.

  Args:
      amount (int): Longitud de la secuencia de juego.

  Returns:
      list: Secuencia de juego generada aleatoriamente.
  """

  game = []

  while len(game) < amount:
    random_number = random.randint(0, 4)
    
    if random_number not in game:
      game.append(random_number)

  return game

def ids_to_image_name(ids: list) -> list:
    """
    Convierte una lista de identificadores de imágenes en una lista de nombres de imágenes.

    Args:
        ids (list): Una lista de identificadores de imágenes.

    Returns:
        list: Una lista de nombres de imágenes correspondientes a los identificadores proporcionados.
    """
    image_names = []
    for id in ids:
        image_names.insert(id, image_sets[config["image_set"]][id])
    return image_names

def play_round(level: int, marks: int): 
  """Ejecuta una ronda del juego para cada jugador.

  Args:
      level (int): Nivel actual del juego.
      marks (int): Cantidad actual de marcas del juego.
  """

  for player in players.keys():
    game = generate_game(marks)
    game_names = ids_to_image_name(game)

    terminal.clear()
    terminal.color("Regular", "White")
    print(f"{player} memoriza lo siguiente:")
    
    terminal.color("Regular", "Green")
    print(game_names)
    
    terminal.color("Bold High Intensity", "Red")
    for countdown in range(config["time_sleep"], 0, -1):
      print(countdown)
      time.sleep(1)
      if countdown == 1: 
        terminal.clear_line(3)
      else:
        terminal.clear_line(1)
    # round_time = round(random.random() * 10, 2)
    round_time = round(ar.start_sorting(game, config["image_set"], flip_image=True, show_images=True), 2)
    players[player][f"Nivel {level}"] += round_time

  terminal.clear_line(1)

def level_report(level: int):
  """Genera un informe del nivel especificado.

  Args:
      level (int): Nivel del juego.
  """
  print(f"Reporte del nivel {level}")
  for player in players.keys():
    report = f"{player}: {players[player][f'Nivel {level}']} seg"
    print(report)

def play_level(level: int, marks: int):
  """Juega un nivel específico del juego.

  Args:
      level (int): Nivel del juego a jugar.
      marks (int): Cantidad de marcas del nivel.
  """

  if level == 1:
    terminal.color("Bold", "Green")
  elif level == 2:
    terminal.color("Bold", "Yellow")
  elif level == 3:
    terminal.color("Bold", "Red")
    
  print(f"Nivel {level}")

  for round in range(1, 6):
    terminal.color("Regular", "Cyan")
    print(f"Ronda {round}")
    play_round(level, marks)
  
  terminal.clear()
  level_report(level)
  input("Presiona 'ENTER' para continuar")
  terminal.clear()

def generate_ranking():
  """
    Genera un ranking de jugadores ordenado por el tiempo total acumulado en el juego.

    Returns:
        list: Una lista de tuplas ordenadas en función del tiempo total acumulado por cada jugador.
              Cada tupla contiene el nombre del jugador y su información asociada.
  """
  ranking = sorted(players.items(), key=lambda player: player[1]["Tiempo Total"])

  return ranking

def game_report():
  """Genera un informe completo del juego."""
  for player in players.keys():
    player_info = players[player]
    player_info["Tiempo Total"] = player_info["Nivel 1"] + player_info["Nivel 2"] + player_info["Nivel 3"]

  ranking = generate_ranking()
  print(f"Reporte de la partida")
  print("")

  for player in ranking:
    if ranking.index(player) == 0:
      terminal.color("Bold", "Green")
      print(f"Felicidades {player[0]}!! Has ganado con {player[1]['Tiempo Total']} seg")
      print("")
      terminal.color("Regular", "White")
    else:
      report = f"{ranking.index(player) + 1}. {player[0]}: {player[1]['Tiempo Total']} seg"
      print(report)

def start_game():
  """Inicia el juego, ejecutando los niveles del 1 al 3."""
  terminal.clear()
  for level in range(1, 4):
    play_level(level, level + 2)

def menu():
  """
    Muestra un menú interactivo con opciones para registrar jugadores, configurar la partida o iniciar la partida.
  """

  while True:
    terminal.clear()
    print("(1) Registrar jugadores")
    print("(2) Configurar partida")
    print("(3) Iniciar partida")
    option = int(input("Opción: "))

    if option == 1: init_players()
    elif option == 2: request_data()
    elif option == 3: break

def end_menu():
  """
    Muestra un menú de finalización con opciones para volver a jugar o salir del juego.
  """
  terminal.clear()
  print("(1) Volver a jugar")
  print("(2) Salir")

  option = int(input("Opción: "))

  if option == 1: main()
  elif option == 2:
    print("Gracias por jugar!!")
    return False

def main():
  """Función principal para ejecutar el juego."""
  terminal.clear()
  menu()
  if players != {}:
    start_game()
  else:
    error_message("Debe añadir al menos 1 jugador para iniciar la partida", 3)
    main()

  game_report()
  input("Presiona 'ENTER' para finalizar")
  end_menu()

main() 