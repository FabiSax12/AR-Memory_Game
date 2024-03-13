import ARMem as ar
import random
import time

# (level, marks)
levels = [(1, 3), (2, 4), (3, 5)]

# Recording of each player's data, like a NoSQL database.
# Each player contains the data of his username, time per level and total time.
players: dict = {}

# Game functions
def request_data() -> dict:
  """Prompt the user for all necessary information to customize the game.

    Returns:
        dict: All information obtained from the user.
  """
  amount_of_players = int(input("Cantidad de jugadores: "))

  while amount_of_players <= 0:
    print("La cantidad de jugadores debe ser un número entero mayor a 0")
    amount_of_players = int(input("Cantidad de jugadores: "))

  return amount_of_players

def init_players(amount: int = 1):
  """Initialize player data structure.

    Args:
        amount (int, optional): Number of players. Defaults to 1.
  """
  
  for n in range(amount):
    new_player = (input(f"Nombre del jugador {n+1}: "))
    players[new_player] = {
      "Nivel 1": 0,
      "Nivel 2": 0,
      "Nivel 3": 0,
      "Tiempo Total": 0
    }

def generate_game(amount: int):
  """Generate a random game sequence.

    Args:
        amount (int): Length of the game sequence.

    Returns:
        list: Randomly generated game sequence.
  """

  game = []

  while len(game) < amount:
    random_number = random.randint(0, 4)
    
    if random_number not in game:
      game.append(random_number)

  return game

def play_round(lvl: int): 
  """Execute a round of the game for each player.

    Args:
        level (int): Current level of the game.
  """

  for player in players.keys():
    game = generate_game(lvl[1])
    print(f"{player} memoriza lo siguiente: {game}")
    # time.sleep(2)
    # round_time = round(ar.start_sorting(game,flip_image=False, show_images=True), 2)
    round_time = round(random.random() * 10)
    # time.sleep(round_time)
    players[player][f"Nivel {lvl[0]}"] += round_time

def level_report(lvl):
  print(f"Reporte del nivel {lvl}")
  for player in players.keys():
    report = f"{player} {players[player][f"Nivel {lvl}"]} seg"
    print(report)

def play_level(level: int):
  """Play a specific level of the game.

    Args:
        level (int): Level of the game to play.
  """
  print(f"Nivel {level[0]}")

  for x in range(5):
    print(f"Ronda {x + 1}")
    play_round(level)
  
  level_report(level[0])

def main():
  """
    Main function to run the game.
  """
  amount_of_players = request_data()
  init_players(amount_of_players)
  
  for lvl in levels:
    play_level(lvl)

main()