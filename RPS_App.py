import streamlit as st
import random as rd
import time as tm

winner = 0

st.set_page_config('Rock Paper Scissor', layout='centered',
                   initial_sidebar_state='collapsed')

# st.header('<h1>Rock Paper Scissor</h1>')
st.markdown('<center><h1>Rock Paper Scissor</h1></center><hr>',
            unsafe_allow_html=True)


def get_name():
    '''This will get the name of the user'''
    user = st.text_input("Enter your name : ", key='input1',).capitalize()
    if user:
        st.success(f"Welcome {user} !!!")
    return user


def get_symbol(user):
    '''This will select the choice of the user'''
    symbols = {
        '1': "Rock",
        '2': "Paper",
        '3': "Scissor"
    }

    if user:
        st.markdown('''<center>Choose the symbol: <br>
        🪨  -   1<br>
        📄 -   2<br>
        ✂️  -   3
        </center>''', unsafe_allow_html=True)

    choice = st.text_input('Enter the choice: ', key='input2')
    if choice:
        symbol = [y for x, y in symbols.items() if x == choice]
        return str(symbol[0])


def computers_choice():
    '''This will get the Computers choice'''
    choices = ["Rock", "Paper", "Scissor"]
    Computer_choice = rd.choice(choices)
    return Computer_choice


def main():

    user = get_name()
    your_turn = get_symbol(user)

    if your_turn:
        st.markdown(
            f"<center><b>You have chosen {your_turn}.</b></center>", unsafe_allow_html=True)

    computers_turn = computers_choice()

    if computers_turn and your_turn:
        st.markdown(
            f"<center><b>Computer has chosen {computers_turn}.</b></center>", unsafe_allow_html=True)

    if (your_turn == computers_turn):
        st.warning('Match got tied. Try again.')
        winner = 0
    else:
        if (your_turn == "Rock"):
            if (computers_turn == "Paper"):
                st.error('Sorry you lost 🙁.')
                winner = 2

            else:
                st.success('Hurray! you won 😀.')
                st.balloons()
                winner = 1

        elif (your_turn == "Paper"):
            if (computers_turn == "Scissor"):
                st.error('Sorry you lost 🙁.')
                winner = 2

            else:
                st.success('Hurray! you won 😀.')
                st.balloons()
                winner = 1

        elif (your_turn == "Scissor"):
            if (computers_turn == "Rock"):
                st.error('Sorry you lost 🙁.')
                winner = 2

            else:
                st.success('Hurray! you won 😀.')
                st.balloons()
                winner = 1


main()
