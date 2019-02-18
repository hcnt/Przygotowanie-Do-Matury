SELECT "komputery "."Sekcja", "awarie"."Czas_awarii", 
COUNT( "komputery "."Numer_komputera" ) "liczba", "pomocnicza"."liczba_komputerow" 
FROM "komputery ", "awarie", "pomocnicza" 
WHERE "komputery "."Numer_komputera" = "awarie"."Numer_komputera" 
AND "komputery "."Sekcja" = "pomocnicza"."Sekcja" 
GROUP BY "komputery "."Sekcja", "awarie"."Czas_awarii", "pomocnicza"."liczba_komputerow" 
ORDER BY "liczba" DESC


SELECT  
k.Sekcja
,a.Czas_awarii 
,count(distinct k.Numer_komputera)
FROM komputery as k
left join awarie as a 
on a.Numer_komputera = k.Numer_komputera
group by k.Sekcja
,a.Czas_awarii 
having count(distinct k.Numer_komputera) = (select count(* ) as cnt_komputer 
				from komputery p
				where  k.Sekcja = p.Sekcja )