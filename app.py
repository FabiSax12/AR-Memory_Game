import ARMem as ar
import random
import time
import terminal

# Grabación de los datos de cada jugador, similar a una base de datos NoSQL.
# Cada jugador contiene los datos de su nombre de usuario, tiempo por nivel y tiempo total.
players: dict = {}
config: dict = {
  "time_sleep": 0
}

def request_data() -> dict:
  """Solicita al usuario toda la información necesaria para personalizar el juego.

  Returns:
      dict: Toda la información obtenida del usuario.
  """
  amount_of_players = int(input("Cantidad de jugadores: "))

  while amount_of_players <= 0:
    print("La cantidad de jugadores debe ser un número entero mayor a 0")
    amount_of_players = int(input("Cantidad de jugadores: "))

  config["time_sleep"] = int(input("Tiempo para memorizar la secuencia (segundos): "))

  return amount_of_players

def init_players(amount: int = 1):
  """Inicializa la estructura de datos de los jugadores.

  Args:
      amount (int, opcional): Número de jugadores. Por defecto es 1.
  """
  for n in range(amount):
    new_player = input(f"Nombre del jugador {n+1}: ")
    players[new_player] = {
      "Nivel 1": 0,
      "Nivel 2": 0,
      "Nivel 3": 0,
      "Tiempo Total": 0
    }

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

def play_round(level: int, marks: int): 
  """Ejecuta una ronda del juego para cada jugador.

  Args:
      level (int): Nivel actual del juego.
      marks (int): Cantidad actual de marcas del juego.
  """


  for player in players.keys():
    game = generate_game(marks)

    terminal.color("Regular", "White")
    print(f"{player} memoriza lo siguiente:")
    
    terminal.color("Regular", "Green")
    print(game)
    
    terminal.color("Bold High Intensity", "Red")
    for countdown in range(config["time_sleep"], 0, -1):
      print(countdown)
      time.sleep(1)
      if countdown == 1: 
        terminal.clear_line(3)
      else:
        terminal.clear_line(1)
    
    # round_time = round(ar.start_sorting(game,flip_image=False, show_images=True), 2)
    round_time = round(random.random() * 10)
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
  
  level_report(level)
  terminal.clear()

def game_report():
  """Genera un informe completo del juego."""
  print(f"Reporte de la partida")
  for player in players.keys():
    player_info = players[player]
    player_info["Tiempo Total"] = player_info["Nivel 1"] + player_info["Nivel 2"] + player_info["Nivel 3"]

    report = f"{player}: {player_info['Tiempo Total']} seg"
    print(report)

def main():
  """Función principal para ejecutar el juego."""
  terminal.clear()

  amount_of_players = request_data()
  init_players(amount_of_players)
  
  terminal.clear()
  # Inicio del juego

  for level in range(1, 4):
    play_level(level, level + 2)
  
  game_report()

main()