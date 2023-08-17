-- Craciun Florin Cristian, 141, Sb. 1, exam241
-- Ex 1a
select c.data_plecare, e.denumire, a.nr_inmatriculare
from calendar c
join excursie e on e.id_excursie = c.id_excursie
join autocar a on a.id_autocar = c.id_autocar
where to_char(c.data_plecare, 'MM, YYYY') = '08, 2023';

-- Ex 1b
select e.denumire, count(c.data_plecare) as nr_planificari
from excursie e
join calendar c on c.id_excursie = e.id_excursie
where to_char(c.data_plecare, 'YYYY') = '2023'
group by e.denumire
having count(c.data_plecare) >= 2;

-- Ex 2
select t.nume, t.prenume, sum(c.pret) as suma_totala
from turist t
join rezervare r on r.id_turist = t.id_turist
join calendar c on c.id_calendar = r.id_calendar
group by t.nume, t.prenume

-- Ex 3
select e.denumire, c.data_plecare, (
    select count(r.id_turist)
    from rezervare r
    join calendar c2 on c2.id_calendar = r.id_calendar
    where c2.data_plecare = c.data_plecare
    ) as nr_turisti
from excursie e
join calendar c on c.id_excursie = e.id_excursie
join autocar a on a.id_autocar = c.id_autocar
join program_ghid p on p.id_calendar = c.id_calendar
where a.capacitate > 30
group by e.denumire, c.data_plecare
having count(p.id_ghid) < 2;
-- pentru mai mic sau egal 2 returneaza:
-- Denumire, Data_plecare, nr_turisti
-- Piatra Craiului Creasta Sudica,2023-09-20,2
-- Cabana Malaiesti,2023-06-01,5
-- Cabana Malaiesti,2024-07-03,4
