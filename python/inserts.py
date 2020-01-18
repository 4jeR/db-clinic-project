from db_management import *


def insert_patient(conn, cur, name='', surname='', age='', e_phone='', selected=''):
    _name = name.get()
    _surname = surname.get()
    
    if len(age.get()) == 0:
        _age = 0
    else:
        _age = int(age.get())
    
    _phone = e_phone.get()
    _idp = int(selected.get().split(',')[0])

    if _name.isnumeric() or len(_name) < 3:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne imię.")
        return

    elif _surname.isnumeric() or len(_surname) < 3:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne nazwisko.")
        return

    elif _age <= 0 or _age >= 100:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawny wiek.")
        return

    elif not _phone.isnumeric() or len(_phone) != 9:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawny numer telefonu.")
        return  

    else:
        try:        
            
            cur.execute('INSERT INTO Pacjenci(imie, nazwisko, wiek, nr_telefonu, id_placowki) VALUES (%s, %s, %s, %s, %s)', (_name, _surname, int(_age), _phone, _idp) ) 
            tkinter.messagebox.showinfo("Status", "Pomyślnie zarejestrowano pacjenta. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
        
        except Exception as e: 
            print('Error inserting data', e) 

    conn.commit() 
    
def insert_receptionist(conn, cur, e_name='', e_surname='', selected=''):
    _name = e_name.get()
    _surname = e_surname.get()
    _idp = int(selected.get().split(',')[0])

    if _name.isnumeric() or len(_name) < 3 :
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne imię.")
        return

    elif _surname.isnumeric() or len(_surname) < 3:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne nazwisko.")
        return

    else:
        try:        
            cur.execute('INSERT INTO Recepcjonisci(imie, nazwisko, id_placowki) VALUES (%s, %s, %s)', (_name, _surname, _idp) )
            tkinter.messagebox.showinfo("Status", "Pomyślnie dodano recepcjonistę. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
        
        except Exception as e: 
            print('Error inserting data', e) 

    conn.commit() 

def insert_specialist(conn, cur, root, name='', surname='', specialization='', s_id='', o_id ='',selected=''):
    _name = name.get()
    _surname = surname.get()
    _specialization = specialization.get()
    _idp = int(selected.get().split(',')[0])
    
    if _name.isnumeric() or len(_name) < 3 :
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne imię.")
        return

    elif _surname.isnumeric() or len(_surname) < 3:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawne nazwisko.")
        return
    else:
        try:        
            cur.execute('INSERT INTO Specjalisci(imie, nazwisko, specjalizacja, id_placowki) VALUES (%s, %s, %s, %s)', (_name, _surname, _specialization, _idp) )
            conn.commit()

            conn, cur = connect() 
            specjalisci = get_data_all(conn, cur, 'specjalisci')            
            
            _s_id = int(specjalisci[len(specjalisci)-1].split(',')[0])
            _o_id = int(o_id.get().split(',')[0])
            
            cur.execute('INSERT INTO Specjalisci_Gabinety(id_specjalisty, id_gabinetu) VALUES (%s, %s)', (_s_id, _o_id) )
            tkinter.messagebox.showinfo("Status", "Pomyślnie dodano specjalistę. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
            conn.commit()
        except Exception as e: 
            print('Error inserting data', e) 
            conn.commit()

def insert_office(conn, cur, nr='', selected=''):
    
    if len(nr.get()) == 0:
        _nr = 0
    elif not nr.get().isnumeric():
        tkinter.messagebox.showerror("Error", "Proszę podać poprawny numer")
        return
    else:
        _nr = int(nr.get())

    _idp = int(selected.get().split(',')[0])

    if _nr <= 0 or len(nr.get()) == 0:
        tkinter.messagebox.showerror("Error", "Proszę podać poprawny numer")
        return

    else:
        try:        
            cur.execute('INSERT INTO Gabinety(numer_gabinetu, id_placowki) VALUES (%s, %s)', (_nr, _idp) )
            
            tkinter.messagebox.showinfo("Status", "Pomyślnie dodano gabinet. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")
        
        except Exception as e: 
            print('Error inserting data', e) 

    conn.commit()

def insert_visit(conn, cur, menu_visits='',menu_patients='',menu_specialists='',menu_diseases='',entry_date=''):
    visit_id = int(menu_visits.get().split(',')[0])
    pat_id = int(menu_patients.get().split(',')[0])
    spec_id = int(menu_specialists.get().split(',')[0])
    vd = entry_date.get()

    if len(vd) != 19 or vd[4] != '-' or vd[7] != '-' or vd[10] != ' ' or vd[13] !=':' or vd[16] !=':':
        tkinter.messagebox.showerror("Error", "Proszę podać poprawny format daty wizyty")
        conn.commit()
        return
    try:        
        cur.execute('INSERT INTO Wizyty_Pacjenci(id_wizyty, id_pacjenta, id_specjalisty, data_wizyty) VALUES (%s, %s, %s, %s)', (visit_id, pat_id, spec_id, vd) )
        conn.commit()
        
        _o_id = int(menu_diseases.get().split(',')[0])
    
        cur.execute('INSERT INTO Pacjenci_Dolegliwosci(id_pacjenta, id_dolegliwosci) VALUES (%s, %s)', (pat_id, _o_id) )
        tkinter.messagebox.showinfo("Status", "Pomyślnie umówiono wizytę. Aby wyświetlić zmiany, kliknij przycisk 'odśwież'.")

        conn.commit()

    
    except Exception as e: 
        print('Error inserting data', e) 
        conn.commit()
