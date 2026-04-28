USE final;

INSERT IGNORE INTO fungi (id, name, description) VALUES
    (1, "mushroom", "food"),
    (2, "mushroom2", "not food");

INSERT IGNORE INTO locations (id, region, description) VALUES
    (1, "up", "cold"),
    (2, "down", "humid");

INSERT IGNORE INTO fungus_locations (id, fungus_id, location_id) VALUES
    (1, 1, 1),
    (2, 2, 1);

INSERT IGNORE INTO mycotoxins (id, name, effects) VALUES
    (1, "Instant death poison", "tummy ache"),
    (2, "yummy juice", "instant death");

INSERT IGNORE INTO present_toxins (id, fungus_id, mycotoxin_id) VALUES
    (1, 2, 1),
    (2, 2, 2);

INSERT IGNORE INTO lookalikes (id, fungus1_id, fungus2_id) VALUES
    (1, 1, 2);