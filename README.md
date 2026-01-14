# mini-jira-demo

A simple Jira-like project management board using Python (Flask), HTML, and CSS.

## Features
- Add new tasks with title and description
- Visualize tasks by status ("To Do", "In Progress", "Done")
- Move tasks between statuses

## Running Locally

1. Clone this repository:
    ```
    git clone https://github.com/YOUR_USERNAME/mini-jira-demo.git
    cd mini-jira-demo
    ```
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Start the app:
    ```
    python app.py
    ```
5. Visit `http://127.0.0.1:5000` in your browser.

## Running with Docker

1. Build the image:
    ```
    docker build -t mini-jira-demo .
    ```
2. Run the container:
    ```
    docker run -d -p 5000:5000 mini-jira-demo
    ```
3. Open `http://localhost:5000` in your browser.

---

# Mini Jira Demo (Italiano)

Un semplice gestore di task in stile Jira realizzato con Python (Flask), HTML e CSS.

## Funzionalità
- Aggiungi nuovi task con titolo e descrizione
- Visualizza i task raggruppati per stato ("To Do", "In Progress", "Done")
- Cambia lo stato dei task

## Esecuzione locale

1. Clona questa repository:
    ```
    git clone https://github.com/YOUR_USERNAME/mini-jira-demo.git
    cd mini-jira-demo
    ```
2. (Opzionale) Crea e attiva un ambiente virtuale.
3. Installa le dipendenze:
    ```
    pip install -r requirements.txt
    ```
4. Avvia l'applicazione:
    ```
    python app.py
    ```
5. Vai su `http://127.0.0.1:5000` nel browser.

## Esecuzione con Docker

1. Crea l'immagine:
    ```
    docker build -t mini-jira-demo .
    ```
2. Esegui il container:
    ```
    docker run -d -p 5000:5000 mini-jira-demo
    ```
3. Vai su `http://localhost:5000` nel browser.
