CREATE TABLE msmpoint (
    skunitid      TEXT        PRIMARY KEY
  , msmid         TEXT        NOT NULL    UNIQUE
  , name          TEXT
  , hardware      TEXT
);
CREATE TABLE httpgetmt (
    unit_id                       INTEGER       NOT NULL
  , dtime                         TEXT          NOT NULL
  , target                        TEXT
  , address                       TEXT
 
  , bytes_sec                     INTEGER

  , threads                       INTEGER
  , successes                     INTEGER
  , failures                      INTEGER
  , location_id                   INTEGER

  , PRIMARY KEY ( unit_id, dtime )
  , FOREIGN KEY ( unit_id ) REFERENCES msmpoint ( skunitid ) ON DELETE CASCADE
);
CREATE TABLE httpgetmt6 (
    unit_id                       INTEGER       NOT NULL
  , dtime                         TEXT          NOT NULL
  , target                        TEXT
  , address                       TEXT

  , bytes_sec                     INTEGER

  , threads                       INTEGER
  , successes                     INTEGER
  , failures                      INTEGER
  , location_id                   INTEGER

  , PRIMARY KEY ( unit_id, dtime )
  , FOREIGN KEY ( unit_id ) REFERENCES msmpoint ( skunitid ) ON DELETE CASCADE
);