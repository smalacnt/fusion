drop table if exists ifc_dta_t;
create table ifc_dta_t(
    ifcnam char(10) not null,
    fedseq smallint unsigned not null,
    fednam char(7) not null,
    feddsc char(16),
    fedtyp char(1),
    fedlen smallint unsigned,
    feddec smallint unsigned,
    primary key(ifcnam, fedseq),
    unique key(ifcnam, fednam)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;