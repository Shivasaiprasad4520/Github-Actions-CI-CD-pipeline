# test_app.py

import pytest
import os
import tempfile
import sqlite3
from app import app


# -------------------------
# TEST DATABASE SETUP
# -------------------------
@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()

    app.config['TESTING'] = True
    app.config['DATABASE'] = 'test.db'
    app.config['UPLOAD_FOLDER'] = 'test_uploads'

    os.makedirs("test_uploads", exist_ok=True)

    with app.test_client() as client:

        # Create tables for testing
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            course TEXT,
            roll_no TEXT,
            branch TEXT,
            year TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE announcements(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            file TEXT
        )
        """)

        conn.commit()
        conn.close()

        yield client

    os.close(db_fd)
    os.unlink(db_path)


# -------------------------
# HOME PAGE TEST
# -------------------------
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


# -------------------------
# REGISTER TEST
# -------------------------
def test_register(client):
    response = client.post('/register', data={
        'name': 'Loki',
        'email': 'loki@test.com',
        'password': '123',
        'course': 'DevOps',
        'roll_no': '101',
        'branch': 'CSE',
        'year': '4'
    }, follow_redirects=True)

    assert response.status_code == 200


# -------------------------
# LOGIN TEST
# -------------------------
def test_login(client):
    client.post('/register', data={
        'name': 'Loki',
        'email': 'loki@test.com',
        'password': '123',
        'course': 'DevOps',
        'roll_no': '101',
        'branch': 'CSE',
        'year': '4'
    })

    response = client.post('/login', data={
        'email': 'loki@test.com',
        'password': '123'
    }, follow_redirects=True)

    assert response.status_code == 200


# -------------------------
# ADMIN LOGIN TEST
# -------------------------
def test_admin_login(client):
    response = client.post('/admin-login', data={
        'username': 'admin',
        'password': '123'
    }, follow_redirects=True)

    assert response.status_code == 200


# -------------------------
# FACULTY LOGIN TEST
# -------------------------
def test_faculty_login(client):
    response = client.post('/faculty-login', data={
        'username': 'faculty',
        'password': '123'
    }, follow_redirects=True)

    assert response.status_code == 200