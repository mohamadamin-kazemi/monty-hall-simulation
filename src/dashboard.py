"""
Streamlit Interface for Monty Hall Simulation
=============================================

This module provides an interactive web interface using Streamlit to visualize
the Monty Hall problem simulations dynamically over time.
"""

import time

import streamlit as st
from src.monty_hall import simulate_games


def main() -> None:
    """
    Main function to construct and execute the Streamlit application.
    """
    st.image("src/images/banner_monty_hall.png")
    st.title("Monty Hall Simulator :video_game:")

    number_games = st.number_input(
        label="Number of simulations",
        min_value=1, 
        max_value=1000,
        value=100, 
        step=10,
        key="num_simulations"
    )

    # Setup layout columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Switching Doors")
        chart1 = st.line_chart(x=None, y=None, height=200)
        
    with col2:
        st.subheader("Not Switching Doors")
        chart2 = st.line_chart(x=None, y=None, height=200)

    # Trackers for total wins
    win_switch_total = 0.0
    win_no_switch_total = 0.0

    # i starts at 1 to prevent ZeroDivisionError on the first loop
    for i in range(1, int(number_games) + 1):
        # simulate_games returns (win_rate, loss_rate) 
        # In a single game, a switching loss maps exactly to a no-switch win
        switch_win_rate, switch_loss_rate = simulate_games(1, switch_doors=True)
        
        win_switch_total += switch_win_rate
        win_no_switch_total += switch_loss_rate

        # Update charts dynamically
        chart1.add_rows([win_switch_total / i])
        chart2.add_rows([win_no_switch_total / i])

        time.sleep(0.05)

    # Display final metrics inside their respective columns
    with col1:
        st.metric("Switching Win Rate", f"{win_switch_total / number_games:.2%}")
        st.metric("Total Wins by Switching", f"{int(win_switch_total)}")
        
    with col2:
        st.metric("Not Switching Win Rate", f"{win_no_switch_total / number_games:.2%}")
        st.metric("Total Wins by Not Switching", f"{int(win_no_switch_total)}")


if __name__ == "__main__":
    main()
