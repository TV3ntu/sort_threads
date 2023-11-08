import threading
import random
import time
import matplotlib.pyplot as plt
import psutil


def quicksort(arr, num_threads=1):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    if num_threads > 1:
        # Divide el trabajo en num_threads subprocesos
        threads = []
        chunk_size = len(left) // num_threads

        for i in range(num_threads):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size if i < num_threads - 1 else len(left)
            thread = threading.Thread(target=quicksort, args=(left[start_index:end_index],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return left + middle + right
    else:
        return quicksort(left) + middle + quicksort(right)


def run_comparison_quick(size, num_threads):
    data = [random.randint(1, 1000) for _ in range(size)]

    # Iniciar el monitoreo de recursos
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    initial_cpu = process.cpu_percent()

    start_time = time.time()
    quicksort(data.copy(), num_threads)
    end_time = time.time()

    # Finalizar el monitoreo de recursos
    final_memory = process.memory_info().rss
    final_cpu = process.cpu_percent()

    # Retornar el tiempo de ejecución y el uso de recursos
    return end_time - start_time, final_memory - initial_memory, final_cpu - initial_cpu


if __name__ == '__main__':
    sizes = [10000, 100000, 1000000, 10000000]
    thread_options = [1, 2, 4, 8]

    # Crear el gráfico con tamaño personalizado
    plt.figure(figsize=(12, 8))

    for threads in thread_options:
        times_with_threads = []
        memory_usage_with_threads = []
        cpu_usage_with_threads = []

        for size in sizes:
            time_with_threads, memory_with_threads, cpu_with_threads = run_comparison_quick(size, threads)
            times_with_threads.append(time_with_threads)
            memory_usage_with_threads.append(memory_with_threads)
            cpu_usage_with_threads.append(cpu_with_threads)

        # Graficar el tiempo de ejecución
        plt.subplot(2, 1, 1)
        plt.plot(sizes, times_with_threads, label=f'Con {threads} Threads')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.title('Comparación de Quick Sort con Diferentes Cantidades de Threads')
        plt.legend()

        # Graficar el uso de memoria
        plt.subplot(2, 1, 2)
        plt.plot(sizes, memory_usage_with_threads, label=f'Con {threads} Threads', marker='o')
        plt.xlabel('Tamaño de la Lista')
        plt.ylabel('Uso de Memoria (bytes)')
        plt.title('Uso de Memoria con Diferentes Cantidades de Threads')
        plt.legend()

    plt.tight_layout()
    plt.show()
