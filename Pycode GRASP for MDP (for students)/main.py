from structure import instance
from algorithms import grasp

def executeInstance(instances,num_executions, output_file):

    with open(output_file, "w") as file:
        for path in instances:
            #print(f"\nProcesando instancia: {path}")
            for i in range(1, num_executions + 1):
                #print(f"\nEjecución {i}:")

                # Iniciamos cronómetro
                #start_time = time.time()

                inst = instance.readInstance(path)
                sol = grasp.execute(inst, 10, 0.75)

                # Detenemos cronómetro
                #end_time = time.time()

                #print("\nBEST SOLUTION:")
                #solution.printSolution(sol)

                # Mostramos el tiempo transcurrido
                #elapsed = end_time - start_time
                #print(f"\nTiempo transcurrido: {elapsed:.2f} segundos")

                file.write(f"{round(sol['of'],2)} ")
if __name__ == '__main__':
    instances = [
        "instances/MDG-a_1_100_m10.txt",
        "instances/MDG-a_4_100_m10.txt",
        "instances/MDG-a_10_100_m10.txt",
        "instances/MDG-a_12_100_m10.txt",
        "instances/MDG-a_14_100_m10.txt",
        "instances/MDG-a_20_100_m10.txt",
        "instances/MDG-a_2_n500_m50.txt",
        "instances/MDG-a_5_n500_m50.txt",
        "instances/MDG-a_6_n500_m50.txt",
        "instances/MDG-a_9_n500_m50.txt",
        "instances/MDG-a_13_n500_m50.txt",
        "instances/MDG-a_16_n500_m50.txt",
        "instances/MDG-a_17_n500_m50.txt",
        "instances/MDG-a_19_n500_m50.txt",
        "instances/MDG-a_20_n500_m50.txt"
    ]
    num_executions = 2
    output_file = "resultados.txt"
    executeInstance(instances,num_executions, output_file)

