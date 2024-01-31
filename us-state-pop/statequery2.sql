SELECT code, state_name, population FROM states2 JOIN states ON code = abbreviation;
CREATE VIEW state_view AS 
  SELECT code, state_name, population FROM states2 JOIN states ON code = abbreviation;
