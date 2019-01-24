select count(distinct osoby.imie) from osoby
join auta on auta.pesel=osoby.pesel
join wypadki on wypadki.numer_rejstracyjny = auta.numer_rejestracyjny

select auta.numer_rejestracyjny,osoby.imię,osoby.nazwisko,wypadki.wysokosc_straty from osoby
join auta on auta.pesel=osoby.pesel
join wypadki on wypadki.numer_rejestracyjny = auta.numer_rejestracyjny
order by wypadki.wysokosc_straty desc
limit 1

select sum(wypadki.wysokosc_straty) from wypadki 
where YEAR(wypadki.data) = 2006 and YEAR(wypadki.data) = 2007

select auta.marka, count(wypadki.id) from auta
join wypadki on wypadki.numer_rejestracyjny = auta.numer_rejestracyjny
group by auta.marka

select osoby.typ_miejscowosci, count(wypadki.id) from osoby
join auta on auta.pesel = osoby.pesel
join wypadki on wypadki.numer_rejstracyjny = auta.numer_rejestracyjny
group by osoby.typ_miejscowosci
