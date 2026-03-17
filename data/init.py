import psycopg2
import os
from dotenv import load_dotenv

load_dotenv("../.env")

def init_db():
    try:
        # Connexion à la base de données PostgreSQL avec l'URL de connexion depuis les variables d'environnement
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        
        # Lecture du fichier SQL
        with open('schema.sql', 'r') as f:
            cur.execute(f.read())
        
        conn.commit()
        print("✅ Base de données initialisée avec succès !")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    init_db()
