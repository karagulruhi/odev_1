1. ÖDEV

#soru1
select title,description 
from film 

#soru 2

select *
from film
where length<75 and length>60

#soru 3

select *
from film
where rental_rate = 0.99 and replacement_cost = 12.99 and replacement_cost = 28.99

#soru 4

select last_name
from customer
where first_name = 'Mary'

#soru 5
select *
from film
where length<60 and (rental_rate != 2.99 and rental_rate != 4.99)
2.ÖDEV

#SORU 1
select *
from film
where replacement_cost BETWEEN 12.99 AND 16.99
#SORU2
select first_name, last_name 
from actor
where first_name IN ('Ed','Nick','Penelope')
#soru3
select *
from actor
where rental_rate IN (0.99, 2.99, 4.99 ) AND replacement_cost IN( 12.99, 15.99, 28.99)

Ödev 3

#soru 1
select country
from country
where country like 'A%a'

#soru 2
select country
from country
where LENGTH(country)>6 and country LIKE '%n'

#soru3
select title
from film
where title LIKE '%t%t%t%t%'	

#soru4
select *
from film
where title like 'C%' and length>90 and rental_rate = 2.99


#ödev4
soru 1
select distinct replacement_cost  from film

soru 2
select count (distinct replacement_cost)  from film

soru 3
select  COUNT(distinct title) from film
where title ILIKE 'T%'
and rating='G'

soru 4
select count (distinct(country)) from country
where country like '_____'

soru 5
select count (distinct(city)) from city
where city like 'R%r'
