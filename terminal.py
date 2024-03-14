color_codes = {
  "Regular": {
    "Black": "\033[0;30m",
    "Red": "\033[0;31m",
    "Green": "\033[0;32m",
    "Yellow": "\033[0;33m",
    "Blue": "\033[0;34m",
    "Purple": "\033[0;35m",
    "Cyan": "\033[0;36m",
    "White": "\033[0;37m"
  },
  "Bold": {
    "Black": "\033[1;30m",
    "Red": "\033[1;31m",
    "Green": "\033[1;32m",
    "Yellow": "\033[1;33m",
    "Blue": "\033[1;34m",
    "Purple": "\033[1;35m",
    "Cyan": "\033[1;36m",
    "White": "\033[1;37m"
  },
  "Underline": {
    "Black": "\033[4;30m",
    "Red": "\033[4;31m",
    "Green": "\033[4;32m",
    "Yellow": "\033[4;33m",
    "Blue": "\033[4;34m",
    "Purple": "\033[4;35m",
    "Cyan": "\033[4;36m",
    "White": "\033[4;37m"
  },
  "Background": {
    "Black": "\033[40m",
    "Red": "\033[41m",
    "Green": "\033[42m",
    "Yellow": "\033[43m",
    "Blue": "\033[44m",
    "Purple": "\033[45m",
    "Cyan": "\033[46m",
    "White": "\033[47m"
  },
  "High Intensity": {
    "Black": "\033[0;90m",
    "Red": "\033[0;91m",
    "Green": "\033[0;92m",
    "Yellow": "\033[0;93m",
    "Blue": "\033[0;94m",
    "Purple": "\033[0;95m",
    "Cyan": "\033[0;96m",
    "White": "\033[0;97m"
  },
  "Bold High Intensity": {
    "Black": "\033[1;90m",
    "Red": "\033[1;91m",
    "Green": "\033[1;92m",
    "Yellow": "\033[1;93m",
    "Blue": "\033[1;94m",
    "Purple": "\033[1;95m",
    "Cyan": "\033[1;96m",
    "White": "\033[1;97m"
  },
  "High Intensity backgrounds": {
    "Black": "\033[0;100m",
    "Red": "\033[0;101m",
    "Green": "\033[0;102m",
    "Yellow": "\033[0;103m",
    "Blue": "\033[0;104m",
    "Purple": "\033[0;105m",
    "Cyan": "\033[0;106m",
    "White": "\033[0;107m"
  }
}

def color(type: str, color: str):
  """Imprime texto en la terminal con diferentes estilos y colores.

    Args:
        type (str): El tipo de estilo de texto a aplicar.
        color (str): El color del texto.

    Raises:
        ValueError: Si el tipo o el color especificados no son válidos.
  """
  types = ["Regular", "Bold", "Underline", "Background", "High Intensity", "Bold High Intensity", "High Intensity backgrounds"]
  colors = ["Black", "Red", "Green", "Yellow", "Blue", "Purple", "Cyan", "White"]

  if type not in types:
    raise ValueError(f"El parámetro 'type' debe ser uno de los siguientes: {', '.join(types)}")
  if color not in colors:
    raise ValueError(f"El parámetro 'color' debe ser uno de los siguientes: {', '.join(colors)}")

  print(color_codes[type][color])
  clear_line(1)

def clear_line(amount: int):
  """ Borra un número específico de líneas en la terminal.

    Args:
        amount (int): La cantidad de líneas que se desea borrar.
  """
  for x in range(amount):
    print("\033[F\033[K\033[F")

def clear():
  """ Limpia toda la terminal, dejándola en blanco. """
  print("\033c")