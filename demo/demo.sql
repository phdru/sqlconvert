SELECT * FROM `mytable`; -- line-comment"
INSERT into /* inline comment */ mytable VALUES (1, 'тест');
/*! directive*/;
INSERT INTO `MyTable` (`Id`, `Name`)
VALUES (1, 'one');

-- The end