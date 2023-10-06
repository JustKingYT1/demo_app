INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (0, "Guest", 0);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (1, "User", 1);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (2, "Manager", 2);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (3, "Admin", 3);

INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (65, 0, "Pismenskiy V. S.", "89377028077", "2004-02-07");
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (2, 1, "Pismenskciy V. S.", "89377028277", "2004-01-07");
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (3, 2, "Pismefnskiy V. S.", "89377028377", "2004-03-07");
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (635, 3, "Pismefdfdnskiy V. S.", "89377048377", "2004-06-07");