-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS messages;
DROP SEQUENCE IF EXISTS messages_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS messages_id_seq;
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR(255)
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO messages (text) VALUES ('message_1');
INSERT INTO messages (text) VALUES ('message_2');
INSERT INTO messages (text) VALUES ('message_3');
INSERT INTO messages (text) VALUES ('message_4');

