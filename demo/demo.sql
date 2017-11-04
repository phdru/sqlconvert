CREATE TABLE `mytable` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `flag` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT into /* inline comment */ mytable VALUES (1, 'тест');

SELECT * FROM `mytable`; -- line-comment"

/*! directive*/;

INSERT INTO `MyTable` (`Id`, `Name`)
VALUES (1, 'one');

insert into mytable values (1, 'one'), (2, 'two');

insert into mytable (id, name) values (1, 'one'), (2, 'two');

-- The end
