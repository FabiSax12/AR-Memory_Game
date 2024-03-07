import ARMem as ar
import random

players: dict = {}

def request_data():
  quantity_of_players = int(input("Cantidad de jugadores: "))

  while quantity_of_players <= 0:
    print("La cantidad de jugadores debe ser un número entero mayor a 0")
    quantity_of_players = int(input("Cantidad de jugadores: "))

  return quantity_of_players

def init_players(quantity: int = 1):
  i = 0
  while len(players.keys()) < quantity:
    new_player = (input(f"Nombre del jugador {i + 1}: "))
    players[new_player] = {
      "Nivel 1": [],
      "Nivel 2": [],
      "Nivel 3": [],
      "Tiempo Total": 0
    }
    i += 1
  print(players)

def generate_game(quantity: int):
  game = []

  while len(game) < quantity:
    random_number = random.randint(0, quantity - 1)
    
    if random_number not in game:
      game.append(random_number)

  return game

def main():
  quantity_of_players = request_data()
  init_players(quantity_of_players)
  game = generate_game(5)

  time = ar.start_sorting(game)

  print(time)

main()