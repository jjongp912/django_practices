-- 
desc guestbook;

-- insert
insert into guestbook values(null, '박종진', '1234', 'ㅎㅇ~', now());

-- select
select no, name, message, date_format(reg_date, '%Y-%m-%d %h:%i:%s') 
from guestbook 
order by reg_date desc;

-- delete
delete 
from guestbook
where no = 4
and password = '1234';
