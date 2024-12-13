# sharpsell-assignment



### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [Python3](https://www.python.org/downloads/) (version 3.10 or higher)
- [Virtual Environment (venv)](https://docs.python.org/3/library/venv.html)

### Installation

1. **Clone the Project Repository:**

   Clone this project repository to your local machine using Git. Open your terminal or command prompt and navigate to the directory where you want to store the project:

   ```shell
   git clone https://github.com/gouravsaini021/sharpsell-assignment
   ```
2. **set environment_variable**
    Create a .env file from the provided example.env:
     
     ```shell
     cp example.env .env
     ```

    ```shell
    DATABASE_URL=mysql+aiomysql://<username>:<password>@<host>/<database_name>
    ```
     Replace <username>, <password>, <host>, and <database_name> with your MySQL database credentials
    

3. **Create and Activate a Virtual Environment:**
     ```shell
     cd sharpsell-assignment
    python -m venv venv
     ```
     Activate the virtual environment:
        on windows:
        ```
          .\venv\Scripts\activate
          ```
        on linux or macOS:
       ```source venv/bin/activate```
4. **Install Project Dependencies:**
     ```shell
   pip install -r requirements.txt 
5. **Run the application:**
   ```shell
   uvicorn src.main:app"--host 0.0.0.0 --port 8080
   ```


### Run via Docker Compose

    ### Installation

1. **Clone the Project Repository:**

   Clone this project repository to your local machine using Git. Open your terminal or command prompt and navigate to the directory where you want to store the project:

   ```shell
   git clone https://github.com/gouravsaini021/sharpsell-assignment
   ```

2. **move to sharpsell-assignment folder:**
     ```shell
     cd sharpsell-assignment
     ```

3. **run docker compose command**

    ```shell
     docker compose up
     ```

