SET search_path to nba;

DROP TABLE IF EXISTS players;

CREATE TABLE players (
    pid VARCHAR(250) PRIMARY KEY,
    playerName VARCHAR(250) NOT NULL
);