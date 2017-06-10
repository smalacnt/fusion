drop table if exists ifc_dta_t;
create table ifc_dta_t(
    ifcnam char(10) not null,
    fedseq smallint unsigned not null,
    fednam char(7) not null,
    feddsc char(16) not null,
    fedtyp char(1) not null,
    fedlen smallint unsigned not null,
    feddec smallint unsigned not null,
    primary key(ifcnam, fedseq),
    unique key(ifcnam, fednam)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;