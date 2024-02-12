from qiskit import QuantumCircuit,Aer
import numpy as np
import streamlit as st

def quantum_superposition():
    
    circuit = QuantumCircuit(1,1)

    circuit.h(0)

    circuit.measure(0,0)

    simulator = Aer.get_backend('aer_simulator')

    result = simulator.run(circuit).result().get_counts()

    return result

def get_random_value():
    res=quantum_superposition()
    values = list(res.values())
    keys=list(res.keys())
    random_value='|'+str(keys[np.argmax(values)])+'>'
    return random_value

def validate(arr):
    """
    The method checks if the game is finished,
    Parametes:
    arr(numpy array) : The array serves as the board
    Returns:
    returns 0 is any ofthe winning condition is satisfied by any of the player
    else returns 1
    """

    #define a boolean variable
    flag = True
    zero_ket='|0>'
    one_ket='|1>'
    #checks for the principal diagonal elements condition w.r.t user
    if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success("User has won!")
        flag = False
    #checks for the principal diagonal elements condition w.r.t computer
    if arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success("Computer has won!")
        flag= False
    #checks for the principal diagonal elements condition w.r.t user
    if arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success("User has won!")
        flag =False
    #checks for the principal diagonal elements condition w.r.t computer
    if arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success("Computer has won!")
        flag =False

    if not flag:
        return 0
    
    #we executed the below for loops if any of the above conditions are notsatisfied
    if flag:
        #checks if any of the row conqured by user
        for index in [0,1,2]:
            if(list(arr[index])==[one_ket,one_ket,one_ket]):
                st.success("User has won!")
                return 0
        #checks if any of the row conqured by computer
        for index in [0,1,2]:
            if(list(arr[index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer has won!")
                return 0
        #checks if any of the row conqured by user
        for index in [0,1,2]:
            if(list(arr[:,index])==[one_ket,one_ket,one_ket]):
                st.success("User has won!")
                return 0
        #checks if any of the row conqured by computer
        for index in [0,1,2]:
            if(list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer has won!")
                return 0
        #check if it is draw
        if '∣ψ>' not in arr:
            st.write("It is a draw")
            return 0
    #if none of the conditions are satisfies , 1 is returned 
    return 1
            
    