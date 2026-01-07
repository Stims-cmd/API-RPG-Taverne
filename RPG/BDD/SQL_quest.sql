DROP TABLE IF EXISTS quests;

CREATE TABLE `quests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `reward` int NOT NULL,
  `base_reward` int NOT NULL DEFAULT 0,
  `status` varchar(50) NOT NULL,
  `modified` boolean NOT NULL DEFAULT FALSE,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `quests` (`id`, `title`, `description`, `reward`, `base_reward`, `status`, `modified`) VALUES
(1, 'Protéger la caravane', 'Le cousin Momo dit qu’il a vu des gens rôder près du camp.', 50, 50, '', FALSE),
(2, 'Le casse de la ferraille bénite', 'Un voleur a pris ton radiateur en cuivre.', 75, 75, '', FALSE),
(3, 'Le champion du barbecue', 'Fais cuire un sanglier entier avant la tombée du jour.', 50, 50, '', FALSE),
(4, 'Du gasoil ou du sang', 'Siphonne trois véhicules avant le lever du jour.', 125, 125, '', FALSE),
(5, 'Le rêve de Kevin', 'Monte des pièces de tuning sur ta voiture.', 60, 60, '', FALSE),
(6, 'Le trésor du lithium', 'On raconte qu’un stock de batteries est enterré sous un rond-point.', 40, 40, '', FALSE),
(7, 'Le camion du destin', 'Remplis ta benne de ferraille en ville.', 50, 50, '', FALSE),
(8, 'Mariachh et Niversaaaaiiire !', 'Lance un service d’événements original.', 40, 40, '', FALSE),
(9, 'La SNCF est en retard (encore)', 'Récupère des câbles abandonnés sur les rails.', 50, 50, '', FALSE),
(10, 'Le calibre de Kendji', 'Apprends à manier ton équipement en toute sécurité.', 50, 50, '', FALSE);

COMMIT;
