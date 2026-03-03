# README — CS 4346 Project #1

**Student ID:** ngq7
**Email:** ngq7@txstate.edu
**Course:** CS 4346 — Artificial Intelligence, Spring 2026

---

## Project Overview

This project demonstrates Machine Learning from Tables using the PSR (Parameter Space Reduction) method. Three datasets were created representing real-world self-driving car decision scenarios. For each dataset, ChatGPT was used to apply the PSR method to discover rules that explain the output column Y. The generated rules and Python/C++ code were then verified for correctness.

### The Three Tables

- **Table A — Should the car brake?**
  Parameters: Obstacle_Detected, Speed_High, Wet_Road, Short_Distance
  Output Y: 1 = Brake, 0 = Do not brake

- **Table B — Should the car change lanes?**
  Parameters: Lane_Clear, Speed_Safe, Turn_Signal_On, No_Blind_Spot
  Output Y: 1 = Change lane, 0 = Stay in lane

- **Table E — Should the car sound an alert?**
  Parameters: Driver_Drowsy, Speed_Exceeded, Lane_Departure, Seatbelt_Off
  Output Y: 1 = Sound alert, 0 = No alert

---

## Files Included

### Data Files
| File | Description |
|------|-------------|
| `Table_A_Brake.xlsx` | Dataset for Table A (100 rows) |
| `Table_B_ChangeLane.xlsx` | Dataset for Table B (100 rows) |
| `Table_E_SoundAlert.xlsx` | Dataset for Table E (100 rows) |

### Source Code Files
| File | Description |
|------|-------------|
| `Project1-ngq7-TableA.py` | Python verification code for Table A |
| `Project1-ngq7-TableB.py` | Python verification code for Table B |
| `Project1-ngq7-TableE.py` | Python verification code for Table E |

### Report
| File | Description |
|------|-------------|
| `Project1-ngq7-Report.docx` | Full project report |
| `README-ngq7.docx` | This README in Word format (for Canvas submission) |

---

## Requirements

Python 3.x must be installed. No external libraries are required — the code uses only built-in Python.

To check your Python version, run:

```bash
python --version
```

---

## How to Run the Python Code

Open a terminal in the project folder and run the script for each table.

### Table A — Should the car brake?

```bash
python Project1-ngq7-TableA.py
```

### Table B — Should the car change lanes?

```bash
python Project1-ngq7-TableB.py
```

### Table E — Should the car sound an alert?

```bash
python Project1-ngq7-TableE.py
```

---

## Expected Output

Each script will output:

1. Total row counts (positives and negatives)
2. PSR value for each parameter (with step-by-step breakdown)
3. The generated ML rules
4. Prediction vs actual Y for every row
5. Final accuracy (100% if rules are perfect)

Example output snippet:
```
--- Verification Summary ---
  Total rows : 100
  Correct    : 100
  Errors     : 0
  Accuracy   : 100.0%

  RESULT: Rules satisfy ALL 100 rows. Verification PASSED.
```
