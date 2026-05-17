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

<img width="1764" height="864" alt="image" src="https://github.com/user-attachments/assets/503e24d8-dfe5-44f3-9706-10f62b710ef3" />

<img width="1751" height="825" alt="image" src="https://github.com/user-attachments/assets/d8b1fe75-2855-4a1f-8e5d-bdf35e14e525" />

<img width="1647" height="780" alt="image" src="https://github.com/user-attachments/assets/c08fdea2-001e-4de1-9168-8ce1ab027345" />

<img width="1646" height="872" alt="image" src="https://github.com/user-attachments/assets/68f980fa-9935-43b1-9ee6-7df95c5d62ac" />

<img width="1629" height="557" alt="image" src="https://github.com/user-attachments/assets/d1536a8d-1342-4d2e-87dd-ac478ad15871" />

<img width="1642" height="778" alt="image" src="https://github.com/user-attachments/assets/21151ba6-4fc0-4555-a702-5d4286b81c94" />

<img width="1237" height="670" alt="image" src="https://github.com/user-attachments/assets/ecd975d6-ee5f-4727-a635-6e601dbbbf1f" />

<img width="1232" height="588" alt="image" src="https://github.com/user-attachments/assets/9639624c-356f-41b1-9bb0-c1d274c1374a" />

<img width="1237" height="671" alt="image" src="https://github.com/user-attachments/assets/a553e23e-85d4-4c8d-898c-012ed15cc537" />

---

## 💻 How to Run

To install and run your Online Bookstore Management System, follow these steps to set up your environment and launch the server.

### 1. Environment Setup
It is highly recommended to use a virtual environment to keep your project dependencies isolated.

**Create a Virtual Environment:**
```bash
python -m venv venv
