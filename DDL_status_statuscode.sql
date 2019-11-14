drop table status_statuscode;

-- auto-generated definition
create table status_statuscode
(
  id       int auto_increment
    primary key,
  cmd      varchar(32) not null,
  created  datetime(6) not null,
  modified datetime(6) not null,
  constraint cmd
    unique (cmd)
);


insert into status_statuscode (cmd, created, modified) values ("PUBLISH", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("message", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("SUBSCRIBE", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("UNSUBSCRIBE", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("SET", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("GET", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("RPUSH", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("LPOP", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("PING", sysdate(), sysdate());
insert into status_statuscode (cmd, created, modified) values ("STATUS", sysdate(), sysdate());

commit;