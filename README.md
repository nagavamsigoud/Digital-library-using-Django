# Online Bookstore Management System

A robust, full-stack web application designed to streamline the operations of a digital bookstore. The system allows users to browse collections, place orders, and manage order histories, while providing administrators with total control over inventory and customer tracking.

---

## 🚀 Features

### For Customers
* **Book Discovery:** Browse a dynamic list of available books organized by categories.
* **Shopping Cart:** Add desired items to a cart and manage quantities before checkout.
* **Order Management:** View a paginated history of all past orders.
* **Request System:** Request specific books if they are currently unavailable in the store.
* **Digital Invoices:** Generate and download professional PDF invoices for individual orders.

### For Administrators
* **Inventory Control:** Add new titles to the collection or delete existing ones.
* **Order Fulfillment:** Monitor all customer orders and requested books to manage supply.
* **User Management:** Oversee registered customers and their associated transaction data.

---

## 🛠️ Tech Stack

The application follows a Client-Server Architecture built with the following technologies:

| Component | Technology |
| :--- | :--- |
| **Backend** | Python 3 using the Django web framework. |
| **Frontend** | HTML5, JavaScript, and CSS for a responsive user interface. |
| **Database** | SQLite3 for lightweight, serverless relational data management. |
| **Documentation** | UML Modeling (ER Diagrams, DFDs, Sequence, and Activity Diagrams). |

---

## 📐 System Design

### Database Architecture
The system utilizes five primary database tables. Key components include:
* **Order:** Stores customer contact details, payment methods, and total costs.
* **OrderItem:** Tracks specific books and quantities within a single transaction.
* **User:** Manages authentication and authorization for customers and admins.

### Modeling (UML)
The development process followed strict software engineering standards:
* **Use Case Diagrams:** To visualize user interactions with system features.
* **Sequence Diagrams:** To detail the time-ordered interaction between objects (e.g., searching, saving data).
* **Activity Diagrams:** To map workflows from login through to final purchase.

---

## 🛡️ Quality Assurance

The system underwent multiple levels of testing to ensure reliability:
* **Unit Testing:** Verified individual modules (Login, HWAdmin, etc.) for functional accuracy.
* **Integration Testing:** Ensured seamless interaction between different services.
* **White Box & Black Box Testing:** Conducted thorough statement-level and interface-level validation.
* **Acceptance Testing:** Validated system performance using realistic client data scenarios.

---

## 📋 Requirements

### Hardware
* **Processor:** 2.4 GHz or higher.
* **RAM:** Minimum 1 GB.
* **Storage:** 80 GB HDD.

### Software
* **OS:** Windows 10 or 11
* **Language:** Python 3.x.
* **Tool:** Sublime Text or any modern IDE.

---

## 📸 Screenshots

<img width="1764" height="864" alt="Screenshot 2026-04-19 152639" src="https://github.com/user-attachments/assets/a090524a-9adb-439d-8c3e-324fbcbdf798" />

<img width="1751" height="825" alt="Screenshot 2026-04-19 152742" src="https://github.com/user-attachments/assets/c4b17444-b08a-4458-89ce-a888d25f043b" />

<img width="1647" height="780" alt="Screenshot 2026-04-19 152811" src="https://github.com/user-attachments/assets/5b6ea384-be9b-4086-95a1-c6a1d4e56234" />

<img width="1646" height="872" alt="Screenshot 2026-04-19 152834" src="https://github.com/user-attachments/assets/f9c0cce8-ee3b-415b-be03-78a9497c0e74" />

<img width="1629" height="557" alt="Screenshot 2026-04-19 152856" src="https://github.com/user-attachments/assets/16d34f12-6981-45e6-a070-4ff73781a2c7" />

<img width="1642" height="778" alt="Screenshot 2026-04-19 152923" src="https://github.com/user-attachments/assets/8fe604e9-409b-48f7-b3ca-78e4f66ea078" />

<img width="1237" height="670" alt="Screenshot 2026-04-19 152950" src="https://github.com/user-attachments/assets/87cb5a32-2b54-41cd-8149-cc474e157bb4" />

<img width="1232" height="588" alt="Screenshot 2026-04-19 153009" src="https://github.com/user-attachments/assets/283b0657-6a2d-4f18-8787-f0cf9fe97fc1" />













---

## 💻 How to Run

Follow these step-by-step instructions to set up your environment, install the dependencies, and launch the development server.

### 1. Environment Setup
It is highly recommended to use a virtual environment to keep your project dependencies isolated.

**Create a Virtual Environment:**
```powershell
python -m venv venv
venv\Scripts\activate


### 2. Install Dependencies
Use the `requirements.txt` file to install all necessary backend libraries at once.
```powershell
pip install -r requirements.txt

Prepare Migrations:
python manage.py makemigrations

Apply Migrations: (This generates your local SQLite3 database tables)

python manage.py migrate

Start the Application
Once the installation and database configurations are complete, boot up the local development server:

python manage.py runserver
Access the Bookstore: Open you
