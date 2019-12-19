# Avviare il progetto
Per poter avviare il progetto dovete seguire i seguenti passi: 
* Creare una Virtua Environment
* Installare il file requirements.txt con il seguente comando:
    * `pip install -r requirements.txt`
* posizionarsi nella cartella del progetto in modo da poter creare il db
* se non esiste il db dovete eseguire i seguenti comandi in ordine:
    * `flask db init`
    * `flask db migrate`
    * `flask db upgrade`
    
 Adesso potete avviare l'applicazione eseguento il file `app.py`
