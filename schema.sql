CREATE DATABASE IF NOT EXISTS final;
USE final;

CREATE TABLE IF NOT EXISTS `fungi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `mycotoxins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `effects` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `locations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `region` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `fungus_locations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fungus_id` int NOT NULL,
  `location_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fungus_id` (`fungus_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `fungus_locations_ibfk_1` FOREIGN KEY (`fungus_id`) REFERENCES `fungi` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fungus_locations_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `present_toxins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fungus_id` int NOT NULL,
  `mycotoxin_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fungus_id` (`fungus_id`),
  KEY `mycotoxin_id` (`mycotoxin_id`),
  CONSTRAINT `present_toxins_ibfk_1` FOREIGN KEY (`fungus_id`) REFERENCES `fungi` (`id`) ON DELETE CASCADE,
  CONSTRAINT `present_toxins_ibfk_2` FOREIGN KEY (`mycotoxin_id`) REFERENCES `mycotoxins` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `lookalikes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fungus1_id` int NOT NULL,
  `fungus2_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fungus1_id` (`fungus1_id`),
  KEY `fungus2_id` (`fungus2_id`),
  CONSTRAINT `lookalikes_ibfk_1` FOREIGN KEY (`fungus1_id`) REFERENCES `fungi` (`id`) ON DELETE CASCADE,
  CONSTRAINT `lookalikes_ibfk_2` FOREIGN KEY (`fungus2_id`) REFERENCES `fungi` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;