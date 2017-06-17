create table if not exists ifc_dta_t(
    ifcnam char(10) not null,
    ifcdsc char(32),
    primary key(ifcnam)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table if not exists ifc_fed_t(
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

create table if not exists wke_dta_t(
    wkecod char(8) not null,
    wkedsc char(32),
    tarsrv char(128),
    primary key(wkecod)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table if not exists wke_ifc_t(
    wkecod char(8) not null,
    ifcnam char(10) not null,
    ifcdir char(1) not null,
    primary key(wkecod, ifcnam, ifcdir)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;