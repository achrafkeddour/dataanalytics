### 1. **Collecte de données**  
   - **Sources de données** :  
     Identifiez les sources, comme :  
     - **API** (services en ligne fournissant des données).  
     - **Bases de données** (SQL, NoSQL).  
     - **Fichiers locaux** (CSV, Excel, JSON, etc.).  
     - **Web scraping** (extraction des données de sites web).  

   - **Outils de collecte** :  
     - **API** : Bibliothèque `requests` ou `http.client`.  
     - **Web scraping** : Utilisez `BeautifulSoup` ou `Selenium`.  
     - **Bases de données** : Connectez-vous avec `pandas` ou des connecteurs comme `SQLAlchemy`.  
     - **Fichiers** : Chargez les fichiers avec `pandas`.  

   - **Exemple de collecte** :  
     ```python
     import pandas as pd

     # Charger un fichier CSV
     data = pd.read_csv('fichier_donnees.csv')
     print(data.head())
     ```

---

### 2. **Nettoyage des données**  
   - **Étapes clés** :  
     - **Gérer les valeurs manquantes** :
       - Remplacer par une valeur par défaut, moyenne, ou supprimer les lignes.  
     - **Uniformiser les formats** :
       - Convertir les colonnes de dates ou numériques dans un format standard.  
     - **Supprimer les doublons** :  
       - Identifiez et supprimez les lignes redondantes.  
     - **Standardiser les valeurs** :
       - Par exemple, aligner les majuscules/minuscules dans des colonnes texte.

   - **Bibliothèques utiles** :  
     - `pandas` pour la manipulation des données.  
     - `numpy` pour des calculs et le traitement des valeurs manquantes.

   - **Exemple de nettoyage** :  
     ```python
     # Remplacer les valeurs manquantes par la moyenne
     data['colonne'] = data['colonne'].fillna(data['colonne'].mean())

     # Supprimer les doublons
     data = data.drop_duplicates()

     # Uniformiser les formats de date
     data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
     ```
