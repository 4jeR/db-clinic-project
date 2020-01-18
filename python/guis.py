from tkinter import *
from db_management import *
from inserts import *
from help import *


def gui_book_visit(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()

    new_widgets = []

    label_register=Label(root, text="UMAWIANIE WIZYTY\nPrzychodnia: {}\n\n".format(inst_id.get()))
    label_register.grid(row=0,column=1) 
    new_widgets.append(label_register)

    label_list_patients=Label(root, text='UMÓW PACJENTA:')
    label_list_patients.grid(row=1,column=0) 
    new_widgets.append(label_list_patients)

    # pacjent
    patients = get_data_all(conn, cur, 'pacjenci')
    inst_idx = inst_id.get()[0]
    
    patients_final = []
    itr = 0
    for pat in patients:
        if str(pat.split(',')[5]) == inst_idx:
            patients_final.append(pat)
        itr += 1
    
    selected_patients = StringVar(root)
    selected_patients.set(str(patients_final[0]))

    menu_patients = OptionMenu(root, selected_patients, *patients_final)
    menu_patients.grid(row=1,column=1)
    new_widgets.append(menu_patients)
    # pacjent end

    label_list_specialists=Label(root, text='U SPECJALISTY:')
    label_list_specialists.grid(row=2,column=0) 
    new_widgets.append(label_list_specialists)
    # u specjalisty
    specjalisci = get_data_all(conn, cur, 'specjalisci')
    inst_idx = inst_id.get()[0]
  
    specjalisci_final = []
    itr = 0
    for specialist in specjalisci:
        if str(specialist.split(',')[4]) == inst_idx:
            specjalisci_final.append(specialist)
        itr += 1

    selected_specialists = StringVar(root)
    selected_specialists.set('' + str(specjalisci_final[0]))
    
    menu_specialists = OptionMenu(root, selected_specialists, *specjalisci_final)
    menu_specialists.grid(row=2,column=1)
    new_widgets.append(menu_specialists)

    # wizyta

    label_list_visits=Label(root, text='RODZAJ WIZYTY:')
    label_list_visits.grid(row=3,column=0) 
    new_widgets.append(label_list_visits)
    
    visits = get_data_all(conn, cur, 'wizyty')
    selected_visits = StringVar(root)
    selected_visits.set(str(visits[0]))

    menu_visits = OptionMenu(root, selected_visits, *visits)
    menu_visits.grid(row=3,column=1)
    new_widgets.append(menu_visits)
    
    # data   

    label_pick_date=Label(root, text="Wybierz datę wizyty \n(RR-MM-DD GG:MM:SS)")
    label_pick_date.grid(row=4,column=0) 
    new_widgets.append(label_pick_date)

    entry_date=Entry(root)
    entry_date.grid(row=4,column=1)
    new_widgets.append(entry_date)

    # dolegliwosc

    label_pick_disease=Label(root, text="Wybierz dolegliwość:")
    label_pick_disease.grid(row=5,column=0) 
    new_widgets.append(label_pick_disease)

    visits = get_data_all(conn, cur, 'dolegliwosci')
    selected_diseases = StringVar(root)
    selected_diseases.set(str(visits[0]))

    menu_visits = OptionMenu(root, selected_diseases, *visits)
    menu_visits.grid(row=5,column=1)
    new_widgets.append(menu_visits)
    
    # dolegliwosc end
    
    button_register_visit = Button(root,command=lambda:insert_visit(conn, cur, selected_visits,selected_patients,selected_specialists,selected_diseases,entry_date), text="Umów wizytę" )
    button_register_visit.grid(row=6, column=1)
    new_widgets.append(button_register_visit)

    button_back = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Powrót" )
    button_back.grid(row=7, column=1)
    new_widgets.append(button_back)

    button_refresh = Button(root,command=lambda:gui_book_visit(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)



    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    label_list_patients.configure(background=rgb(217, 240, 255))
    label_list_specialists.configure(background=rgb(217, 240, 255))
    label_pick_disease.configure(background=rgb(217, 240, 255))
    label_pick_date.configure(background=rgb(217, 240, 255))
    label_list_visits.configure(background=rgb(217, 240, 255))
    label_register.configure(background=rgb(217, 240, 255))

def gui_register_specialist(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()

    new_widgets = []

    button_refresh = Button(root,command=lambda:gui_register_specialist(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)
    
    specializations = [
        'pedagog dziecięcy',
        'psycholog organizacji i pracy',
        'psycholog rodziny',
        'psycholog wspomagania rozwoju',
        'psychoterapeuta'
    ]


    label_register=Label(root, text="Dodanie specjalisty\nPrzychodnia: {}".format(inst_id.get()))
    label_register.grid(row=0,column=1) 
    new_widgets.append(label_register)

    label_name = Label(root, text="Imię: ")
    label_name.grid(row=1, column=0)
    new_widgets.append(label_name)

    entry_name=Entry(root)
    entry_name.grid(row=1,column=1)
    new_widgets.append(entry_name)

    label_surname = Label(root, text="Nazwisko: ")
    label_surname.grid(row=2, column=0)
    new_widgets.append(label_surname)
    
    entry_surname=Entry(root)
    entry_surname.grid(row=2,column=1)
    new_widgets.append(entry_surname)

    label_specialization = Label(root, text="Specjalizacja: ")
    label_specialization.grid(row=4, column=0)
    new_widgets.append(label_specialization)

    #specjalisci
    specjalisci = get_data_all(conn, cur, 'specjalisci')
    inst_idx = inst_id.get()[0]
    

    specjalisci_final = []
    itr = 0
    for specialist in specjalisci:
        if str(specialist.split(',')[4]) == inst_idx:
            specjalisci_final.append(specialist)
        itr += 1
    

    selected_specialists = StringVar(root)
    selected_specialists.set('' + str(specjalisci_final[0]))

    menu_specialists = OptionMenu(root, selected_specialists, *specjalisci_final)
    menu_specialists.grid(row=1,column=3)
    new_widgets.append(menu_specialists)
    # end lista specjalnosci

    # lista gabinetow
    gabinety = get_data_all(conn, cur, 'gabinety')
    inst_idx = inst_id.get()[0]
   
    gabinety_final = []
    itr = 0
    for gab in gabinety:
        if str(gab.split(',')[2]) == inst_idx:
            gabinety_final.append(gab)
        itr += 1


    selected_gabinety = StringVar(root)
    selected_gabinety.set(str(gabinety_final[0]))
    

    menu_offices = OptionMenu(root, selected_gabinety, *gabinety_final)
    menu_offices.grid(row=3,column=1)
    new_widgets.append(menu_offices)

    label_list_o = Label(root, text="Gabinet: ")
    label_list_o.grid(row=3, column=0)
    new_widgets.append(label_list_o)

    # copy paste end
    count = get_vdata_count(conn, cur, 'ilosc_specjalisci{}'.format(inst_idx))
    label_list_s = Label(root, text="Lista specjalistów ({})".format(count))
    label_list_s.grid(row=0, column=3)
    new_widgets.append(label_list_s)

    selected_specialization = StringVar()
    selected_specialization.set(specializations[0])
    menu_specialization = OptionMenu(root, selected_specialization, *specializations)
    menu_specialization.grid(row=4,column=1)
    new_widgets.append(menu_specialization)

    
    button_register = Button(root, command=lambda:insert_specialist(conn, cur, root, entry_name, entry_surname,selected_specialization ,selected_specialists ,selected_gabinety, inst_id), text="Dodaj")
    button_register.grid(row=5,column=1)
    new_widgets.append(button_register)

    button_back = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Powrót" )
    button_back.grid(row=6, column=1)
    new_widgets.append(button_back)
    

    # STYLE 
    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    label_register.configure(background=rgb(217, 240, 255))
    label_name.configure(background=rgb(217, 240, 255))
    label_surname.configure(background=rgb(217, 240, 255))
    label_specialization.configure(background=rgb(217, 240, 255))
    label_list_o.configure(background=rgb(217, 240, 255))
    label_list_s.configure(background=rgb(217, 240, 255))

def gui_register_office(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()

    new_widgets = []

    button_refresh = Button(root,command=lambda:gui_register_office(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)
    # gabinety

    gabinety = get_data_all(conn, cur, 'gabinety')
    inst_idx = inst_id.get()[0]
   
    gabinety_final = []
    itr = 0
    for gab in gabinety:
        if str(gab.split(',')[2]) == inst_idx:
            gabinety_final.append(gab)
        itr += 1


    selected_gabinety = StringVar(root)
    selected_gabinety.set(str(gabinety_final[0]))
    # copy paste end

    menu_offices = OptionMenu(root, selected_gabinety, *gabinety_final)
    menu_offices.grid(row=1,column=2)
    new_widgets.append(menu_offices)

    count = get_vdata_count(conn, cur, 'ilosc_gabinety{}'.format(inst_idx))
    label_list = Label(root, text="Lista gabinetów, ilość ({})".format(count))
    label_list.grid(row=0, column=2)
    new_widgets.append(label_list)

    label_register=Label(root, text="Dodanie gabinetu\nPrzychodnia: {}".format(inst_id.get()))
    label_register.grid(row=0,column=1) 
    new_widgets.append(label_register)

    label_officeNumber = Label(root, text="Numer gabinetu: ")
    label_officeNumber.grid(row=1, column=0)
    new_widgets.append(label_officeNumber)

    entry_nr=Entry(root)
    entry_nr.grid(row=1,column=1)
    new_widgets.append(entry_nr)


    button_register = Button(root, command=lambda:insert_office(conn, cur, entry_nr, inst_id), text="Dodaj")
    button_register.grid(row=3,column=1)
    new_widgets.append(button_register)

    button_back = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Powrót" )
    button_back.grid(row=5, column=1)
    new_widgets.append(button_back)

    # STYLE

    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    label_list.configure(background=rgb(217, 240, 255))
    label_register.configure(background=rgb(217, 240, 255))
    label_officeNumber.configure(background=rgb(217, 240, 255))

def gui_register_receptionist(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()

    new_widgets = []

    button_refresh = Button(root,command=lambda:gui_register_receptionist(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)

    receptionists = get_data_all(conn, cur, 'recepcjonisci')
    inst_idx = inst_id.get()[0]
    receptionists_final = []
    itr = 0
    for recep in receptionists:
        if str(recep.split(',')[3]) == inst_idx:
            receptionists_final.append(recep)
        itr += 1
    

    selected_receptionists = StringVar(root)
    selected_receptionists.set(str(receptionists_final[0]))

    menu_receptionists = OptionMenu(root, selected_receptionists, *receptionists_final)
    menu_receptionists.grid(row=1,column=3)
    new_widgets.append(menu_receptionists)
    
    #CP
    

    # lista recepcjonistow
    count = get_vdata_count(conn, cur, 'ilosc_recepcjonisci{}'.format(str(inst_idx)))
    label_list = Label(root, text="Lista recepcjonistów, ilość ({})".format(count))
    label_list.grid(row=0, column=3)
    new_widgets.append(label_list)

    button_register = Button(root, command=lambda:insert_receptionist(conn, cur, entry_name, entry_surname, inst_id), text="Dodaj")
    button_register.grid(row=3,column=1)
    new_widgets.append(button_register)

    label_register=Label(root, text="Dodanie recepcjonisty\nPrzychodnia: {}".format(inst_id.get()))
    label_register.grid(row=0,column=1) 
    new_widgets.append(label_register)

    label_name = Label(root, text="Imię: ")
    label_name.grid(row=1, column=0)
    new_widgets.append(label_name)

    entry_name=Entry(root)
    entry_name.grid(row=1,column=1)
    new_widgets.append(entry_name)

    label_surname = Label(root, text="Nazwisko: ")
    label_surname.grid(row=2, column=0)
    new_widgets.append(label_surname)
    
    entry_surname=Entry(root)
    entry_surname.grid(row=2,column=1)
    new_widgets.append(entry_surname)

    button_back = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Powrót" )
    button_back.grid(row=5, column=1)
    new_widgets.append(button_back)

    # STYLE

    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    label_list.configure(background=rgb(217, 240, 255))
    label_register.configure(background=rgb(217, 240, 255))
    label_name.configure(background=rgb(217, 240, 255))
    label_surname.configure(background=rgb(217, 240, 255))

def gui_register_patient(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()

    new_widgets = []

    button_refresh = Button(root,command=lambda:gui_register_patient(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)
    # lista pacjentow

    patients = get_data_all(conn, cur, 'pacjenci')
    inst_idx = inst_id.get()[0]
    

    patients_final = []
    itr = 0
    for pat in patients:
        if str(pat.split(',')[5]) == inst_idx:
            patients_final.append(pat)
        itr += 1
    

    selected_patients = StringVar(root)
    selected_patients.set(str(patients_final[0]))


    menu_patients = OptionMenu(root, selected_patients, *patients_final)
    menu_patients.grid(row=1,column=2)
    new_widgets.append(menu_patients)

    # lista pacjentow END
    


    count = get_vdata_count(conn, cur, 'ilosc_pacjenci{}'.format(inst_idx))
    label_list = Label(root, text="Lista pacjentów, ilość ({}): ".format(count))
    label_list.grid(row=0, column=2)
    new_widgets.append(label_list)


    label_register=Label(root, text="REJESTRACJA PACJENTA: \nPrzychodnia: {}".format(inst_id.get()))
    label_register.grid(row=0,column=1) 
    new_widgets.append(label_register)

    label_name = Label(root, text="Imię: ")
    label_name.grid(row=1, column=0)
    new_widgets.append(label_name)

    entry_name=Entry(root)
    entry_name.grid(row=1,column=1)
    new_widgets.append(entry_name)

    label_surname = Label(root, text="Nazwisko: ")
    label_surname.grid(row=2, column=0)
    new_widgets.append(label_surname)
    
    entry_surname=Entry(root)
    entry_surname.grid(row=2,column=1)
    new_widgets.append(entry_surname)

    label_age = Label(root, text="Wiek: ")
    label_age.grid(row=3, column=0)
    new_widgets.append(label_age)


    entry_age=Entry(root)
    entry_age.grid(row=3,column=1)
    new_widgets.append(entry_age)


    label_phone = Label(root, text="Telefon (9 cyfr): ")
    label_phone.grid(row=4, column=0)
    new_widgets.append(label_phone)


    entry_phone=Entry(root)
    entry_phone.grid(row=4,column=1)
    new_widgets.append(entry_phone)

    
    button_register = Button(root, command=lambda:insert_patient(conn, cur, entry_name, entry_surname, entry_age, entry_phone, inst_id), text="Zarejestruj")
    button_register.grid(row=5,column=1)
    new_widgets.append(button_register)

    button_back = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Powrót" )
    button_back.grid(row=6, column=1)
    new_widgets.append(button_back)

    # STYLE

    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))
    
    label_name.configure(background=rgb(217, 240, 255))
    label_surname.configure(background=rgb(217, 240, 255))
    label_age.configure(background=rgb(217, 240, 255))
    label_phone.configure(background=rgb(217, 240, 255))
    label_list.configure(background=rgb(217, 240, 255))
    label_register.configure(background=rgb(217, 240, 255))


def gui_institution(conn, cur, root, old_widgets, inst_id):
    for widget in old_widgets:
        widget.grid_forget()
    
    new_widgets = []
    label_widgets = []
    inst_idx = int(inst_id.get()[0])

    button_refresh = Button(root,command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Odśwież" )
    button_refresh.grid(row=0, column=0)
    new_widgets.append(button_refresh)

    label_name = Label(root, text="Placówka: " + inst_id.get() + "\n\n")
    label_name.grid(row=0,column=2)
    new_widgets.append(label_name)
    label_widgets.append(label_name)

    button_register_patient = Button(root, command=lambda:gui_register_patient(conn, cur, root, new_widgets, inst_id), text="Zarejestruj pacjenta")
    button_register_patient.grid(row=1,column=1)
    new_widgets.append(button_register_patient)

    button_register_receptionist = Button(root, command=lambda:gui_register_receptionist(conn, cur, root, new_widgets, inst_id), text="Dodaj recepcjonistę")
    button_register_receptionist.grid(row=1,column=2)
    new_widgets.append(button_register_receptionist)

    button_add_office = Button(root, command=lambda:gui_register_office(conn, cur, root, new_widgets, inst_id), text="Dodaj gabinet")
    button_add_office.grid(row=1, column=3)
    new_widgets.append(button_add_office)

    button_visit = Button(root, command=lambda:gui_book_visit(conn, cur, root, new_widgets, inst_id), text="Umów wizytę")
    button_visit.grid(row=2,column=1)
    new_widgets.append(button_visit)

    button_register_specialist = Button(root, command=lambda:gui_register_specialist(conn, cur, root, new_widgets, inst_id), text="Dodaj specjalistę")
    button_register_specialist.grid(row=2,column=2)
    new_widgets.append(button_register_specialist)
    
    label_empty = Label(root, text="\n\n")
    label_empty.grid(row=3, column=2)
    new_widgets.append(label_empty)
    label_widgets.append(label_empty)

    count = get_vdata_count(conn, cur, 'ilosc_pacjenci{}'.format(inst_idx))
    label_list_p = Label(root, text="Lista pacjentów, ilość ({}): ".format(count))
    label_list_p.grid(row=4, column=1)
    new_widgets.append(label_list_p)
    label_widgets.append(label_list_p)

    # pacjenci
    patients = get_data_all(conn, cur, 'pacjenci')
    inst_idx = inst_id.get()[0]
    patients_final = []
    itr = 0
    for pat in patients:
        if str(pat.split(',')[5]) == inst_idx:
            patients_final.append(pat)
        itr += 1
    

    selected_patients = StringVar(root)
    selected_patients.set('brak')
    
    for str_pat in patients_final:
        if len(str_pat) != 0:
            selected_patients.set(str(patients_final[0]))
            break
    
    patients_final = list(filter(None, patients_final))
    menu_patients = OptionMenu(root, selected_patients, *patients_final)
    menu_patients.grid(row=5,column=1)
    new_widgets.append(menu_patients)

    
    button_delete_patient = Button(root,command=lambda:delete_patients(conn, cur, selected_patients), text="Usuń rekord" )
    button_delete_patient.grid(row=6, column=1)
    new_widgets.append(button_delete_patient)


    # recepcjonisci
    count = get_vdata_count(conn, cur, 'ilosc_recepcjonisci{}'.format(str(inst_idx)))
    label_list_r = Label(root, text="Lista recepcjonistów, ilość ({})".format(count))
    label_list_r.grid(row=4, column=2)
    new_widgets.append(label_list_r)
    label_widgets.append(label_list_r)

    receptionists = get_data_all(conn, cur, 'recepcjonisci')
    inst_idx = inst_id.get()[0]
    receptionists_final = []
    itr = 0
    for recep in receptionists:
        if str(recep.split(',')[3]) == inst_idx:
            receptionists_final.append(recep)
        itr += 1
    
    selected_receptionists = StringVar(root)
    selected_receptionists.set(str(receptionists_final[0]))

    menu_receptionists = OptionMenu(root, selected_receptionists, *receptionists_final)
    menu_receptionists.grid(row=5,column=2)
    new_widgets.append(menu_receptionists)
    
    button_gui_recept = Button(root,command=lambda:delete_receptionists(conn, cur, selected_receptionists), text="Usuń rekord" )
    button_gui_recept.grid(row=6, column=2)
    new_widgets.append(button_gui_recept)

    # gabinety
    gabinety = get_data_all(conn, cur, 'gabinety')
    inst_idx = inst_id.get()[0]
   
    gabinety_final = []
    itr = 0
    for gab in gabinety:
        if str(gab.split(',')[2]) == inst_idx:
            gabinety_final.append(gab)
        itr += 1


    selected_gabinety = StringVar(root)
    selected_gabinety.set(str(gabinety_final[0]))

    menu_offices = OptionMenu(root, selected_gabinety, *gabinety_final)
    menu_offices.grid(row=5,column=3)
    new_widgets.append(menu_offices)

    count = get_vdata_count(conn, cur, 'ilosc_gabinety{}'.format(inst_idx))
    label_list_g = Label(root, text="Lista gabinetów, ilość ({})".format(count))
    label_list_g.grid(row=4, column=3)
    new_widgets.append(label_list_g)
    label_widgets.append(label_list_g)

    button_gui_offices = Button(root,command=lambda:delete_offices(conn, cur, selected_gabinety), text="Usuń rekord" )
    button_gui_offices.grid(row=6, column=3)
    new_widgets.append(button_gui_offices)

    # specjalisci
    count = get_vdata_count(conn, cur, 'ilosc_specjalisci{}'.format(inst_idx))
    label_list_sp = Label(root, text="Lista specjalistów ({})".format(count))
    label_list_sp.grid(row=10, column=2)
    new_widgets.append(label_list_sp)
    label_widgets.append(label_list_sp)

    specjalisci = get_data_all(conn, cur, 'specjalisci')
    inst_idx = inst_id.get()[0]
    
    specjalisci_final = []
    itr = 0
    for specialist in specjalisci:
        if str(specialist.split(',')[4]) == inst_idx:
            specjalisci_final.append(specialist)
        itr += 1
    
    selected_specialists = StringVar(root)
    selected_specialists.set('' + str(specjalisci_final[0]))

    specjalisci_final = list(filter(None, specjalisci_final))
    menu_specialists = OptionMenu(root, selected_specialists, *specjalisci_final)
    menu_specialists.grid(row=11,column=2)
    new_widgets.append(menu_specialists)

    button_delete_spec = Button(root,command=lambda:delete_specialists(conn, cur, selected_specialists), text="Usuń rekord" )
    button_delete_spec.grid(row=12, column=2)
    new_widgets.append(button_delete_spec)

    button_back = Button(root,command=lambda:gui_main(conn, cur, root, new_widgets), text="Powrót" )
    button_back.grid(row=2, column=0)
    new_widgets.append(button_back)

    # STYLE 

    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    for lwidget in label_widgets:
        lwidget.configure(background=rgb(217, 240, 255))


def gui_main(conn, cur, root, old_widgets):
    for widget in old_widgets:
        widget.grid_forget()
        
    new_widgets = []

    button_choose_inst = Button(root, command=lambda:gui_institution(conn, cur, root, new_widgets, inst_id), text="Przejdź")
    button_choose_inst.grid(row=2,column=0)
    new_widgets.append(button_choose_inst)

    button_exit = Button(root, command=lambda:exit_app(root), text="Zamknij aplikację.")
    button_exit.grid(row=1,column=2)
    new_widgets.append(button_exit)

    label_empty = Label(root, text="\n\n")
    label_empty.grid(row=4,column=2)
    new_widgets.append(label_empty)
    
    # wizyty ########
    count = get_vdata_count(conn, cur, 'ilosc_wizyty')
    label_list_visits = Label(root, text="WIZYTY ({})".format(count))
    label_list_visits.grid(row=7,column=2)
    new_widgets.append(label_list_visits)

    visits = get_data_all(conn, cur, 'wizyty')
    selected_visits = StringVar(root)
    selected_visits.set(visits[0])
    menu_visits = OptionMenu(root, selected_visits, *visits)
    menu_visits.grid(row=8,column=2)
    new_widgets.append(menu_visits)

    # wizyty_pacjenci ######
    count = get_vdata_count(conn, cur, 'ilosc_wizyty_pacjenci')
    label_list_vp = Label(root, text="WIZYTY_PACJENCI ({})".format(count))
    label_list_vp.grid(row=9,column=1)
    new_widgets.append(label_list_vp)

    vp = get_data_all(conn, cur, 'wizyty_pacjenci')
    selected_vp = StringVar(root)
    selected_vp.set(vp[0])
    menu_vp = OptionMenu(root, selected_vp, *vp)
    menu_vp.grid(row=10,column=1)
    new_widgets.append(menu_vp)

    # pacjenci ##########
    count = get_vdata_count(conn, cur, 'ilosc_pacjenci')
    label_list_patients = Label(root, text="PACJENCI ({})".format(count))
    label_list_patients.grid(row=5,column=0)
    new_widgets.append(label_list_patients)

    patients = get_data_all(conn, cur, 'pacjenci')
    selected_patients = StringVar(root)
    selected_patients.set(patients[0])
    menu_patients = OptionMenu(root, selected_patients, *patients)
    menu_patients.grid(row=6,column=0)
    new_widgets.append(menu_patients)

    # pacjenci_dolegliwosci #########
    count = get_vdata_count(conn, cur, 'ilosc_pacjenci_dolegliwosci')
    label_list_pd = Label(root, text="PACJENCI_DOLEGLIWOŚCI".format(count))
    label_list_pd.grid(row=9,column=0)
    new_widgets.append(label_list_pd)

    pd = get_data_all(conn, cur, 'pacjenci_dolegliwosci')
    selected_pd = StringVar(root)
    selected_pd.set(pd[0])
    menu_pd = OptionMenu(root, selected_pd, *pd)
    menu_pd.grid(row=10,column=0)
    new_widgets.append(menu_pd)

    # specjalisci ########
    count = get_vdata_count(conn, cur, 'ilosc_specjalisci')
    label_list_specialists = Label(root, text="SPECJALISCI ({})".format(count))
    label_list_specialists.grid(row=7,column=0)
    new_widgets.append(label_list_specialists)

    specialists = get_data_all(conn, cur, 'specjalisci')
    selected_specialists = StringVar(root)
    selected_specialists.set(specialists[0])
    menu_specialists = OptionMenu(root, selected_specialists, *specialists)
    menu_specialists.grid(row=8,column=0)
    new_widgets.append(menu_specialists)

    # specjalisci_gabinety ########
    count = get_vdata_count(conn, cur, 'ilosc_specjalisci_gabinety')
    label_list_so = Label(root, text="SPECJALIŚCI_GABINETY ({})".format(count))
    label_list_so.grid(row=7,column=1)
    new_widgets.append(label_list_so)

    so = get_data_all(conn, cur, 'specjalisci')
    selected_so = StringVar(root)
    selected_so.set(so[0])
    menu_so = OptionMenu(root, selected_so, *so)
    menu_so.grid(row=8,column=1)
    new_widgets.append(menu_so)

    # gabinety ##########
    count = get_vdata_count(conn, cur, 'ilosc_gabinety')
    label_list_offices = Label(root, text="GABINETY ({})".format(count))
    label_list_offices.grid(row=5,column=1)
    new_widgets.append(label_list_offices)

    offices = get_data_all(conn, cur, 'gabinety')
    selected_gabinety = StringVar(root)
    selected_gabinety.set(offices[0])
    menu_offices = OptionMenu(root, selected_gabinety, *offices)
    menu_offices.grid(row=6,column=1)
    new_widgets.append(menu_offices)


    #dolegliwosci ######
    count = get_vdata_count(conn, cur, 'ilosc_dolegliwosci')
    label_list_diseases = Label(root, text="DOLEGLIWOŚCI ({})".format(count))
    label_list_diseases.grid(row=9,column=2)
    new_widgets.append(label_list_diseases)

    diseases = get_data_all(conn, cur, 'dolegliwosci')
    selected_diseases = StringVar(root)
    selected_diseases.set(diseases[0])
    menu_diseases = OptionMenu(root, selected_diseases, *diseases)
    menu_diseases.grid(row=10,column=2)
    new_widgets.append(menu_diseases)

    institutions = get_data_all(conn, cur, 'placowki')
    inst_id = StringVar(root)
    inst_id.set(institutions[0])

    label_list_inst = Label(root, text="WYBIERZ PLACÓWKĘ:")
    label_list_inst.grid(row=0,column=0)
    new_widgets.append(label_list_inst)

    menu_inst = OptionMenu(root, inst_id, *institutions)
    menu_inst.grid(row=1,column=0)
    new_widgets.append(menu_inst)
    
    #recepcjonisci ########
    count = get_vdata_count(conn, cur, 'ilosc_recepcjonisci')
    label_list_receptionists = Label(root, text="RECEPCJONIŚCI ({})".format(count))
    label_list_receptionists.grid(row=5,column=2)
    new_widgets.append(label_list_receptionists)

    receptionits = get_data_all(conn, cur, 'recepcjonisci')
    selected_recepcjonisci = StringVar(root)
    selected_recepcjonisci.set(receptionits[0])
    menu_receptionists = OptionMenu(root, selected_recepcjonisci, *receptionits)
    menu_receptionists.grid(row=6,column=2)
    new_widgets.append(menu_receptionists)
    
    label_widgets = []
    label_widgets.append(label_empty)
    label_widgets.append(label_list_inst)
    label_widgets.append(label_list_patients)
    label_widgets.append(label_list_receptionists)
    label_widgets.append(label_list_offices)
    label_widgets.append(label_list_visits)
    label_widgets.append(label_list_specialists)
    label_widgets.append(label_list_diseases)
    label_widgets.append(label_list_vp)
    label_widgets.append(label_list_pd)
    label_widgets.append(label_list_so)

    # STYLE

    for widget in new_widgets:
        widget.configure(background=rgb(112, 169, 204))

    for lwidget in label_widgets:
        lwidget.configure(background=rgb(217, 240, 255))
    