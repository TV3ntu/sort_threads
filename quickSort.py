import random
import threading
import time
import sys
import matplotlib.pyplot as plt

lengthLista = 1000000
sys.setrecursionlimit(lengthLista)

def parallel_quick_sort(arr, num_threads):
    if len(arr) <= 1:
        return arr

    # Divide la lista en subconjuntos
    chunk_size = len(arr) // num_threads
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Crea hilos para ordenar cada subconjunto
    threads = []
    sorted_chunks = [None] * num_threads
    for i in range(num_threads):
        thread = threading.Thread(target=lambda i=i: sorted_chunks.__setitem__(i, quick_sort(chunks[i])))
        threads.append(thread)
        thread.start()

    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Combina los subconjuntos ordenados
    sorted_list = []
    for chunk in sorted_chunks:
        sorted_list += chunk

    return sorted_list

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

hilos = [1, 5, 10, 15, 20, 25, 30, 35, 40]
tiempos = []

print(f"Ordena lista de {lengthLista} elementos")

for cantHilos in hilos:
    inicio_tiempo = time.time()

    parallel_quick_sort([random.randint(1, 1000) for _ in range(lengthLista)], cantHilos)

    tiempoFinal = round(time.time() - inicio_tiempo, 3)

    tiempos.append(tiempoFinal)

    print(f"Tiempo de ejecución con {cantHilos} thread: {tiempoFinal} segundos")

plt.plot(hilos, tiempos, marker='o')
plt.title(f'Quick sort en un arreglo de {lengthLista} elementos')
plt.xlabel('Cantidad de hilos')
plt.ylabel('Segundos')
plt.xticks(hilos)
plt.grid(True)
plt.show()