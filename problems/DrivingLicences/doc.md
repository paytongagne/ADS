# Driving Licenses

The **DGT (Traffic Authority)** has requested our help in managing a **points-based driving license** system. Drivers are uniquely identified by their **DNI (National ID)**, and their point balance ranges from **0 to 15 points, inclusive**.  

The system must be implemented as an **Abstract Data Type (ADT)** with the following operations:  

## Operations
- **`nuevo(dni)`**: Adds a new driver identified by their `dni` (a string) with **15 points**.  
  - If the `dni` is already registered, it throws a **domain error** with the message **"Conductor duplicado"** (Duplicate driver).  

- **`quitar(dni, puntos)`**: Deducts `puntos` from a driver's balance due to an infraction.  
  - If the deducted points exceed the driver’s balance, they will be **set to 0**.  
  - If the driver does not exist, it throws a **domain error** with the message **"Conductor inexistente"** (Non-existent driver).  

- **`consultar(dni)`**: Returns the **current points** of a driver.  
  - If the driver does not exist, it throws a **domain error** with the message **"Conductor inexistente"**.  

- **`cuantos_con_puntos(puntos)`**: Returns the **number of drivers** who have exactly `puntos`.  
  - If the specified `puntos` is **not between 0 and 15**, it throws a **domain error** with the message **"Puntos no válidos"** (Invalid points).  

---

## Implementation Requirements
The operations should be **as efficient as possible**. Therefore, selecting an appropriate **data representation** for the ADT is crucial. The operations must be implemented efficiently, and their **complexity should be justified**.  

💡 **Important:**  
- **The ADT methods should not print anything to the screen.**  
- **Input and output handling should be done externally.**  

---

## Input Format 
The input consists of multiple test cases.  
Each test case contains a series of **operations**, one per line, formatted as:  
`operation_name argument(s)`  

- The keyword **"FIN"** in a line indicates the **end of a test case**.  

---

## Output Format
For each test case, the required output should be generated based on the operations:  

- **`consultar(dni)`**: Prints  
  ```
  Puntos de DNI: N  
  ```  
  where `DNI` is the driver's ID and `N` is their current points.  

- **`cuantos_con_puntos(puntos)`**: Prints  
  ```
  Con N puntos hay M  
  ```  
  where `N` is the queried points and `M` is the number of drivers with that exact point balance.  

- **Each test case should end with a line containing:**  
  ```
  ---  
  ```  

- **Error Handling:**  
  - If an operation encounters an error, print:  
    ```
    ERROR: error_message  
    ```  
  - No additional output should be produced for that operation.  


### Input 

```text
nuevo 123A
nuevo 456B
nuevo 666
cuantos_con_puntos 15
cuantos_con_puntos 0
quitar 666 15
cuantos_con_puntos 0
quitar 456B 9
consultar 456B
quitar 123A 10
cuantos_con_puntos 5
quitar 456B 1
cuantos_con_puntos 5
FIN
nuevo 123A
nuevo 123A
cuantos_con_puntos 20
quitar 456B 2
FIN
```

### Output
```
Con 15 puntos hay 3
Con 0 puntos hay 0
Con 0 puntos hay 1
Puntos de 456B: 6
Con 5 puntos hay 1
Con 5 puntos hay 2
---
ERROR: Conductor duplicado
ERROR: Puntos no validos
ERROR: Conductor inexistente
---
```