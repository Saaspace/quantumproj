import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from game import get_random_value,validate
import math
 

def main():
    menu=["Play","Instructions","About"]
    option = st.sidebar.selectbox("Menu",menu)

    if option=="Play":
        st.subheader('Quantum Play Begins')
        st.write("Computer ---> |0>")
        st.write("User ---> |1>")

        psi='∣ψ>'

        if 'board' not in st.session_state:
            st.session_state.board=np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves = [0,1,2,3,4,5,6,7,8,9]


        moves=st.selectbox("Make a move!",st.session_state.available_moves)

        if moves==1:
            if st.session_state.board[0,0]==psi:

                st.session_state.board[0,0]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)
        
        elif moves==2:
            if st.session_state.board[0,1]==psi:

                st.session_state.board[0,1]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        elif moves==3:
            if st.session_state.board[0,2]==psi:

                st.session_state.board[0,2]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==4:
            if st.session_state.board[1,0]==psi:

                st.session_state.board[1,0]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        elif moves==5:
            if st.session_state.board[1,1]==psi:

                st.session_state.board[1,1]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        elif moves==6:
            if st.session_state.board[1,2]==psi:

                st.session_state.board[1,2]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        elif moves==7:
            if st.session_state.board[2,0]==psi:

                st.session_state.board[2,0]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        elif moves==8:
            if st.session_state.board[2,1]==psi:

                st.session_state.board[2,1]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

        else:
            if st.session_state.board[2,2]==psi:

                st.session_state.board[2,2]=get_random_value()


                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list()
                    return 0



                comp_square=np.random.randint(1,9)
                col=(comp_square-1)%3
                row=math.floor((comp_square-1)/3)
                comp_value= get_random_value()
                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=comp_value
                
                
                comp_flag=validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("computer's move: ",comp_square)
                st.write("Computer's value: ",comp_value)
                st.dataframe(st.session_state.board)
            
            else:
                st.dataframe(st.session_state.board)

    elif option=="Instructions":
        st.subheader("Instructions")
        psi = '∣ψ>'
        board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
        st.write("Board:")
        st.dataframe(board)
        instruction_1 ="""
        The above board represents the initial state of the game.
        
        ∣ψ represents the superposition state!
        
        Always the user is given the chance to make the move first.
        |0> and |1> represents the piece chosen by the computer and the user respectively.

        However, unlike the classical tic tac toe , there is not a 100% probability that 
        when the computer/user makes the move,it,will result into their respective move.
        
        For eg, if user selects a piece, it's actually possible that the piece take the value of |0> or |1>.
        
        This is the Quantumeffect og Quantum superposition in the quantum tic tac toe.
        
        The squares in the 3*3 grid boards are numbered in the following manner as below.
        """
        st.write(instruction_1)
        board_numbering=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
        st.dataframe(board_numbering)

        instruction_2="""
        The user can select any space from the 3*3 grid using the selection menu as shown below 
        and press the submit button.
        
        """
        st.write(instruction_2)

    else:
        st.subheader("About")
        #Add Image
        img=Image.open(r'C:\Users\saapr\Downloads\download.jpg')
        st.image(img)
        about="""
        Create by Saahil Pradhan , Rushil Sunil Kharate , Livya Falodia , Anjali Kumari
        
        Created using: Python,Qiskit,StreamLit

        The game is build to help  us understand the Quantum superposition in a fun way.

        The Equation given down displays the mathematical form of Quantum superposition.
        """

        st.write(about)
        st.markdown(r'''
                    $|\psi$> = $\alpha$ |0 + $\beta$ |1>
                    ''')
        st.write('here,')
        st.markdown(r'''
                    $|\psi$> = Superposition state

                    |0> = Zero Ket = $$\begin{bmatrix}1 \\
                                        0
                                        \end{bmatrix}$$
                    
                    |1> = Zero Ket = $$\begin{bmatrix}0 \\
                                        1
                                        \end{bmatrix}$$
                    
                    After a measurement, superposition collapses into either of the basis states (|0> or |1>).

                    Probability of $|psi>$ collapsingto |0> = $|\alpha| ^ 2$

                    Probability of $|psi>$ collapsingto |1> = $|\beta| ^ 2$

                    $|\alpha| ^ 2$ + $|\beta| ^ 2$ = 1
                    ''')


if __name__=='__main__':
    condition=main()
    if condition==0:
        st.subheader('Game Over!')
    