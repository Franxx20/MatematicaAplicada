import base64
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    lista=[]
    for row in matrix:
        lista+=row
        
  # sum itera sobre los elementos de su parametro izquierdo para ingresarlos en el derecho, que en este caso es una lista vacia sin nombre.
    # El resultado es luego enviado como parametro a la funcion bytes que transforma la lista en binario
    return bytes(sum(matrix,[]))

    

 
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(bytes2matrix(matrix))
# print(matrix2bytes(matrix))
