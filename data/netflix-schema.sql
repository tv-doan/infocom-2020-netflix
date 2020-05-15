CREATE TABLE msmpoint (
    skunitid      TEXT        PRIMARY KEY
  , msmid         TEXT        NOT NULL    UNIQUE
  , name          TEXT
  , hardware      TEXT
);

CREATE TABLE netflix (
    unit_id                       INTEGER       NOT NULL
  , dtime                         TEXT          NOT NULL
  , target                        TEXT
  , address                       TEXT

  , connect_time                  INTEGER
  , download_duration             INTEGER
  , bytes_sec                     INTEGER

  , error                         TEXT
  , error_msg                     TEXT
  , successes                     INTEGER
  , failures                      INTEGER
  , location_id                   INTEGER

  , FOREIGN KEY ( unit_id ) REFERENCES msmpoint ( skunitid ) ON DELETE CASCADE
);

CREATE TABLE traceroute (
    unit_id                       INTEGER       NOT NULL
  , dtime                         TEXT          NOT NULL
  , version                       TEXT

  , destination                   TEXT
  , method                        TEXT
  , status                        TEXT

  , ttl                           INTEGER
  , endpoint                      TEXT
  , rtt                           TEXT

  , location_id                   INTEGER

  , FOREIGN KEY ( unit_id ) REFERENCES msmpoint ( skunitid ) ON DELETE CASCADE
);
