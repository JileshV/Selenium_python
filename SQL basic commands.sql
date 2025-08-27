use mydatabase;

create table Student(SNo int(5), SName varchar(15), Marks int(3));

describe student;

insert into student values(105, "Ronak", 99);

select * from student;

insert into student(sname, sno, marks) values("Jilesh", 102, 88);

insert into student values(110, "Ajay", null);

select Marks MarksOutOf100, SName Student from student;

select marks+100, sname from student;