create table stationID(
    id int auto increment primary key,
    latitude double not null ,
    longitude double not null,
    googleID varchar(50),
    tomtomID varchar(50)
);

create table stz_googleAPI(
    id int auto_increment primary key,
    api_id varchar(80) not null,
    latitude double not null ,
    longitude double not null,
    insert_time timestamp not null default current_timestamp
);

create table stz_tomtomAPI(
    id int auto_increment primary key,
    api_id varchar(80) not null,
    latitude double not null ,
    longitude double not null,
    insert_time timestamp default current_timestamp
);

