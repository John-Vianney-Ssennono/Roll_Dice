# Dice Rolling Simulator

🎲 Infinite Dice Roller 🎲

A fun, interactive Python command-line utility that simulates rolling a pair of six-sided dice repeatedly until the player decides to call it quits!

🎨 Visual Preview

       ____       ____
      / \'  \     / \'  \
     /   \'  \   /   \'  \
    /___  \'__\ /___  \'__\
    \   /  /   \   /  /
     \ /  /     \ /  /
      \/__/      \/__/


✨ Features

🎲 Interactive Loop: Keep rolling as long as you want.

🔀 True Randomization: Powered by Python's built-in random module.

🔤 Case Insensitive: Accepts both uppercase (Y/N) and lowercase (y/n) inputs seamlessly.

⚡ Lightweight & Fast: Runs instantly in any standard terminal or console environment.

🚀 Quick Start

Prerequisites

Make sure you have Python 3.x installed on your system. You can verify by running:

python --version



📋 How It Works

graph TD
    A[Start Program] --> B[Prompt User: 'y' or 'n'?]
    B -->|'y' or 'Y'| C[Generate 2 Random Numbers 1-6]
    C --> D[Display Dice Results]
    D --> B
    B -->|'n' or 'N'| E[Print Goodbye Message]
    E --> F[End Program]
    B -->|Other Input| G[Show Error & Retry]
    G --> B

