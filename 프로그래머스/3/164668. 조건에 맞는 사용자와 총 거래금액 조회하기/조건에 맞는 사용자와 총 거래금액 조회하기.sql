-- 코드를 입력하세요
select u.user_id, u.nickname, b.total_sales
from used_goods_user u right join 
(select writer_id, sum(price) total_sales
from used_goods_board
where status = 'DONE'
group by writer_id) b on (u.user_id=b.writer_id)
where b.total_sales >= 700000
order by total_sales