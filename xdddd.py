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
Ödev
