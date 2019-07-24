DROP TABLE "question";
DROP TABLE "category";
DROP TABLE "answer"


CREATE TABLE "category" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"display"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id")
)

CREATE TABLE "question" (
	"id"	INTEGER NOT NULL UNIQUE,
	"category_id"	INTEGER NOT NULL,
	"text"	TEXT NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("category_id") REFERENCES "category"("id")
)

CREATE TABLE "answer" (
	"id"	INTEGER NOT NULL UNIQUE,
	"question_id"	INTEGER NOT NULL,
	"text"	INTEGER NOT NULL,
	PRIMARY KEY("id")
)

