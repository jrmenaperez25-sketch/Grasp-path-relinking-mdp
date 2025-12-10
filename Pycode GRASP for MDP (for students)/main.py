from structure import instance
from algorithms import grasp

def executeInstance(instances, num_executions, output_file):
    with open(output_file, "w") as file:
        for path in instances:
            # Encabezado de instancia
            file.write("========================================================\n")
            file.write(f"INSTANCIA: {path}\n")
            file.write("Ejecución | Mejor solución GRASP\n")
            file.write("--------------------------------------------------------\n")

        for i in range(1, num_executions + 1):
                inst = instance.readInstance(path)
                sol = grasp.execute(inst, 10, 0.75)

                # Guardamos el valor de la función objetivo
                file.write(f"{round(sol['of'], 2)} ")

        file.write("\n========================================================\n\n")

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
    output_file = "resultadosGRASP.txt"
    executeInstance(instances, num_executions, output_file)
