import json
import time
import numpy as np
from find_car_by_id import find_car_by_id

class CacheClient:
    def __init__(self):
        self.total_time = 0.0  # Inicializamos el tiempo total en 0.0 segundos

    def get(self, key, simulated=False):
        start_time = time.time()  # Inicio del temporizador

        # Simulamos un retraso aletorio de 1 a 3 segundos, con una distribución normal en 2
        delay = np.random.normal(2, 0.5)

        if not simulated:
            time.sleep(delay)

        # Buscar en el JSON
        value = find_car_by_id(int(key))
        value = str(value)
        if value:
            print("Key found in JSON.")
                
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            if simulated:
                # Agregamos el delay al tiempo total
                elapsed_time += delay
            self.total_time += elapsed_time  # Sumamos el tiempo transcurrido al tiempo total
            print(f"Time taken (JSON + delay): {elapsed_time:.5f} seconds")
                
            return value
        else:
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            print(f"Time taken: {elapsed_time:.5f} seconds")
            print("Key not found.")
            return None
            
    def simulate_searches(self, n_searches=100):
        keys_to_search = [f"{i}" for i in np.random.randint(1, 101, n_searches)]
        
        for key in keys_to_search:
            print("\033[H\033[J")
            print(f"Searching : {key}/{n_searches}")
            self.get(key)

if __name__ == '__main__':
    client = CacheClient()

    while True:
        print("\nChoose an operation:")
        print("1. Get")
        print("2. Simulate Searches")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = client.get(key)
            if value is not None:
                print(f"Value: {value}")
        elif choice == "2":
            n_searches = int(input("Enter the number of searches you want to simulate: "))
            client.simulate_searches(n_searches)
            print(f"Total time taken for {n_searches} searches: {client.total_time:.5f} seconds")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
