create table stationID(
    id int auto increment primary key,
    latitude double not null ,
    longitude double not null,
    googleID varchar(50),
    tomtomID varchar(50)
)