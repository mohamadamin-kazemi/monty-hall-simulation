# Monty Hall Simulation 🎲🚪

A Python project that simulates the famous **Monty Hall Problem** and provides an interactive **Streamlit dashboard** to visualize the probability difference between **switching** and **not switching** doors.

---

## 📖 About the Monty Hall Problem

The Monty Hall problem is a probability puzzle inspired by a game show scenario:

1. A contestant chooses one of three doors.
2. Behind one door is a **car** 🚗.
3. Behind the other two doors are **goats** 🐐.
4. The host, who knows where the car is, opens one of the remaining doors showing a goat.
5. The contestant can either:
   - **Stay** with the original choice
   - **Switch** to the other unopened door

Mathematically:

- Staying gives approximately a **33%** chance of winning.
- Switching gives approximately a **66%** chance of winning.

This project demonstrates that result through large-scale simulations and real-time visualization.

---

## ✨ Features

- Simulate the Monty Hall problem using Python
- Compare:
  - Switching strategy
  - Staying strategy
- Interactive Streamlit dashboard
- Real-time probability visualization
- Dynamic line charts
- Clean and Pythonic implementation
- Type hints and detailed docstrings

---

## 📂 Project Structure

```text
monty-hall-simulation/
│
├── src/
│   ├── images/
│   │   └── banner_monty_hall.png
│   │
│   ├── dashboard.py
│   └── monty_hall.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- Streamlit

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mohamadamin-kazemi/monty-hall-simulation.git
```

Move into the project directory:

```bash
cd monty-hall-simulation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Simulation Script

Run the core simulation:

```bash
python src/monty_hall.py
```

Example output:

```text
Switching wins: 666742 out of 1000000 (66.67%)
Not switching wins: 333258 out of 1000000 (33.33%)
```

---

## 🌐 Running the Streamlit Dashboard

Start the dashboard with:

```bash
streamlit run src/dashboard.py
```

The application will open in your browser automatically.

---

## 📊 Dashboard Features

- Adjustable number of simulations
- Live-updating charts
- Separate statistics for:
  - Switching strategy
  - Staying strategy
- Final win-rate metrics

---

## 🧠 How the Simulation Works

The project uses:

- Randomized car placement
- Random player choices
- Set operations for elegant door logic
- Large-scale repeated simulations for probability estimation

Core logic:

```python
available_for_host = {0, 1, 2} - {initial_choice, car_door}
```

This ensures the host only opens a valid goat door.

---

## 📸 Preview

![Dashboard Preview](src/images/banner_monty_hall.png)

---

## 👨‍💻 Author

**Mohammad Amin Kazemi**

GitHub:  
https://github.com/mohamadamin-kazemi

---

## 📄 License

This project is licensed under the MIT License.