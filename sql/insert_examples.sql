-- placówki --
insert into placowki (ulica, miejscowosc)
values ('Rema 32', 'Kraków');

insert into placowki (ulica, miejscowosc)
values ('Pielgrzymów 11', 'Kraków');

insert into placowki (ulica, miejscowosc)
values ('Reja 8', 'Warszawa');

insert into placowki (ulica, miejscowosc)
values ('Sulikowskiego 38', 'Rzeszów');

-- gabinety --
insert into gabinety(numer_gabinetu, id_placowki)
values (11, 1);

insert into gabinety(numer_gabinetu, id_placowki)
values (12, 1);

insert into gabinety(numer_gabinetu, id_placowki)
values (24, 2);

insert into gabinety(numer_gabinetu, id_placowki)
values (25, 2);

insert into gabinety(numer_gabinetu, id_placowki)
values (31, 3);

insert into gabinety(numer_gabinetu, id_placowki)
values (47, 4);

insert into gabinety(numer_gabinetu, id_placowki)
values (48, 4);

-- wizyty --
insert into wizyty(nazwa_wizyty, cena)
values ('prywatna', 50);

insert into wizyty(nazwa_wizyty, cena)
values ('na NFZ', 0);

insert into wizyty(nazwa_wizyty, cena)
values ('konsultacja', 30);

insert into wizyty(nazwa_wizyty, cena)
values ('konsultacja-pierwsza', 40);


-- dolegliwosci --
insert into dolegliwosci (nazwa)
values ('napad lękowy');

insert into dolegliwosci (nazwa)
values ('schizofrenia');

insert into dolegliwosci (nazwa)
values ('anoreksja');

insert into dolegliwosci (nazwa)
values ('depresja');

-- recepcjonisci --
insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Adam', 'Mickiewicz', 2);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Mikołaj', 'Rej', 3);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Juliusz', 'Słowacki', 4);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Jan', 'Kochanowski', 1);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Tomasz', 'Kamel', 2);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Michał', 'Wiśniewski', 3);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Julia', 'Słowacka', 4);

insert into recepcjonisci (imie, nazwisko, id_placowki)
values ('Piotr', 'Niekochanowski', 1);

-- pacjenci --
insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Małgorzata', 'Górnik', 22, '123696321', 1);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Grzegorz', 'Murdek', 21, '551321422', 3);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Michał', 'Konopka', 21, '731325561', 4);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Jan', 'Brzechwa', 39, '899009032', 2);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Patrycja', 'Minik', 25, '185963271', 1);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Karol', 'Drzewo', 46, '728966999', 3);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Tadeusz', 'Kleszczyński', 31, '411355371', 4);

insert into pacjenci (imie, nazwisko, wiek, nr_telefonu, id_placowki)
values ('Adam', 'Boryła', 49, '400901232', 2);

-- specjalisci --
insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Bartłomiej', 'Jurman', 'psychoterapeuta', 2);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Mateusz', 'Kozak', 'pedagog dziecięcy', 3);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Patrycja', 'Dzik', 'psycholog wspomagania rozwoju', 1);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Adam', 'Barbur', 'psycholog wspomagania rozwoju', 4);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Hubert', 'Godak', 'psycholog organizacji i pracy', 2);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Ksawery', 'Pień', 'psycholog rodziny', 3);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Monika', 'Zalewska', 'pedagog dziecięcy', 1);

insert into specjalisci (imie, nazwisko, specjalizacja, id_placowki )
values ('Zofia', 'Wawel', 'psychoterapeuta', 4);

-- wizyty_pacjenci -- 
insert into wizyty_pacjenci (id_wizyty, id_pacjenta, id_specjalisty, data_wizyty)
values (1, 2, 3, '2020-01-22 19:00:00');

insert into wizyty_pacjenci  (id_wizyty, id_pacjenta, id_specjalisty, data_wizyty)
values (2, 1, 2, '2020-01-16 18:00:00');

insert into wizyty_pacjenci  (id_wizyty, id_pacjenta, id_specjalisty, data_wizyty)
values (3, 3, 1, '2020-02-11 18:30:00');

insert into wizyty_pacjenci  (id_wizyty, id_pacjenta, id_specjalisty, data_wizyty)
values (4, 4, 1, '2020-03-11 15:30:00');

insert into wizyty_pacjenci (id_wizyty, id_pacjenta, id_specjalisty, data_wizyty)
values (2, 5, 5, '2020-02-14 15:00:00');

-- pacjenci_dolegliwosci --
insert into pacjenci_dolegliwosci(id_pacjenta, id_dolegliwosci)
values (1, 3);

insert into pacjenci_dolegliwosci(id_pacjenta, id_dolegliwosci)
values (2, 2);

insert into pacjenci_dolegliwosci(id_pacjenta, id_dolegliwosci)
values (3, 4);

insert into pacjenci_dolegliwosci(id_pacjenta, id_dolegliwosci)
values (4, 1);


-- specjalisci_gabinety --
insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (1, 3);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (2, 5);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (3, 1);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (4, 6);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (5, 4);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (6, 5);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (7, 2);

insert into specjalisci_gabinety(id_specjalisty, id_gabinetu)
values (8, 7);