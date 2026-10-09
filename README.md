# Infinite Dice Roller 🎲✨

An interactive command-line Python utility that allows users to simulate rolling two dice continuously in real time. Designed with user control in mind, the program continuously generates randomized results until explicitly instructed to stop.

---

## 🎯 Project Overview

Traditional board games often require physical dice, which can be easily lost or inconvenient to carry. This **Infinite Dice Roller** serves as a lightweight digital replacement.

Unlike fixed-turn dice rolling scripts, this program operates in an **interactive loop driven by user input**. The user controls the execution by entering simple prompts, making it an efficient tool for quick randomized number generation without extra overhead or unnecessary complex dependencies.

---

## 🛠️ Logic & Execution Flow

The script is powered by Python's built-in `random` module. All interactions are handled according to the decision structure below:

| Action / Prompt | User Input | Script Behavior | Output / Result |
| --- | --- | --- | --- |
| **Roll Request** | `y` or `Y` | Triggers two independent random integers from $1$ to $6$ | Displays Die 1, Die 2, Total sum, and double detection |
| **Exit Request** | `n` or `N` | Terminates the loop execution safely | Displays exit message and closes program |
| **Invalid Entry** | *Any other input* | Catches invalid characters | Displays warning prompt and retries loop |

---

## 📦 Features & Functionality

The program is structured to deliver a simple yet complete interactive experience:

* **Case-Insensitive Input Handling:** Accepts both uppercase and lowercase inputs (`Y`/`y` to continue, `N`/`n` to exit).
* **Double Roll Detection:** Automatically identifies when both dice land on identical values.
* **Input Validation:** Prevents program crashes by catching invalid keypresses and prompting the user to try again.
