DROP TABLE IF EXISTS profile;

CREATE TABLE profile (
            id INT,
            first_name CHAR(25) NOT NULL,
            last_name CHAR(25),
            age INT
);

-- ah ah ah, no sensitive data here!
INSERT INTO profile (id, first_name, last_name, age) VALUES (1, "Major", "Johnson", 48);
INSERT INTO profile (id, first_name, last_name, age) VALUES (2, "John", "Forebrosia", 35);
INSERT INTO profile (id, first_name, last_name, age) VALUES (3, "Macy", "Kuliak", 28);
INSERT INTO profile (id, first_name, last_name, age) VALUES (4, "Alice", "Major", 18);
INSERT INTO profile (id, first_name, last_name, age) VALUES (5, "Cryptopolis", "Bloom", 37);
INSERT INTO profile (id, first_name, last_name, age) VALUES (6, "Joe", "Schmoe", 25);
INSERT INTO profile (id, first_name, last_name, age) VALUES (7, "John", "Doe", 26);
INSERT INTO profile (id, first_name, last_name, age) VALUES (8, "Javier", "Bierdole", 22);
