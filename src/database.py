import sqlite3
import os
from hashlib import sha256

DB_PATH = "database.db"


def conectar():
    return sqlite3.connect(DB_PATH)


def inicializar_banco():
    if not os.path.exists(DB_PATH):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE medico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                nome TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE paciente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                identificacao TEXT NOT NULL,
                prontuario TEXT UNIQUE NOT NULL,
                medico_id INTEGER NOT NULL,
                FOREIGN KEY (medico_id) REFERENCES medico(id)
            )
        """)
        conn.commit()
        conn.close()


def hash_senha(senha):
    return sha256(senha.encode()).hexdigest()


def cadastrar_medico(login, senha, nome):
    try:
        conn = conectar()
        cursor = conn.cursor()
        senha_hash = hash_senha(senha)
        cursor.execute("INSERT INTO medico (login, senha, nome) VALUES (?, ?, ?)", (login, senha_hash, nome))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def verificar_login(login, senha):
    conn = conectar()
    cursor = conn.cursor()
    senha_hash = hash_senha(senha)
    cursor.execute("SELECT id FROM medico WHERE login = ? AND senha = ?", (login, senha_hash))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return True, resultado[0]
    return False, None  

def pegar_nome_medico_por_id(medico_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome FROM medico WHERE id = ?", (medico_id,))
    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] if resultado else ""

def cadastrar_paciente(prontuario, identificacao, medico_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO paciente (prontuario, identificacao, medico_id)
            VALUES (?, ?, ?)
        """, (prontuario, identificacao, medico_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def listar_pacientes_por_medico(medico_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id,identificacao, prontuario FROM paciente WHERE medico_id = ?", (medico_id,))
    pacientes = cursor.fetchall()
    conn.close()
    return pacientes

def obter_dados_paciente(paciente_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT identificacao, prontuario FROM paciente WHERE id = ?", (paciente_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado if resultado else None