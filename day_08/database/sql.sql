-- 데이터베이스에 접속하는 명령
-- use 데이터베이스명;
use sakila;

-- 데이터베이스 내부의 테이블 목록을 검색하는 명령
show tables;

-- 테이블의 구조를 확인할 수 있는 명령
-- (desc, describe) 테이블명; 
describe rental;
desc rental;

-- 테이블을 검색하는 쿼리문
-- SELECT 절
-- SELECT 컬렴명1, 컬럼명2, ... *(모든컬럼)
-- FROM 테이블명
select *
from rental;

select rental_id, customer_id, last_update
from rental;

-- WHERE 절을 사용한 조건에 맞는 데이터 검색
-- 조건식의 작성에는 컬럼명이 사용되며, 각 레코드 단위로
-- 실행됩니다.
select *
from rental
where customer_id = 130;

-- 논리연산자의 활용
-- and, or, not
select *
from rental
where customer_id = 130 and staff_id = 1;

-- 직원 데이터를 저장하고 있는 테이블 검색
select *
from staff;

-- 이미지 데이터 존재하지 않는(NULL) 직원을 검색 
-- 주의사항 NULL 값은 부등호로 검색할 수 없습니다.
-- 아래의 SQL문은 검색 결과가 나오지 않습니다.
select *
from staff
where picture = NULL;

-- NULL 값을 검색하려는 경우 is null 연산자를 연산자를 사용
select *
from staff
where picture is NULL;

-- NULL 이 아닌 값을 검색하려는 경우 is not null 연산자를 연산자를 사용
select *
from staff
where picture is not NULL;

-- 문자열 정보를 사용하여 검색
select *
from staff
where first_name = "Mike";

-- 문자열의 부분 정보를 활용하여 검색
-- like 연산자를 활용
-- where 컬럼명 like '검색할 문자열 패턴'
-- 'P%' -> P로 시작하는 모든 문자열을 검색
-- '%P%' -> P를 포함하는 모든 문자열을 검색
-- '_P%' -> 두번째 글자가 P인 모든 문자열을 검색
select *
from actor
where first_name like '_P%';

-- 그룹함수
-- 각 컬럼 데이터의 연산의 결과를 반환하는 함수
-- sum, avg, max, min, count .. 
select * 
from payment;

select sum(amount), avg(amount), max(amount), min(amount)
from payment;

-- 특정 컬럼의 데이터 그룹을 기준으로 함수를 실행한 결과
-- group by 절을 활용
-- group by 절을 사용하는 group by의 기준 컬럼을 출력할 수
-- 있습니다.
select staff_id, sum(amount), avg(amount), max(amount), min(amount)
from payment
group by staff_id;

-- 나리이름과 도시명을 조합하여 출력하기 위한 조인문
-- city 테이블은 country 테이블의 country_id를 
-- 참조하는 테이블입니다.
select *
from city;
select *
from country;

select *
from city, country;

select *
from city, country
where city.country_id = country.country_id;

-- 별칭을 사용하여 조인문의 조건을 기술하는 방법
select *
from city c1, country c2
where c1.country_id = c2.country_id;

-- ANSI 조인을 활용한 조인문
-- 조건에 만족하는 레코드만 추출하는 INNER JOIN
-- FROM 테이블1 INNER JOIN 테이블2
-- ON 조인조건
select *
from city c1 inner join country c2
on c1.country_id = c2.country_id;

-- 동일 컬럼을 사용하여 조인하는 경우 using을 활용
select *
from city join country using(country_id);

-- 데이터베이스를 생성하는 명령
create database mydb;

use mydb;

-- 테이블 생성 방법
-- create table 테이블명 (
--    컬럼명 자료형 [제약조건]
--    ...
-- );

create table myTable (
	-- primary key 제약조건 : 현재 테이블에서
    -- 종복되지 않은 값을 가지는 컬럼을 선언할 때 사용
    -- (기본키 - 주민번호와 같은 데이터 저장에 사용)
	id int primary key,
    -- char : 고정 길이 문자열
    -- -> char(10) 는 데이터의 길이에 관계없이 무조건 10글자로 저장
    -- varchar : 가변 길이 문자열
    -- -> varchar(10)는 실제 데이터의 길이에 맞춰서 조정됨
    -- not null 제약조건 : NULL 값을 허용하지 않는 제약조건
    -- not null 제약이 지정된 컬럼은 반드시 값이 입력되야함
    name varchar(20) not null,
    -- null 제약조건 : NULL 값을 허용하는 컬럼(기본값)
    age int null
);

desc mytable;

-- 테이블에 데이터를 추가(입력)할 수 있는 insert 문
-- INSERT INTO 테이블명 (입력할 컬럼명 - 전체 입력의 경우 생략 가능)
-- VALUES (입력값)
insert into mytable
values (1, 'AAA', 11);

-- 기본키로 지정된 컬럼은 중복된 값의 입력을 허용하지 않음
insert into mytable (id, name)
values (1, 'BBB');

insert into mytable (id, name)
values (2, 'BBB');

select *
from mytable;

-- 테이블 내부의 데이터 수정을 위한 update 절
-- update 테이블명
-- set 수정할컬럼명1 = 수정할값1 [수정할컬럼명N = 수정할값N]
-- where 조건식(특정 컬럼명에 대한 조건식)
update mytable
set age = 0
where id = 2;

select *
from mytable;

update mytable
set age = age + 1;

-- 테이블의 레코드를 삭제할 수 있는 delete 절
-- (테이블 자체를 삭제하는 것이 아닌 레코드만 삭제)
-- delete from 테이블명
-- where 조건식
delete from mytable
where id > 10;






















