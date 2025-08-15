# 📦 Inventory Management System in Python

A **robust and user-friendly Inventory Management System** built with **Python**, designed specifically for small businesses like grocery stores and retail shops.  
This CLI-based tool helps you **manage product inventory efficiently** using CSV files for data storage and offers **seamless Excel export** for detailed reporting and analysis.

Whether you want to track stock levels, add or edit product details, or generate reports, this system makes inventory management straightforward and accessible — no complex databases needed!

## ✨ Features

- **Product CRUD Operations:** Create, Read, Update, and Delete products with unique codes.
- **Search & Sort:** Quickly locate items by name or code; sort by name, price, or quantity.
- **CSV Data Storage:** Simple and portable product data management using CSV files.
- **Excel Export:** Generate `.xlsx` reports automatically using [Pandas](https://pandas.pydata.org/).
- **Safe Exit & Save Prompts:** Prevent accidental data loss with confirmation prompts on exit.
- **Interactive Command-Line Interface:** Easy-to-navigate menu for seamless user experience.

## 🛠️ Technologies Used

- **Python** 🐍 — Core programming language
- **Pandas** — Data manipulation and Excel export
- **CSV** — Lightweight and accessible data storage format
- **Fast API** — Web-based user interface for efficient interaction

## 🚀 Planned Future Enhancements

- Develop a **Graphical User Interface (GUI)** for enhanced usability
- Add **multi-user authentication and role-based access control**
- Integrate with **SQLite** or **PostgreSQL** for scalable database management
- Implement a **REST API** for remote inventory operations
- Support for **barcode scanning** to speed up product entry

## 📥 Installation

🌐 FastAPI Integration & Built-in Docs
To enable RESTful API access and interactive documentation, FastAPI can be added to this project. FastAPI provides automatic, interactive API docs via Swagger UI and ReDoc.

1. **Clone the repository:**

   ```sh
   git clone https://github.com/erfandevsol/IMS-project.git
   ```

2. **Navigate to the project folder:**

   ```sh
   cd inventory-management-system
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the API server:**

   ```sh
   uvicorn api:app --reload
   ```

5. **Access built-in docs:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🎯 Usage

- Use the interactive menu to manage inventory: add, edit, delete, search, and sort products.
- Export inventory data to Excel anytime for detailed reporting.
- Always save your changes before exiting to avoid data loss.

## 🤝 Contributing

Contributions are highly appreciated!  
Please fork the repo, make your improvements, and submit a pull request.  
Ensure your code follows existing style conventions and includes relevant tests.
