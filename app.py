import streamlit as st 
import random

st.title("Number Guessing Game")

if "secret_number" not in st.session_state:
  st.session_state.secret_number = random.randint(1,1000)

if "attempts" not in st.session_state:
  st.session_state.attempts = 0
  st.session_state.game_over = False

with st.form(key="game_form"):
  guess = st.number_input("Guess a number between 1 and 100:",min_value=1,max_value=1000,step=1)

  submit_button = st.form_submit_button(label="Submit Guess")

if submit_button:
  st.session_state.attempts +=1

  if guess == st.session_state.secret_number:
    st.success(f"COmgrates the secret number was{st.session_state.secret_number}. You WON in {st.session_state.attempts} attempts!")

  elif st.session_state.attempts >= 10:
    st.error(f"Game over! you are out of attempts. The correct number was {st.session_state.secret_number}.")

  elif guess > st.session_state.secret_number:
    st.info(f"{guess} is too high! Try a lower number.")
  
  else:
    st.info(f"{guess} is too low! Try a higher number.")


st.write("---")

if st.button("Restart Game & Clear Memory"):
  del st.session_state.secret_number
  del st.session_state.attempts

  st.rerun()