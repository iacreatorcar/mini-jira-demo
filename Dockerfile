# Usa Python slim come base
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di requirements e installa le librerie
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutti i file nel container
COPY . .

# Espone la porta 5000
EXPOSE 5000

# Comando di default per avviare il server Flask
CMD ["python", "app.py"]
