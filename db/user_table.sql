create table user (
    email text not null,
    fname text not null,
    lname text not null,
    DOB text,
    location text,
    gender text,
    photo blob,
    password text not null,
    phone text,
    other text,
    primary key(user_id) not null,
);

create table post:
    message integer not null,
    auther integer not null,
    satus integer not null,
    timestamp text not null,
    primary key (post_id) not null,
);

insert into user values ('sofia123@mail.com', 'Sofia', 'HeLlo', '20/12/98', '40.7127, -74.0059', 'F', null, '56_ol%' 
