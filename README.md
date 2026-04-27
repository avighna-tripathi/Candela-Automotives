# Candela Automotives

A comprehensive software management system designed for the automotive sector. Developed between January and March 2024, this project focuses on efficient data manipulation, visualization, and database management for various organizational departments.

## 🚀 Features

The system is modularized to handle different aspects of automotive business operations seamlessly:
* **Finance Management** (`Finance_software.py`): Tools for tracking and managing financial records.
* **Human Resources** (`HR_software.py`): Employee and personnel management functionalities.
* **Purchasing** (`purchase_software.py`): Inventory and procurement tracking.
* **User Operations** (`user_software.py`): General user interaction and access handling.

## 🛠️ Technology Stack

* **Core Language:** Python
* **Data Manipulation & Visualization:** NumPy, Pandas, Matplotlib
* **Database:** MySQL

## 📂 Project Structure

```text
Candela-Automotives/
├── MAIN FILE.py            # Central entry point for the application
├── creation_tables.py      # MySQL database initialization script
├── Finance_software.py     # Finance department module
├── HR_software.py          # HR department module
├── purchase_software.py    # Purchasing department module
├── user_software.py        # User operations module
├── MARKETING/              # Marketing resources and data
└── Plms/                   # Additional project data
```

##⚙️ Setup & Installation

**Clone the repository:**
git clone [https://github.com/avighna-tripathi/Candela-Automotives.git](https://github.com/avighna-tripathi/Candela-Automotives.git)
cd Candela-Automotives

**Install dependencies:**
Ensure you have a local MySQL server installed and running. Then, install the required Python libraries:
pip install numpy pandas matplotlib mysql-connector-python


**Database Setup:**
Open creation_tables.py and update it with your local MySQL credentials (username and password) if necessary. Run the script to set up your database schema:
python creation_tables.py

**Run the Application:**
Start the software by executing the main script:
python "MAIN FILE.py"

**👨‍💻 Author**
Avighna Tripathi

GitHub
