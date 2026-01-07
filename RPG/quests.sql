-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : db:3306
-- Généré le : lun. 05 jan. 2026 à 13:53
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `quests_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `quests`
--

CREATE TABLE `quests` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `reward` int NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `quests`
--

INSERT INTO `quests` (`id`, `title`, `description`, `reward`, `status`) VALUES
(1, 'Protéger la caravane', 'Le cousin Momo dit qu’il a vu des gadjé rôder près du camp. Achète un douze, sors le Dobermann, et montre-leur que la caravane, c’est sacré, frère.', 50, ''),
(2, 'Le casse de la ferraille bénite', 'Un gadjo a volé ton radiateur en cuivre béni par le padrino. Infiltre sa casse, récupère ta ferraille... et pourquoi pas sa roumnia aussi, pour l’honneur.\r\n', 75, ''),
(3, 'Le champion du barbecue ', 'Le feu c’est la vie, frère. Fais cuire un sanglier entier avant la tombée du jour avec un tas de pneus et trois bidons d’essence. Si ça fume pas jusqu’à la nationale, c’est raté.', 50, ''),
(4, 'Du gasoil ou du sang', 'Ta bagnole a soif, et les stations sont fermées. Siphonne trois véhicules avant le lever du jour. Fais vite, les keufs aiment pas les bricoleurs de nuit.', 125, ''),
(5, 'Le rêve de Kevin', 'Ta 306 mérite le respect du clan. Monte-lui des pièces de tuning, des bandes LED Temu, un aileron de Boeing, et roule vers la gloire. Si ça clignote plus qu’un mariage à Carpentas, t’as gagné.', 60, ''),
(6, 'Le trésor du lithium', 'On raconte que sous un vieux rond-point, y’a un stock de batteries lithium oubliées. Déterre le trésor avec la tribu et va le revendre au marché noir. Le cuivre, c’est fini, le futur, c’est les piles !', 40, ''),
(7, 'Le camion du destin', 'Monte dans ton vieux camion, fais le tour de la ville et remplis ta benne de ferraille. Plus t’en trouves, plus t’es respecté au camp. N’oublie pas : tout ce qui brille, c’est métal.', 50, ''),
(8, 'Mariachh et Niversaaaaiiire !', 'Ta femme veut lancer Mariachhhh & Niversaaaaaire, un service d’événements un peu spéciale. Il deviendra connu sur les réseaux.', 40, ''),
(9, 'La SNCF est en retard (encore)', 'Y’a des kilomètres de câbles qui dorment sur les rails, mon frère. Va leur “alléger” un peu la voie et ramène tout au camp. Fais vite avant que les flics comprennent pourquoi plus rien roule.\r\n', 50, ''),
(10, 'Le calibre de Kendji', 'Apprends à manier ton fusil et ta meuf sans te tirer dessus — y’en a qu’ont essayé, y chantent moins bien maintenant.', 50, '');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `quests`
--
ALTER TABLE `quests`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `quests`
--
ALTER TABLE `quests`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;