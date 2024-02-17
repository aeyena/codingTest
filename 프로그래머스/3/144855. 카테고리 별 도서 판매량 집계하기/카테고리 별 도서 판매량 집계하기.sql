select b.category, sum(bs.sales) total_sales
from book b inner join book_sales bs on(b.book_id = bs.book_id)
where to_char(bs.sales_date,'yyyy-mm') = '2022-01'
group by b.category
order by b.category asc