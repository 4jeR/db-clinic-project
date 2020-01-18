import tkinter
from tkinter import *
import tkinter.messagebox
import psycopg2
from guis import *


def connect():
    try:
        conn = psycopg2.connect(
            database = "dfi2dif1n0rgd1",
            user = "kfuhgkrrumgxsu",
            password = "761ea554798535a9c858113362c9c3256421b4eab2f164814225c1e6add1689b",
            host = "54.247.181.239",
            port = "5432"
        )
        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)

    return conn, cur  


def fetch_data_all(conn, cur, table):
    try:
        cur.execute('SELECT * FROM {}'.format(table))
        conn.commit()
    except:
        print('Error fetching the data from {}'.format(table))

    return cur.fetchall()

def get_data_all(conn, cur, table):
    data = fetch_data_all(conn, cur, table)
    result = []
    for tup in data:
        string = ''
        for el in tup:
            string += str(el) + ','
        result.append(string)
        
    return result


def fetch_count_of(conn, cur, table, cond):
    try:
        cur.execute('SELECT COUNT(*) FROM {} {}'.format(table, cond))
        conn.commit()
    except:
        print('Error selecting the data from {}'.format(table))

    return cur.fetchall()


def get_data_count(conn, cur, table, cond=''):
    data = fetch_count_of(conn, cur, table, cond)        
    return data[0][0]


def fetch_vcount_of(conn, cur, view, cond=''):
    try:
        cur.execute('SELECT * FROM {} {}'.format(view, cond))
        conn.commit()
    except:
        print('Error selecting the data from view: {}'.format(view))

    return cur.fetchall()

def get_vdata_count(conn, cur, view, cond=''):
    data = fetch_vcount_of(conn, cur, view, cond)
    return data[0][0]

def delete_patients(conn, cur, selected_patients):
    if len(selected_patients.get()) == 0:
        return
    try:
        patient_id = selected_patients.get().split(',')[0]
        cur.execute('DELETE FROM wizyty_pacjenci WHERE id_pacjenta IN (SELECT id FROM pacjenci where id = %s)', (str(patient_id)))
        cur.execute('DELETE FROM pacjenci_dolegliwosci WHERE id_pacjenta IN (SELECT id FROM pacjenci where id = %s)', (str(patient_id)))
        cur.execute('DELETE FROM pacjenci where pacjenci.id = %s', (str(patient_id)))
        conn.commit()
        tkinter.messagebox.showinfo("Status", "Pomyślnie usunięto pacjenta. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
    except:
        print('Error deleting patients')

def delete_specialists(conn, cur, selected_specialists):
    if len(selected_specialists.get()) == 0:
        return
    try:
        spec_id = selected_specialists.get().split(',')[0]
        cur.execute('DELETE FROM wizyty_pacjenci WHERE id_specjalisty IN (SELECT id FROM specjalisci where id = %s)', (str(spec_id)))
        cur.execute('DELETE FROM specjalisci_gabinety WHERE id_specjalisty IN (SELECT id FROM specjalisci where id = %s)', (str(spec_id)))
        cur.execute('DELETE FROM specjalisci where specjalisci.id = %s', (str(spec_id)))
        conn.commit()
        tkinter.messagebox.showinfo("Status", "Pomyślnie usunięto specjalistę. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
    except:
        print('Error deleting specialists') 


def delete_receptionists(conn, cur, selected_receptionists):
    if len(selected_receptionists.get()) == 0:
        return
    try:
        recep_id = selected_receptionists.get().split(',')[0]
        cur.execute('DELETE FROM recepcjonisci where id = %s', (str(recep_id)))
        conn.commit()
        tkinter.messagebox.showinfo("Status", "Pomyślnie usunięto recepcjonistę. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
    except:
        print('Error deleting receptionists')


def delete_offices(conn, cur, selected_offices):
    if len(selected_offices.get()) == 0:
        return
    try:
        office_id = selected_offices.get().split(',')[0]
        cur.execute('DELETE FROM specjalisci_gabinety WHERE id_gabinetu IN (SELECT id from gabinety where id = %s)',(str(office_id)))
        cur.execute('DELETE FROM gabinety where id = %s', (str(office_id)))
        conn.commit()
        tkinter.messagebox.showinfo("Status", "Pomyślnie usunięto gabinet. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
    except:
        print('Error deleting offices')
