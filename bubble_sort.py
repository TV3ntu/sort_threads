import threading
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_with_threads(arr, num_threads):
    chunk_size = len(arr) // num_threads
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=bubble_sort, args=(arr,))
        threads.append(thread)

    start_time = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time

    return elapsed_time

def run_test(num_threads, num_elements):
    arr = [random.randint(1, 100000000) for _ in range(num_elements)]

    print(f"\nCon {num_threads} hilos y {num_elements} elementos:")
    # print("Lista desordenada:", arr) DESCOMENTAR PARA VER LISTA ORDENADA

    elapsed_time = sort_with_threads(arr, num_threads)

    # print("Lista ordenada:", arr) DESCOMENTAR PARA VER LISTA ORDENADA
    print(f"Tardó {elapsed_time:.4f} segundos\n")

    return num_threads, elapsed_time

def plot_graph(title, x_label, y_label, data):
    x, y = zip(*data)
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def main():
    element_count_5 = 100
    element_count_10 = 10000
    thread_counts = [1, 20, 40]
    results_5 = []
    results_10 = []

    # Pruebas con 5 elementos
    for num_threads in thread_counts:
        elapsed_time = run_test(num_threads, element_count_5)
        results_5.append(elapsed_time)

    # Gráfico para 5 elementos
    plot_graph("Bubble Sort con 100 elementos", "Cantidad de Hilos", "Tiempo (segundos)", results_5)

    # Pruebas con 10 elementos
    for num_threads in thread_counts:
        elapsed_time = run_test(num_threads, element_count_10)
        results_10.append(elapsed_time)

    # Gráfico para 10 elementos
    plot_graph("Bubble Sort con 10000 elementos", "Cantidad de Hilos", "Tiempo (segundos)", results_10)

if __name__ == "__main__":
    main()
import threading
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_with_threads(arr, num_threads):
    chunk_size = len(arr) // num_threads
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=bubble_sort, args=(arr,))
        threads.append(thread)

    start_time = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time

    return elapsed_time

def run_test(num_threads, num_elements):
    arr = [random.randint(1, 100000000) for _ in range(num_elements)]

    print(f"\nCon {num_threads} hilos y {num_elements} elementos:")
    # print("Lista desordenada:", arr) DESCOMENTAR PARA VER LISTA ORDENADA

    elapsed_time = sort_with_threads(arr, num_threads)

    # print("Lista ordenada:", arr) DESCOMENTAR PARA VER LISTA ORDENADA
    print(f"Tardó {elapsed_time:.4f} segundos\n")

    return num_threads, elapsed_time

def plot_graph(title, x_label, y_label, data):
    x, y = zip(*data)
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def main():
    element_count_5 = 100
    element_count_10 = 10000
    thread_counts = [1, 20, 40]
    results_5 = []
    results_10 = []

    # Pruebas con 5 elementos
    for num_threads in thread_counts:
        elapsed_time = run_test(num_threads, element_count_5)
        results_5.append(elapsed_time)

    # Gráfico para 5 elementos
    plot_graph("Bubble Sort con 100 elementos", "Cantidad de Hilos", "Tiempo (segundos)", results_5)

    # Pruebas con 10 elementos
    for num_threads in thread_counts:
        elapsed_time = run_test(num_threads, element_count_10)
        results_10.append(elapsed_time)

    # Gráfico para 10 elementos
    plot_graph("Bubble Sort con 10000 elementos", "Cantidad de Hilos", "Tiempo (segundos)", results_10)

if __name__ == "__main__":
    main()
