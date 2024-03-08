import ARMem as ar
import random
import time

# (level, difficulty)
levels = [(1, 3), (2, 4), (3, 5)]
players: dict = {}

def request_data():
  amount_of_players = int(input("Cantidad de jugadores: "))

  while amount_of_players <= 0:
    print("La cantidad de jugadores debe ser un número entero mayor a 0")
    amount_of_players = int(input("Cantidad de jugadores: "))

  return amount_of_players

def init_players(amount: int = 1):
  i = 0
  while len(players.keys()) < amount:
    new_player = (input(f"Nombre del jugador {i + 1}: "))
    players[new_player] = {
      "Nivel 1": [],
      "Nivel 2": [],
      "Nivel 3": [],
      "Tiempo Total": 0
    }
    i += 1
  print(players)

def generate_game(amount: int):
  game = []

  while len(game) < amount:
    random_number = random.randint(0, amount - 1)
    
    if random_number not in game:
      game.append(random_number)

  return game

def round(lvl: int):
  for player in players.keys():
    game = generate_game(levels[lvl - 1][1])
    print(f"{player} memoriza lo siguiente: {game}")
    time.sleep(2)
    round_time = round(ar.start_sorting(game,flip_image=False, show_images=True), 2)
    players[player][lvl].append(round_time)

def play_level(level: int):
  for x in range(4):
    round(level)
  
def main():
  amount_of_players = request_data()
  init_players(amount_of_players)
  
  for lvl in levels:
    play_level(lvl)

  print(players)

main()