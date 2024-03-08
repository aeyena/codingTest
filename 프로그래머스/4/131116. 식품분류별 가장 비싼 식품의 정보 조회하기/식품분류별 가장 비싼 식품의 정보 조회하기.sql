select category, price, product_name
from FOOD_PRODUCT
where (category, price) in (
select category, max(price)
from FOOD_PRODUCT
where category in ('과자','국','김치','식용유')
group by category
)
order by price desc

