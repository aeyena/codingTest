select b.author_id, a.author_name, b.category, sum(b.price*bs.count) total_sales
from book b inner join (
--도서 별 총 매출량
select book_id, sum(sales) count
from book_sales
where '202201' = to_char(sales_date,'YYYYMM')
group by book_id) bs on (b.book_id=bs.book_id)
inner join author a on (b.author_id=a.author_id)
group by b.category, b.author_id, a.author_name
order by b.author_id asc, b.category desc
