USE final;

INSERT IGNORE INTO fungi (id, name, description) VALUES
    (1, "Chanterelles", "orange"),
    (2, "Jack-o-lantern mushroom", "orange"),
    (3, "Calvatia Gigantea", "big and round white"),
    (4, "Amanita Virosa", "looks like an egg"),
    (5, "Amanita Bisporigera", "looks like an egg"),
    (6, "Shaggy Mane", "white cap top purple cap bottom connical cap"),
    (7, "Alcohol Inky Cap", "white cap top purple cap bottom round cap"),
    (8, "Death Cap", "flat cap wite"),
    (9, "Yellow Morel", "yellow, spongy cap hallow"),
    (10, "False Morel", "orange spongy body");

INSERT IGNORE INTO locations (id, region, description) VALUES
    (1, "African beech forests", "mossy forrested"),
    (2, "American pacific northwest", "mossy forrested"),
    (3, "Iberian Peninsula", "hardwood forests"),
    (4, "central north america", "grassfeilds"),
    (5, "scandanavia", "humid cool"),
    (6, "eastern north america", "oak forrests"),
    (7, "western north america", "forrests and orchards"),
    (8, "mars", "red"),
    (9, "mongolia", "desert"),
    (10, "challanger deep", "wet");

INSERT IGNORE INTO fungus_locations (id, fungus_id, location_id) VALUES
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 3),
    (4, 3, 4),
    (5, 4, 5),
    (6, 5, 6),
    (7, 6, 4),
    (8, 7, 4),
    (9, 8, 5),
    (10, 9, 7),
    (11, 10, 7);


INSERT IGNORE INTO mycotoxins (id, name, effects) VALUES
    (1, "Illuden S", "toxic"),
    (2, "amatoxin", "liver injury, death"),
    (3, "phallotoxin", "liver injury, death"),
    (4, "coprine", "nausea"),
    (5, "virotoxin", "liver injury, death"),
    (6, "gyromitrin", "vertigo, nausea"),
    (7, "aflatoxin", "immune supresion, stunted growth"),
    (8, "lupinosis", "jaundice, death"),
    (9, "psilocin", "hallucination"),
    (10, "oosporein", "cell damage");
    

INSERT IGNORE INTO present_toxins (id, fungus_id, mycotoxin_id) VALUES
    (1, 2, 1),
    (2, 4, 2),
    (3, 4, 3),
    (4, 5, 2),
    (5, 5, 3),
    (6, 7, 4),
    (7, 8, 2),
    (8, 8, 3),
    (9, 8, 5),
    (10, 10, 6);




INSERT IGNORE INTO lookalikes (id, fungus1_id, fungus2_id) VALUES
    (1, 1, 2),
    (2, 3, 4),
    (3, 3, 5),
    (4, 4, 5),
    (5, 6, 7),
    (6, 6, 8),
    (7, 7, 8),
    (8, 9, 10);