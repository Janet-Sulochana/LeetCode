# Write your MySQL query statement below
# Write your MySQL query statement below
(select name as results from movierating join users using(user_id) group by user_id order by count(*) desc, name limit 1) union all (select title from movierating join movies using(movie_id) where created_at like '2020-02%' group by movie_id order by avg(rating) desc , title limit 1); 