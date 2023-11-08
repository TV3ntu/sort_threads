import threading
import random
import time
import matplotlib.pyplot as plt
import psutil


def mergesort(arr, num_threads=1):
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos partes
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    if num_threads > 1:
        # Divide el trabajo en dos subprocesos
        left_thread = threading.Thread(target=mergesort, args=(left, num_threads // 2))
        right_thread = threading.Thread(target=mergesort, args=(right, num_threads // 2))

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()

        return merge(left, right)
    else:
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def run_comparison_merge(arr_size, num_threads):
    data = [random.randint(1, 1000) for _ in range(arr_size)]

    # Iniciar el monitoreo de recursos
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    initial_cpu = process.cpu_percent()

    start_time = time.time()
    mergesort(data.copy(), num_threads)
    end_time = time.time()

    # Finalizar el monitoreo de recursos
    final_memory = process.memory_info().rss
    final_cpu = process.cpu_percent()

    # Retornar el tiempo de ejecución y el uso de recursos
    return end_time - start_time, final_memory - initial_memory, final_cpu - initial_cpu


if __name__ == '__main__':
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    thread_options = [1, 2, 4, 8]

    # Crear el gráfico con tamaño personalizado
    plt.figure(figsize=(12, 8))

    for threads in thread_options:
        times_with_threads_merge = []
        memory_usage_with_threads_merge = []
        cpu_usage_with_threads_merge = []

        for size in sizes:
            time_with_threads, memory_with_threads, cpu_with_threads = run_comparison_merge(size, threads)
            times_with_threads_merge.append(time_with_threads)
            memory_usage_with_threads_merge.append(memory_with_threads)
            cpu_usage_with_threads_merge.append(cpu_with_threads)

        # Graficar el tiempo de ejecución para Merge Sort
        plt.subplot(2, 1, 1)
        plt.plot(sizes, times_with_threads_merge, label=f'Con {threads} Threads')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.title('Comparación de Merge Sort con Diferentes Cantidades de Threads')
        plt.legend()

        # Graficar el uso de memoria para Merge Sort
        plt.subplot(2, 1, 2)
        plt.plot(sizes, memory_usage_with_threads_merge, label=f'Con {threads} Threads', marker='o')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Uso de Memoria (bytes)')
        plt.title('Uso de Memoria con Diferentes Cantidades de Threads')
        plt.legend()

    plt.tight_layout()
    plt.show()
