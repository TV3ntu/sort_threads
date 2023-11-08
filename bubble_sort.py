import threading
import random
import time
import matplotlib.pyplot as plt
import psutil


def bubblesort(arr, num_threads=1):
    n = len(arr)
    chunk_size = n // num_threads
    threads = []

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < num_threads - 1 else n
        thread = threading.Thread(target=bubblesort_part, args=(arr, start_index, end_index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Merge de las partes ordenadas
    return merge(arr, num_threads)


def bubblesort_part(arr, start, end):
    for i in range(start, end):
        for j in range(start, end - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge(arr, num_threads):
    n = len(arr)
    merged_arr = [0] * n

    # Dividir el arreglo en partes ordenadas por los threads
    chunk_size = n // num_threads
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads)]

    # Inicializar índices para cada chunk
    indices = [0] * num_threads

    # Combinar las partes ordenadas
    for i in range(n):
        min_val = float('inf')
        min_index = -1

        for j in range(num_threads):
            if indices[j] < len(chunks[j]) and chunks[j][indices[j]] < min_val:
                min_val = chunks[j][indices[j]]
                min_index = j

        indices[min_index] += 1
        merged_arr[i] = min_val

    return merged_arr


def run_comparison_bubble(arr_size, num_threads):
    data = [random.randint(1, 1000) for _ in range(arr_size)]

    # Iniciar el monitoreo de recursos
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    initial_cpu = process.cpu_percent()

    start_time = time.time()
    bubblesort(data.copy(), num_threads)
    end_time = time.time()

    # Finalizar el monitoreo de recursos
    final_memory = process.memory_info().rss
    final_cpu = process.cpu_percent()

    # Retornar el tiempo de ejecución y el uso de recursos
    return end_time - start_time, final_memory - initial_memory, final_cpu - initial_cpu


if __name__ == '__main__':
    sizes = [10, 100, 1000, 10000]
    thread_options = [1, 2, 4, 8]

    # Crear el gráfico con tamaño personalizado
    plt.figure(figsize=(12, 8))

    for threads in thread_options:
        times_with_threads_bubble = []
        memory_usage_with_threads_bubble = []
        cpu_usage_with_threads_bubble = []

        for size in sizes:
            time_with_threads, memory_with_threads, cpu_with_threads = run_comparison_bubble(size, threads)
            times_with_threads_bubble.append(time_with_threads)
            memory_usage_with_threads_bubble.append(memory_with_threads)
            cpu_usage_with_threads_bubble.append(cpu_with_threads)

        # Graficar el tiempo de ejecución para Bubble Sort
        plt.subplot(2, 1, 1)
        plt.plot(sizes, times_with_threads_bubble, label=f'Con {threads} Threads')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.title('Comparación de Bubble Sort con Diferentes Cantidades de Threads')
        plt.legend()

        # Graficar el uso de memoria para Bubble Sort
        plt.subplot(2, 1, 2)
        plt.plot(sizes, memory_usage_with_threads_bubble, label=f'Con {threads} Threads', marker='o')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Uso de Memoria (bytes)')
        plt.title('Uso de Memoria con Diferentes Cantidades de Threads')
        plt.legend()

    plt.tight_layout()
    plt.show()
