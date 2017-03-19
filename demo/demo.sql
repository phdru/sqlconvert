SELECT * FROM `mytable`; -- line-comment"

INSERT into /* inline comment */ mytable VALUES (1, 'тест');

/*! directive*/;

INSERT INTO `MyTable` (`Id`, `Name`)
VALUES (1, 'one');

insert into mytable values (1, 'one'), (2, 'two');

insert into mytable (id, name) values (1, 'one'), (2, 'two');

-- The end
